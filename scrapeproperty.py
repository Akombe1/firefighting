import requests
from bs4 import BeautifulSoup
import csv
import time

# Base URL
base_url = "https://www.bostonplans.org"
view_all_url = f"{base_url}/projects/development-projects?viewall=1"

# Headers for the CSV file
headers = [
    "Project Name",
    "Address",
    "Status",
    "Project Type",
    "Neighborhood",
    "Square Footage",
    "Units",
    "Project URL"
]

def get_project_list():
    print(f"Fetching all projects from: {view_all_url}")
    response = requests.get(view_all_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    projects = []
    
    # Find the project listings container
    listings = soup.find('div', class_='projectTableWrapper')
    
    if not listings:
        print("Could not find project listings container")
        return projects
    
    # Find all project entries
    for project in listings.find_all('table', class_='devprojectTable'):
        # Extract project name and URL

        title_tag = project.find('caption').find('a') if project.find('caption') else None
        if not title_tag:
            continue
            
        project_name = title_tag.text.strip()
        project_url = f"{base_url}{title_tag['href']}"
        
        # Extract address
        address = title_tag
        
        # Extract status
        table_cols = project.find_all("th")
        
        status = table_cols[0].find("h2").text.strip() if table_cols[0].find("h2") else 'N/A'
        
        project_type = table_cols[1].find("h2").text.strip() if table_cols[1].find("h2") else 'N/A'
        
        neighborhood = table_cols[2].find("h2").text.strip() if table_cols[2].find("h2") else 'N/A'
    
        # Extract square footage and units (these might need individual page scraping)
        square_footage = 'N/A'
        units = 'N/A'
        
        projects.append([
            project_name, # 0
            address, # 1
            status, # 2
            project_type, # 3
            neighborhood, # 4
            square_footage, # 5
            units, # 6
            project_url # 7
        ])
    
    print(f"Found {len(projects)} projects")
    return projects

def get_project_details(project_url):
    try:
        response = requests.get(project_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract square footage
        square_footage = 'N/A'
        sqft_div = soup.find('div', class_='field--name-field-square-footage')
        if sqft_div:
            square_footage = sqft_div.find('div', class_='field__item').text.strip()
        
        # Extract address
        units = 'N/A'
        address_div = soup.find('div', class_='field--name-address')
        if units_div:
            units = units_div.find('div', class_='field__item').text.strip()

        # Extract units
        units = 'N/A'
        units_div = soup.find('div', class_='field--name-field-units')
        if units_div:
            units = units_div.find('div', class_='field__item').text.strip()
        
        return square_footage, address, units
        
    except Exception as e:
        print(f"Error scraping {project_url}: {str(e)}")
        return 'N/A', 'N/A'

def scrape_projects():
    projects = get_project_list()
    
    # Now get additional details for each project
    for i, project in enumerate(projects):
        print(f"Processing project {i+1}/{len(projects)}: {project[0]}")
        square_footage, units = get_project_details(project[-1])  # URL is at index 7
        project[5] = square_footage  # Update square footage
        project[6] = units  # Update units
        time.sleep(0.25)  # Be polite to the server
    
    # Write to CSV
    with open('bpda_projects_full.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(projects)
    
    print(f"Successfully saved {len(projects)} projects to bpda_projects_full.csv")

if __name__ == "__main__":
    scrape_projects()