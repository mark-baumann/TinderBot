
# TinderBot 2025 - Automatisierter Tinder Swiper mit Facebook-Login

**TinderBot 2025** ist ein Python-Skript, das speziell für das Tinder-Web-Interface im Jahr 2025 entwickelt wurde. Dieser Bot nutzt **Selenium**, um die Tinder-Webseite zu automatisieren, sich über Facebook anzumelden und automatisch Swipes nach rechts zu tätigen. Beachte, dass Tinder seine DOM-Struktur regelmäßig ändert, wodurch viele bestehende Bots nicht mehr funktionieren. Dieser Bot wurde speziell an das DOM von **2025** angepasst, um die aktuelle Funktionsweise zu gewährleisten.

---

## 🚨 Wichtiger Hinweis:
Dieser Bot funktioniert **nur** mit dem aktuellen Tinder-Website DOM von **2025**! Da Tinder regelmäßig Änderungen an der Webseite vornimmt, ist es wahrscheinlich, dass dieser Bot in der Zukunft nicht mehr funktioniert, wenn das DOM geändert wird. Bitte überprüfe regelmäßig, ob der Bot noch funktioniert, oder passe ihn an neue Versionen der Seite an.

---

## Funktionen:

- **Automatisches Facebook-Login**: Der Bot meldet sich über Facebook bei Tinder an.
- **Popup-Handling**: Der Bot schließt automatisch alle wichtigen Popups wie Cookie-Banner, Standortanfragen und Berechtigungs-Popups.
- **Swipe nach rechts**: Der Bot führt automatisierte Swipes nach rechts auf Tinder durch, um Profile zu liken.
- **Periodisches Swipen**: Der Bot führt alle Stunde maximal 50 Swipes durch und wartet dann eine Stunde, bevor der nächste Zyklus beginnt.
- **Benutzerfreundlichkeit**: Der Bot geht mit unerwarteten Popups und Änderungen im DOM um.

---

## 🚀 Installation:

1. **Abhängigkeiten installieren**:
   - Stelle sicher, dass du Python 3 oder eine neuere Version installiert hast.
   - Installiere die benötigten Python-Pakete mit:
   ```bash
   pip install selenium
   ```

2. **Chrome WebDriver installieren**:
   - Lade den **Chrome WebDriver** von [hier](https://sites.google.com/a/chromium.org/chromedriver/) herunter und stelle sicher, dass der WebDriver in deinem Systempfad verfügbar ist.

3. **Facebook-Zugangsdaten**:
   - Ersetze die Platzhalter `email` und `password` im Skript durch deine Facebook-Zugangsdaten.

---

## 🛠 Nutzung:

1. **Skript ausführen**:
   - Öffne die Kommandozeile und führe das Skript aus:
   ```bash
   python tinder_bot.py
   ```

2. **Bot-Interaktionen**:
   - Der Bot öffnet die Tinder-Webseite und führt den Facebook-Login durch.
   - Nachdem der Login abgeschlossen ist, beginnt der Bot automatisch mit dem Swipen von Tinder-Profilen. Der Bot swiped alle Stunde maximal 50 Profile nach rechts.

3. **Warte auf manuelle Captcha-Lösung**:
   - Wenn ein Captcha erscheint, pausiert der Bot und fordert dich auf, das Captcha manuell zu lösen. Der Bot wartet, bis du das Captcha gelöst hast.

4. **Bot schließt sich automatisch**:
   - Der Bot schließt den Browser nach dem Abschluss seiner Aufgabe.

---

## 📄 Hinweise:

- Der Bot nutzt Selenium, um eine Webbrowser-Instanz zu automatisieren, daher muss der Chrome WebDriver korrekt installiert und konfiguriert sein.
- **Facebook-Zugangsdaten** sind erforderlich, um den Login-Prozess zu automatisieren.
- Der Bot funktioniert **nur mit dem aktuellen DOM von 2025**! Bei zukünftigen Änderungen auf der Webseite kann der Bot nicht mehr wie erwartet funktionieren.
- Du solltest den Bot nicht übermäßig verwenden, um die Wahrscheinlichkeit einer Sperrung des Tinder-Kontos zu minimieren.
- Das Skript pausiert während der Captcha-Eingabe und erwartet von dir, dass du das Captcha manuell löst.

---

## ⚠️ Wichtige Hinweise:

- Tinder ändert regelmäßig die Struktur seiner Webseite (DOM), was dazu führen kann, dass viele Bots nicht mehr funktionieren. Dieser Bot wurde speziell für das **Tinder-Website-DOM von 2025** entwickelt.
- Stelle sicher, dass du die neueste Version des Skripts verwendest und achte darauf, dass die XPath-Selektoren noch gültig sind, wenn Tinder Änderungen an der Seite vornimmt.

---

## 📝 Lizenz:

- **MIT License** - Siehe [LICENSE](LICENSE).

---

## 🧑‍💻 Autor:

Dieses Projekt wurde von **Mark Baumann** erstellt.

---

### Viel Spaß beim Swipen! 🚀
