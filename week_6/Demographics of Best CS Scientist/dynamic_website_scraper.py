import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--chromedriver_path', type=str, help= "check where the chromedriver is in your pc and share the path")
args = parser.parse_args()

columns = ["World Rank", "National Rank", "Name", "Image URLs", "Affiliation", "Country", "H-Index", "Citations", "#DBLP"]

def get_scholar_details(row):
    try:
        details = row.text.split('\n')
        # if len(details) < 7:
        #     print("Skipping row due to insufficient data:", details)
        #     return None
        contents = {}
        contents["World Rank"] =        details[0]
        contents["National Rank"] =     details[1]
        contents["Name"] =              details[2]
        contents["Affiliation"] =       details[3].split(',')[0]
        contents["Country"] =           details[3].split(',')[1].strip() if ',' in details[3] else ""
        contents["H-Index"] =           details[4]
        contents["Citations"] =         details[5].replace(',', '')
        contents["#DBLP"] =             details[6].replace(',', '')
        try:
            contents["Image URLs"] =    row.find_element(By.CLASS_NAME, 'lazyload').get_attribute('src')
        except:
            contents["Image URLs"] = ""
        return contents
    except:
        return None

def main():
    webdriver_path = args.chromedriver_path
    scholar_data = []
    
    print("Starting web scraping...")
    for page_id in range(1, 11):
        service = Service(executable_path=webdriver_path)
        driver = webdriver.Chrome(service=service)
        page_url = f"https://research.com/scientists-rankings/computer-science?page={page_id}"
        driver.get(page_url)
        
        rankings = driver.find_element(By.ID, "rankingItems")
        rows = rankings.find_elements(By.CLASS_NAME, "cols")
        
        print(f"Scraping page {page_id} processing...")
        for row in rows:
            data = get_scholar_details(row)
            if data:
                scholar_data.append(data)
        driver.quit()
        print(f"Page {page_id} has been completed successfully.")
        print("----------------------------------------")
        
        
    df = pd.DataFrame(scholar_data, columns=columns)
    df.to_csv("data/computer_science_scientists.csv", index=False)
    print("Process completed successfully! Data saved to 'computer_science_scientists.csv'")

if __name__ == "__main__":
    main()
