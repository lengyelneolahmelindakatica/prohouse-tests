import pytest
from generate_driver import get_preconfigured_chrome_driver
from main_page import MainPage
from RegistrationPage import RegistrationPage
from SignIn import SignIn
import json
import csv
from datetime import datetime
import os

@pytest.fixture(scope="function")
def driver():
    # WebDriver inicializálása a generate_driver.py segítségével
    driver = get_preconfigured_chrome_driver()
    driver.set_window_size(1024, 768)  # Ablakméret beállítása minden teszthez
    yield driver
    # Teszt végeztével bezárjuk a böngészőt
    driver.quit()

@pytest.fixture(scope="function")
def main_page(driver):
    # MainPage objektum inicializálása
    page = MainPage(driver)
    page.get()  # Navigálunk a főoldalra
    return page

@pytest.fixture(scope="function")
def registration_page(driver):
    # RegistrationPage objektum inicializálása
    return RegistrationPage(driver)

@pytest.fixture(scope="function")
def signin_page(driver):
    # SignIn objektum inicializálása
    return SignIn(driver)

@pytest.fixture(scope="session")
def base_url():
    # Közös URL definiálása
    return "http://localhost:4200"


def pytest_sessionfinish(session, exitstatus):
    """Test session befejezése után automatikus összegzés generálás"""

    # Test results összegyűjtése
    passed = len([item for item in session.items if hasattr(item, 'rep_call') and item.rep_call.passed])
    failed = len([item for item in session.items if hasattr(item, 'rep_call') and item.rep_call.failed])
    skipped = len([item for item in session.items if hasattr(item, 'rep_call') and item.rep_call.skipped])

    # Ha nincs rep_call, akkor a pytest internal stats-ot használjuk
    if hasattr(session, 'testsfailed'):
        failed = session.testsfailed
    if hasattr(session, 'testscollected'):
        total = session.testscollected
        passed = total - failed - skipped

    # Execution summary
    end_time = datetime.now()
    duration = getattr(session, '_session_start_time', end_time)
    if hasattr(session, '_session_start_time'):
        duration = (end_time - session._session_start_time).total_seconds()
    else:
        duration = 0

    summary = {
        "timestamp": end_time.strftime("%Y-%m-%d %H:%M:%S"),
        "sprint": "Sprint-1",
        "project": "Moovsmart",
        "total_tests": getattr(session, 'testscollected', passed + failed + skipped),
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "success_rate": round((passed / max(1, passed + failed)) * 100, 2),
        "duration_seconds": round(duration, 2),
        "exit_status": exitstatus
    }

    # JSON log file-ba írás (append mode)
    json_log_file = "test_execution_log.json"

    # Ha nincs file, akkor lista kezdése
    if not os.path.exists(json_log_file):
        with open(json_log_file, "w") as f:
            json.dump([summary], f, indent=2)
    else:
        # Meglévő JSON olvasása
        try:
            with open(json_log_file, "r") as f:
                existing_data = json.load(f)
        except:
            existing_data = []

        # Új eredmény hozzáadása
        existing_data.append(summary)

        # Visszaírás
        with open(json_log_file, "w") as f:
            json.dump(existing_data, f, indent=2)

    # CSV summary is (egyszerűbb Excel-hez)
    csv_log_file = "test_summary.csv"
    file_exists = os.path.exists(csv_log_file)

    with open(csv_log_file, "a", newline='') as f:
        writer = csv.writer(f)

        # Header írása ha új file
        if not file_exists:
            writer.writerow([
                "Timestamp", "Sprint", "Project", "Total_Tests",
                "Passed", "Failed", "Skipped", "Success_Rate_%",
                "Duration_Sec", "Exit_Status"
            ])

        # Adatok írása
        writer.writerow([
            summary["timestamp"],
            summary["sprint"],
            summary["project"],
            summary["total_tests"],
            summary["passed"],
            summary["failed"],
            summary["skipped"],
            summary["success_rate"],
            summary["duration_seconds"],
            summary["exit_status"]
        ])

    # Console kiírás
    print("\n" + "=" * 60)
    print("TEST EXECUTION SUMMARY")
    print("=" * 60)
    print(f"Project: {summary['project']} - {summary['sprint']}")
    print(f"Timestamp: {summary['timestamp']}")
    print(f"Total Tests: {summary['total_tests']}")
    print(f"✅ Passed: {summary['passed']}")
    print(f"❌ Failed: {summary['failed']}")
    print(f"⏭️  Skipped: {summary['skipped']}")
    print(f"📊 Success Rate: {summary['success_rate']}%")
    print(f"⏱️  Duration: {summary['duration_seconds']} seconds")
    print(f"Exit Code: {summary['exit_status']}")
    print("=" * 60)

    # Eredmény file path kiírása
    print(f"📄 Detailed results saved to: {json_log_file}")
    print(f"📈 CSV summary saved to: {csv_log_file}")


def pytest_sessionstart(session):
    """Session start time rögzítése"""
    session._session_start_time = datetime.now()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Test results capture hook"""
    outcome = yield
    rep = outcome.get_result()

    # Report mentése az item-hez
    setattr(item, f"rep_{rep.when}", rep)