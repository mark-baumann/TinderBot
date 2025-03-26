import time
import pickle
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TinderBot:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = None

    def setup_driver(self):
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        self.driver.get("https://tinder.com")
        self.wait = WebDriverWait(self.driver, 10)

    def click_element(self, xpath, description=""):
        """ Klicke ein Element, wenn es existiert. Falls nicht, überspringen. """
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)
            print(f"✅ {description} wurde erfolgreich geklickt.")
        except Exception:
            print(f"⚠️ {description} wurde nicht gefunden oder konnte nicht geklickt werden.")

    def handle_all_popups(self):
        """ Prüft auf alle möglichen Popups und schließt sie. """
        popups = {
            "Cookies akzeptieren": "/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]",
            "Cookies akzeptieren (zweites Popup)": "/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]",
            "Standortfreigabe": "/html/body/div[2]/div/div/div/div/div[3]/button[1]/div[2]/div[2]",
            "Berechtigungs-Popup": "/html/body/div[2]/div/div[1]/div/div/div[3]/button[1]/div[2]/div[2]",
            "Tinder zum Startbildschirm hinzufügen": "/html/body/div[2]/div/div/div[2]/button[1]/div[2]/div[2]",
            "Superlike Popup": "/html/body/div[2]/div/div/button[2]/div[2]/div[2]",
        }

        for description, xpath in popups.items():
            self.click_element(xpath, description)

    def login_facebook(self):
        print("🔵 Starte Facebook-Login...")

        # Tinder Login-Button anklicken
        self.click_element(
            "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a",
            "Tinder Login-Button")

        # Facebook-Login auswählen
        self.click_element(
            "/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]",
            "Facebook-Login auswählen")

        # Warten, bis Facebook-Login-Tab geöffnet wird
        self.wait.until(lambda driver: len(self.driver.window_handles) > 1)

        # Fensterwechsel zum Facebook-Login-Fenster
        all_window_handles = self.driver.window_handles
        self.driver.switch_to.window(all_window_handles[1])

        # Facebook-Anmeldedaten eingeben
        self.enter_text("/html/body/div/div[2]/div[1]/form/div/div[1]/div/input", self.email, "Facebook Email")
        self.enter_text("/html/body/div/div[2]/div[1]/form/div/div[2]/div/input", self.password, "Facebook Passwort")

        # Facebook-Login absenden
        self.click_element("/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input", "Facebook Login-Button")

        # Warten auf manuelle Captcha-Eingabe
        print("🟡 Bitte löse das Captcha manuell.")
        time.sleep(30)  # Wartezeit für Captcha

        # Zurück zum Haupt-Tinder-Fenster wechseln
        self.driver.switch_to.window(all_window_handles[0])

    def enter_text(self, xpath, text, description=""):
        """ Text in ein Feld eingeben, wenn es existiert. """
        try:
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            element.send_keys(text)
            print(f"✅ {description} wurde erfolgreich eingegeben.")
        except Exception:
            print(f"⚠️ {description} konnte nicht eingegeben werden.")

    def swipe_right(self, max_swipes=50):
        """ Swipe nach rechts für maximal 'max_swipes' Mal innerhalb einer Stunde. """
        body = self.driver.find_element(By.TAG_NAME, "body")
        for i in range(max_swipes):
            try:
                # Popups während des Swipens behandeln
                self.handle_all_popups()

                body.send_keys(Keys.ARROW_RIGHT)
                print(f"👉 Swipe {i + 1}/{max_swipes} nach rechts erfolgreich!")
                time.sleep(2)
            except Exception:
                print(f"⚠️ Swipe {i + 1} konnte nicht durchgeführt werden.")
                break

    def perform_tinder_action(self):
        """ Führe Aktionen auf Tinder aus (z. B. Swipen oder Like). """
        if len(self.driver.window_handles) == 0:
            print("❌ Browser-Fenster ist geschlossen. Skript wird beendet.")
            return

        # Sicherstellen, dass das richtige Fenster aktiv ist
        self.driver.switch_to.window(self.driver.window_handles[0])

        # Alle möglichen Popups schließen
        self.handle_all_popups()

        # Swipen starten
        self.swipe_right()

    def close(self):
        self.driver.quit()
        print("❌ Browser wurde geschlossen.")

    def start_swiping_cycle(self, interval=3600, swipes_per_cycle=50):
        """ Startet einen Swiping-Zyklus, der alle Stunde ausgeführt wird. """
        while True:
            print("🕒 Starte neuen Swiping-Zyklus...")
            self.perform_tinder_action()
            print(f"⏳ Warten für {interval / 3600} Stunden bis zum nächsten Zyklus...")
            time.sleep(interval)


if __name__ == "__main__":
    email = "kontakt@markb.de"  # Deine Facebook-E-Mail
    password = "Mustang_<3"  # Dein Facebook-Passwort

    bot = TinderBot(email, password)
    bot.setup_driver()
    bot.login_facebook()

    # Starte Swiping-Zyklus (alle Stunde maximal 50 Swipes)
    bot.start_swiping_cycle(interval=3600, swipes_per_cycle=50)

    # Drücke Enter, um den Browser zu schließen
    input("Drücke Enter, um den Browser zu schließen...")
    bot.close()
