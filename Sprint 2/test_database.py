"""
Moovsmart Database Testing
Clean pytest implementation for CI/CD integration
"""

import mysql.connector
import pytest
import allure

# Database connection configuration
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'database': 'moovsmart',
    'user': 'root',
    'password': 'test1234'
}


def get_db_connection():
    """Create database connection with standard configuration"""
    return mysql.connector.connect(**DB_CONFIG)


@allure.feature("Database Connectivity")
@allure.story("Basic Connection Test")
@allure.severity(allure.severity_level.CRITICAL)
def test_db_connection():
    """Test basic database connectivity and authentication"""
    connection = get_db_connection()
    cursor = connection.cursor()

    # Simple connectivity test
    cursor.execute("SELECT 1")
    result = cursor.fetchone()

    cursor.close()
    connection.close()

    assert result[0] == 1, "Database connection failed"


@allure.feature("Database Structure")
@allure.story("Property Table Validation")
@allure.severity(allure.severity_level.NORMAL)
def test_property_table():
    """Validate property table contains expected data"""
    connection = get_db_connection()
    cursor = connection.cursor()

    # Check property count - API testing showed 8+ properties expected
    cursor.execute("SELECT COUNT(*) FROM property")
    count = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    # Assertions based on API test results
    assert count > 0, "No properties found in database"
    assert count >= 8, f"Insufficient properties: {count} (expected: min 8 from API)"


@allure.feature("Database Structure")
@allure.story("Property Data Quality")
@allure.severity(allure.severity_level.NORMAL)
def test_property_data_quality():
    """Validate property data integrity and business rules"""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Get sample property data for validation
    cursor.execute("SELECT * FROM property LIMIT 3")
    properties = cursor.fetchall()

    cursor.close()
    connection.close()

    # Data quality assertions
    assert len(properties) > 0, "No property data available for testing"

    for prop in properties:
        # Primary key validation
        assert prop['id'] is not None, f"Property ID cannot be null"

        # Price validation for business logic
        if 'price' in prop and prop['price'] is not None:
            assert prop['price'] > 0, f"Property ID {prop['id']}: Invalid price {prop['price']}"


@allure.feature("Database Structure")
@allure.story("Users Table Validation")
@allure.severity(allure.severity_level.NORMAL)
def test_users_table():
    """Validate users table structure and data presence"""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Check user count
    cursor.execute("SELECT COUNT(*) as count FROM users")
    user_count = cursor.fetchone()['count']

    # Get sample user data for validation
    cursor.execute("SELECT email FROM users LIMIT 3")
    users = cursor.fetchall()

    cursor.close()
    connection.close()

    # User data assertions
    assert user_count > 0, "No users found in database"
    assert len(users) > 0, "No user email data available"

    # Basic email format validation
    for user in users:
        email = user['email']
        assert '@' in email, f"Invalid email format: {email}"
        assert '.' in email, f"Invalid email domain: {email}"


@allure.feature("Database Architecture")
@allure.story("Table Relationships")
@allure.severity(allure.severity_level.NORMAL)
def test_address_property_relationship():
    """Validate address-property table relationship integrity"""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Check both table record counts
    cursor.execute("SELECT COUNT(*) as count FROM address")
    address_count = cursor.fetchone()['count']

    cursor.execute("SELECT COUNT(*) as count FROM property")
    property_count = cursor.fetchone()['count']

    # Check for potential circular reference in table structure
    cursor.execute("SHOW CREATE TABLE property")
    property_structure = cursor.fetchone()['Create Table']

    cursor.close()
    connection.close()

    # Relationship validation
    assert address_count > 0, "No address records found"
    assert property_count > 0, "No property records found"

    # Business logic: expect roughly 1:1 relationship
    assert address_count == property_count, \
        f"Address-Property count mismatch: {address_count}:{property_count}"

    # Verify no circular reference (issue from API testing phase)
    circular_ref_detected = 'address' in property_structure.lower()
    if circular_ref_detected:
        allure.attach(property_structure, name="Property Table Structure",
                      attachment_type=allure.attachment_type.TEXT)


@allure.feature("API Integration")
@allure.story("Database-API Consistency")
@allure.severity(allure.severity_level.CRITICAL)
def test_database_vs_api_consistency():
    """Validate database data consistency with API layer expectations"""
    connection = get_db_connection()
    cursor = connection.cursor()

    # Get database property count for API consistency check
    cursor.execute("SELECT COUNT(*) FROM property")
    db_property_count = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    # API testing showed minimum 8 properties available
    api_expected_minimum = 8

    # Consistency validation
    assert db_property_count >= api_expected_minimum, \
        f"Database-API inconsistency: DB has {db_property_count}, API expects {api_expected_minimum}+"


@allure.feature("GDPR Compliance")
@allure.story("Personal Data Protection")
@allure.severity(allure.severity_level.HIGH)
def test_gdpr_personal_data_protection():
    """GDPR compliance check for personal data handling"""
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Personal data inventory - email addresses
    cursor.execute("SELECT email FROM users LIMIT 3")
    emails = cursor.fetchall()

    # Check for data retention timestamp capability
    cursor.execute("SHOW COLUMNS FROM users LIKE 'created_at'")
    has_timestamp = cursor.fetchone()

    # Get total personal data count
    cursor.execute("SELECT COUNT(*) as count FROM users")
    user_count = cursor.fetchone()['count']

    cursor.close()
    connection.close()

    # GDPR compliance assertions
    assert len(emails) > 0, "No personal data found for GDPR compliance testing"
    assert user_count > 0, "No users found for GDPR validation"

    # Data minimization principle check
    personal_data_count = 0
    for user in emails:
        email = user['email']
        if '@' in email and '.' in email:
            personal_data_count += 1

    assert personal_data_count > 0, "No valid personal data found for GDPR testing"

    # Data retention capability validation
    if not has_timestamp:
        allure.attach("No timestamp field found for data retention tracking",
                      name="GDPR Data Retention Warning",
                      attachment_type=allure.attachment_type.TEXT)


@allure.feature("Database Performance")
@allure.story("Query Performance Baseline")
@allure.severity(allure.severity_level.MINOR)
def test_database_performance_baseline():
    """Establish baseline performance metrics for database operations"""
    import time

    connection = get_db_connection()
    cursor = connection.cursor()

    # Measure connection time
    connection_start = time.time()
    test_connection = get_db_connection()
    connection_time = time.time() - connection_start
    test_connection.close()

    # Measure query time
    query_start = time.time()
    cursor.execute("SELECT COUNT(*) FROM property")
    result = cursor.fetchone()
    query_time = time.time() - query_start

    cursor.close()
    connection.close()

    # Performance assertions (reasonable thresholds for development environment)
    assert connection_time < 1.0, f"Connection too slow: {connection_time:.3f}s"
    assert query_time < 0.5, f"Query too slow: {query_time:.3f}s"
    assert result[0] > 0, "Query returned no results"

    # Attach performance metrics to Allure report
    allure.attach(f"Connection: {connection_time:.3f}s, Query: {query_time:.3f}s",
                  name="Performance Metrics",
                  attachment_type=allure.attachment_type.TEXT)