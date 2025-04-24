import requests
from bs4 import BeautifulSoup
import csv
import time

# Base URL
base_url = "https://www.bostonplans.org"

# URL of the filtered development projects page (Board Approved, sorted by filed date)
projects_url = f"{base_url}/projects/development-projects?projectstatus=board+approved&sortby=filed&sortdirection=DESC&viewall=1"

# Headers for the CSV file
headers = [
    "Address",
    "Status",
    "Latest Filed Date",
    "Neighborhood",
    "Square Footage",
    "Gross Land Area",
    "Project Description"
]

# List to store project data
projects_data = []

# Function to extract project details from the view-all page
def get_project_list():
    print("Fetching all Board Approved projects...")
    response = requests.get(projects_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract project links from projectListItem divs
    project_links = []
    project_cards = soup.find_all('div', class_='projectListItem')

    for card in project_cards:
        a_tag = card.find('a', href=True)
        if a_tag:
            address = a_tag.text.strip()
            href = a_tag['href']
            full_url = f"{base_url}{href}"
            project_links.append((address, full_url))

    print(f"Found {len(project_links)} Board Approved projects.")
    return project_links

# Function to extract details from individual project pages
def get_project_details(project_url):
    response = requests.get(project_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract Neighborhood
    neighborhood_div = soup.find('div', class_='bpdaPrjDetails')
    neighborhood = neighborhood_div.text.strip() if neighborhood_div else ''

    # Extract Square Footage and Gross Land Area
    square_footage = ''
    gross_land_area = ''
    bpda_details = soup.find_all('div', class_='bpdaPrjDetails')
    for detail in bpda_details:
        text = detail.text.strip()
        if 'sq ft' in text.lower():
            if not square_footage:
                square_footage = text
            elif not gross_land_area:
                gross_land_area = text
                break

    # Extract Project Description
    description_div = soup.find('div', style=lambda value: value and 'font-size:20px' in value)
    project_description = description_div.text.strip() if description_div else ''

    # Extract Status
    status = ''
    status_header = soup.find('span', string="Project Status")
    if status_header and status_header.parent:
        status = status_header.parent.text.replace("Project Status", "").strip()

    # Extract Latest Filed Date
    latest_filed_date = ''
    filed_date_header = soup.find('span', string="Latest Filed Date")
    if filed_date_header and filed_date_header.parent:
        latest_filed_date = filed_date_header.parent.text.replace("Latest Filed Date", "").strip()

    return neighborhood, square_footage, gross_land_area, project_description, status, latest_filed_date

# Main function to scrape data and write to CSV
def scrape_projects():
    project_list = get_project_list()

    for address, project_url in project_list:
        print(f"Processing: {address}")

        # Visit the project page to get additional details
        neighborhood, square_footage, gross_land_area, project_description, status, latest_filed_date = get_project_details(project_url)

        # Append the data
        projects_data.append([
            address,
            status,
            latest_filed_date,
            neighborhood,
            square_footage,
            gross_land_area,
            project_description
        ])

        # Sleep to be polite to the server
        time.sleep(1)

    # Write to CSV
    with open('bpda_board_approved_projects.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(projects_data)

    print("Data has been written to bpda_board_approved_projects.csv")

# Run the script
if __name__ == "__main__":
    scrape_projects()