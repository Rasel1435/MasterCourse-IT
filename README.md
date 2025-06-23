# MasterCourse-IT

# Demographics of Best CS Scientist

## Build From Sources and Run the Selenium Scraper
1. Clone the repo
```bash
  git clone https://github.com/Rasel1435/MasterCourse-IT.git
```
2. Initialize and activate the virtual environment
```bash
  virtualenv --no-site-packages  venv
  source venv/bin/activate
```
3. Install dependencies
```bash
  pip install -r requirements.txt
```
4. Download Chrome WebDrive from https://googlechromelabs.github.io/chrome-for-testing
5. Run the scraper
```bash
  python week_6/Demographics of Best CS Scientist/dynamic_website_scraper.py --chromedriver_path <path_to_chromedriver>
```
You will get a file named `computer_science_scientists.csv` containing all the required fields

Tableau Public URL: https://public.tableau.com/app/profile/sheikh.rasel.ahmed/viz/DemographicsofBestCSScientist_17501649413280/Dashboard1
