
# 🧭 Tesztterv – Prohouse kezdőoldal (Tesztelési logika)

## 🎯 Cél:
A főoldal első betöltési állapotának, alapvető működésének, vizuális elemeinek és elérhetőségének ellenőrzése különböző felhasználói környezetekben.

## 🧪 1. Smoke teszt – Főoldal desktop nézeten

| Tesztcél | Ellenőrzés típusa | Megjegyzés |
|----------|-------------------|------------|
| Oldal betöltése | Smoke | Nagy képernyőn, teljesen betöltött oldal |
| Görgetés alulra | UI működés | Vizuális stabilitás, nem tűnik el semmi |
| Főbb elemek látszanak (Buy, Rent, Prohouse logó, keresőmező) | Vizsgálat | Smoke szinten elég a jelenlétük |
| Gombok elérhetőek (Sign in, Registration) | Navigáció | Kattinthatók, új oldalra navigálnak |
| Nyelvválasztó jelenik meg | Vizsgálat | Szúrópróbaszerűen váltani és ellenőrizni az oldalcímkéket |
| Keresőmező írható | Input kontroll | Placeholder megjelenik, kurzor aktív |
| Csempék megjelennek (ingatlanok) | Vizsgálat | Legalább 1–2 betölt |
| Lapozó nyilak működnek | Interakció | Reagálnak kattintásra |
| Kattintás egy csempére | Navigáció | Eljut a részletező oldalra |
| Visszagomb használata | Böngészési logika | Oldal visszanavigál a kezdőre (opcionális smoke-ba, de hasznos) |

📌 **Megjegyzés:** Ez a tesztelés asztali (desktop) nézeten történik nagy kijelzőn.  
🧪 **Ajánlott:** később egy külön UI regressziós teszt mobilos nézetre is.

---

## 📦 2. Funkcionális tesztek (külön ciklusban)

Ezek nem tartoznak a Smoke tesztbe, hanem funkcionális ciklusba vagy regressziós mappába kerülnek.

- Buy és Rent gomb funkció tesztelése (helyes lista betöltése)
- Keresés eredményei – különböző városnevekre
- Nyelvváltás hatása minden főbb szövegre (EN / HU)
- Részletes hirdetés oldal működése (kép, leírás, ár)
- Navigációs linkek aktívak-e minden nézetben

---

## 🔐 3. Pozitív/Negatív tesztek (későbbi ciklusba)

| Funkció | Pozitív eset | Negatív eset |
|---------|--------------|--------------|
| Regisztráció | Helyes adatokkal siker | Üres mezők, rossz e-mail, már létező e-mail |
| Bejelentkezés | Helyes adatokkal siker | Hibás jelszó, üres mező |
| Nyelvváltás | Teljes oldalváltás | Nem váltódik minden szöveg – hiba bejelentése |

---

## 📱 4. Eszköz- és nézetfüggő ellenőrzés

| Eszköz / Felbontás | Ellenőrzés típusa |
|--------------------|-------------------|
| Desktop (nagy képernyő) | Alapértelmezett Smoke teszt |
| Mobil (Chrome DevTools – iPhone SE / Android) | Vizuális kontroll, gombok használhatósága |
| Tablet | Görgetés és térkép kezelhetőség (később) |
