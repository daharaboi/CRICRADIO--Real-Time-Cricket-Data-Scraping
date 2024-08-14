# CRICRADIO--Real-Time-Cricket-Data-Scraping

## Overview
CRICRADIO--Real-Time-Cricket-Data-Scraping is a Python-based web scraping tool designed to monitor and extract match schedules and detailed match information from the CREX cricket website. This project allows users to automatically track and store data from the match listing page, including team names, scores, overs, match dates, and live status, directly into an Excel file.

## Features
- **Scrape Match List**: Extracts match URLs, team names, scores, overs, match dates, and live status from the CREX fixtures page.
- **Detailed Match Info**: Capable of scraping additional details from individual match pages under the "Match info," "Squads," "Live," and "Scorecard" tabs.
- **Automatic Excel File Creation**: Saves all scraped data into a well-organized Excel file, ready for analysis and reporting.
- **Real-Time Data Monitoring**: The system can be extended to monitor live matches and update the Excel file in real-time as the match progresses.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Required Libraries
Make sure you have the following Python libraries installed:
- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing HTML content.
- `pandas`: For handling data and exporting it to an Excel file.
- `openpyxl`: For working with Excel files.

You can install the required libraries using pip:
pip install requests beautifulsoup4 pandas openpyxl
