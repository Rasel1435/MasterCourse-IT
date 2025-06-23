# MasterCourse-IT

# Demographics of Best CS Scientist

## Problem Statement
This project aims to gather information on the best 1000 Computer Science researchers from <a href="https://research.com/scientists-rankings/best-scientists" target="_blank">this website</a>.</br>
Later, we utilized the scraped data to understand the following demographics and correlations using Tableau</br>Dashboard:

1. A bar chart of countries with average publications.
2. European countries with the number of scientists in a map (excluding Russia)
3. Which Middle Eastern universities are good at research? (using citations as metric)
4. Which column is directly correlated with the  World Rank column? We wanted to understand how the ranking was done.

You can visit the public dashboard <a href="https://public.tableau.com/app/profile/sheikh.rasel.ahmed/viz/DemographicsofBestCSScientist_17501649413280/Dashboard1" target="_blank">here</a>.

## Findings and Observations from the <a href="https://public.tableau.com/app/profile/sheikh.rasel.ahmed/viz/DemographicsofBestCSScientist_17501649413280/Dashboard1" target="_blank">Dashboard</a>.
1. Brazilian scientists have the highest average publications.
2. Researchers from King Abdullah University of Science and Technology (KAUST), Saudi Arabia, have the highest number of average citations.
3. Among European countries, the United Kingdom (UK) has the highest number of scientists among the top 1000.
4. The ranking was most probably done using H-Index.

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

