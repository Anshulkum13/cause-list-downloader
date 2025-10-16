import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

def fetch_cause_list(state, district, complex, court, date, all_courts):
    # Setup headless Chrome
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://services.ecourts.gov.in/ecourtindia_v6/?p=cause_list/index")
        time.sleep(2)

        # Select State
        Select(driver.find_element(By.ID, "sess_state_code")).select_by_visible_text(state)
        time.sleep(1)

        # Select District
        Select(driver.find_element(By.ID, "sess_dist_code")).select_by_visible_text(district)
        time.sleep(1)

        # Select Court Complex
        Select(driver.find_element(By.ID, "court_complex_code")).select_by_visible_text(complex)
        time.sleep(1)

        # Get all court names if needed
        court_names = []
        if all_courts:
            court_dropdown = Select(driver.find_element(By.ID, "court_code"))
            court_names = [opt.text for opt in court_dropdown.options if opt.text.strip()]
        else:
            court_names = [court]

        # Prepare output folder
        output_dir = "downloads"
        os.makedirs(output_dir, exist_ok=True)
        downloaded_files = []

        for court_name in court_names:
            Select(driver.find_element(By.ID, "court_code")).select_by_visible_text(court_name)
            time.sleep(1)

            # Set Date
            date_input = driver.find_element(By.ID, "from_date")
            date_input.clear()
            date_input.send_keys(date)
            time.sleep(1)

            # Submit
            driver.find_element(By.NAME, "submit").click()
            time.sleep(3)

            # Find PDF link
            try:
                pdf_link = driver.find_element(By.PARTIAL_LINK_TEXT, "PDF").get_attribute("href")
                response = requests.get(pdf_link)
                filename = f"{court_name.replace(' ', '_')}_{date}.pdf"
                filepath = os.path.join(output_dir, filename)
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                downloaded_files.append(filepath)
            except Exception as e:
                print(f"PDF not found for {court_name}: {e}")
                continue

            # Go back to form
            driver.back()
            time.sleep(2)

        # Return single file or zip
        if len(downloaded_files) == 1:
            return downloaded_files[0]
        elif len(downloaded_files) > 1:
            zip_path = os.path.join(output_dir, f"cause_lists_{date}.zip")
            import zipfile
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                for file in downloaded_files:
                    zipf.write(file, os.path.basename(file))
            return zip_path
        else:
            return None

    except Exception as e:
        print("Scraper error:", e)
        return None

    finally:
        driver.quit()