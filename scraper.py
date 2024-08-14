import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL
BASE_URL = "https://crex.live/fixtures/match-list"

# Function to get match details from the main list
def get_match_details():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.content, "html.parser")
    
    match_data = []

    # Find all match cards
    for match_card in soup.find_all('li', class_='match-card-container'):
        match_info = {}

        # Extract match URL
        match_link_tag = match_card.find('a', class_='match-card-wrapper')
        match_info['match_url'] = "https://crex.live" + match_link_tag['href']

        # Extract Team Names
        teams = match_card.find_all('div', class_='team-wrapper')
        match_info['team1_name'] = teams[0].find('span', class_='team-name').text.strip()
        match_info['team2_name'] = teams[1].find('span', class_='team-name').text.strip()

        # Extract Team Scores
        match_info['team1_score'] = teams[0].find('span', class_='team-score').text.strip() if teams[0].find('span', class_='team-score') else 'N/A'
        match_info['team2_score'] = teams[1].find('span', class_='team-score').text.strip() if teams[1].find('span', class_='team-score') else 'N/A'

        # Extract Overs
        match_info['team1_overs'] = teams[0].find('span', class_='total-overs').text.strip() if teams[0].find('span', class_='total-overs') else 'N/A'
        match_info['team2_overs'] = teams[1].find('span', class_='total-overs').text.strip() if teams[1].find('span', class_='total-overs') else 'N/A'

        # Extract live status (if the match is ongoing)
        live_status = match_card.find('div', class_='result live')
        match_info['live_status'] = live_status.find('span', class_='liveTag').text.strip() if live_status else 'Not Live'

        match_data.append(match_info)

    return match_data

# Function to save the data into an Excel file
def save_to_excel(match_data, filename):
    df = pd.DataFrame(match_data)
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")

# Main function to scrape and save data
def main():
    matches = get_match_details()
    save_to_excel(matches, 'crex_match_data.xlsx')

if __name__ == "__main__":
    main()
