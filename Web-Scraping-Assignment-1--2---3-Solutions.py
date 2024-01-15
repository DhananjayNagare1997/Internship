#!/usr/bin/env python
# coding: utf-8
1) Write a python program to display all the header tags from wikipedia.org and make data frame.
# In[6]:


# Install necessary libraries if not already installed
#!pip install bs4
#!pip install requests

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_wikipedia_headers(url):
    # Sending the get request
    response = requests.get(url)
    
    # Checking the response of requests
    if response.status_code == 200:
        # Now need to parse the HTML content of the page 
        soup = BeautifulSoup(response.text, 'html.parser')
    
        # Now need to find all the Header tags
        headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
        # Extract text from the header tags
        header_text = [header.get_text() for header in headers]
    
        # Now let's create a DataFrame with the headers text
        df = pd.DataFrame({'Header': header_text})
    
        # Now let's print the DataFrame
        print(df)
        
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        
        
# Now call the function & provide the URL        
get_wikipedia_headers("https://en.wikipedia.org/wiki/Main_Page")

2) Write s python program to display list of respected former presidents of India(i.e. Name , Term ofoffice)
from https://presidentofindia.nic.in/former-presidents.htm and make data frame.
"https://www.icc-cricket.com/rankings/team-rankings/mens/odi"

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_icc_team_rankings(url):
    # Sending the get request
    response = requests.get(url)
    
    # Checking the response of requests
    if response.status_code == 200:
        # Now need to parse the HTML content of the page 
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table containing team rankings data
        table = soup.find('table', {'class': 'table'})
        
        # Initialize empty lists to store data
        teams = []
        matches = []
        points = []
        ratings = []
        
        # Extract data from the table
        for row in table.find_all('tr')[1:11]:  # Extract top 10 teams, skip the header row
            columns = row.find_all('td')
            teams.append(columns[1].text.strip())
            matches.append(columns[2].text.strip())
            points.append(columns[3].text.strip())
            ratings.append(columns[4].text.strip())
            
        # Create a DataFrame
        rankings_df = pd.DataFrame({'Team': teams, 'Matches': matches, 'Points': points, 'Rating': ratings})

        return rankings_df
    
    else:
        # If the request was not successful, print an error message
        print(f"Error: Unable to fetch data from {url}")
        return None
    
# Example usage
icc_team_rankings = get_icc_team_rankings("https://www.icc-cricket.com/rankings/team-rankings/mens/odi")

if icc_team_rankings is not None:
    print("Top 10 Men's ODI Teams:")
    print(icc_team_rankings)

3) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data framea) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
b) Top 10 ODI Batsmen along with the records of their team andrating.
c) Top 10 ODI bowlers along with the records of their team andrating.
# In[12]:


#Ans:
import requests
from bs4 import BeautifulSoup
import pandas as pd

#Function for Display Teams rankings
def scrape_odi_team_rankings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting data for ODI teams
    teams = []
    matches = []
    points = []
    ratings = []

    for team in soup.find_all('span', class_='u-hide-phablet'):
        teams.append(team.text.strip())

    for data in soup.find_all('td', class_='rankings-block__banner--matches'):
        matches.append(data.text)

    for data in soup.find_all('td', class_='rankings-block__banner--points'):
        points.append(data.text)

    for data in soup.find_all('td', class_='rankings-block__banner--rating u-text-right'):
        ratings.append(data.text.strip())

    for data in soup.find_all('td', class_='table-body__cell u-center-text'):
        if 'matches' in data.text:
            matches.append(data.text)
        elif 'points' in data.text:
            points.append(data.text)
        elif 'rating' in data.text:
            ratings.append(data.text.strip())

    # Creating a DataFrame
    df = pd.DataFrame({
        'Team': teams[:10],
        'Matches': matches[:10],
        'Points': points[:10],
        'Rating': ratings[:10]
    })

    return df

#Function for Batsmen's ranking.
def scrape_odi_batsmen_rankings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting data for ODI batsmen
    players = []
    teams = []
    ratings = []

    for player in soup.find_all('div', class_='rankings-block__banner--name'):
        players.append(player.text.strip())

    for team in soup.find_all('div', class_='rankings-block__banner--nationality'):
        teams.append(team.text.strip())

    for rating in soup.find_all('div', class_='rankings-block__banner--rating'):
        ratings.append(rating.text.strip())

    for player in soup.find_all('td', class_='table-body__cell name'):
        players.append(player.a.text.strip())

    for team in soup.find_all('span', class_='table-body__logo-text'):
        teams.append(team.text.strip())

    for rating in soup.find_all('td', class_='table-body__cell u-text-right rating'):
        ratings.append(rating.text.strip())

    # Creating a DataFrame
    df = pd.DataFrame({
        'Player': players[:10],
        'Team': teams[:10],
        'Rating': ratings[:10]
    })

    return df

#Function for Boller's ranking.
def scrape_odi_bowlers_rankings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting data for ODI bowlers
    players = []
    teams = []
    ratings = []

    for player in soup.find_all('div', class_='rankings-block__banner--name'):
        players.append(player.text.strip())

    for team in soup.find_all('div', class_='rankings-block__banner--nationality'):
        teams.append(team.text.strip())

    for rating in soup.find_all('div', class_='rankings-block__banner--rating'):
        ratings.append(rating.text.strip())

    for player in soup.find_all('td', class_='table-body__cell name'):
        players.append(player.a.text.strip())

    for team in soup.find_all('span', class_='table-body__logo-text'):
        teams.append(team.text.strip())

    for rating in soup.find_all('td', class_='table-body__cell u-text-right rating'):
        ratings.append(rating.text.strip())

    # Creating a DataFrame
    df = pd.DataFrame({
        'Player': players[:10],
        'Team': teams[:10],
        'Rating': ratings[:10]
    })

    return df

# Example for each url
url = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
odi_team_rankings = scrape_odi_team_rankings(url)
print("Top 10 ODI Teams:")
print(odi_team_rankings)

url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting"
odi_batsmen_rankings = scrape_odi_batsmen_rankings(url)
print("\nTop 10 ODI Batsmen:")
print(odi_batsmen_rankings)

url = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
odi_bowlers_rankings = scrape_odi_bowlers_rankings(url)
print("\nTop 10 ODI Bowlers:")
print(odi_bowlers_rankings)

4) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape and make data framea) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
b) Top 10 women’s ODI Batting players along with the records of their team and rating.
c) Top 10 women’s ODI all-rounder along with the records of their team and rating.
# In[24]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_womens_odi_teams(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    teams_data = []
    for team in soup.select('.rankings-block__banner, .table-body'):
        team_name = team.select_one('.u-hide-phablet').text.strip()
        matches = team.select_one('td:nth-child(2)').text.strip()
        points = team.select_one('td:nth-child(3)').text.strip()
        rating = team.select_one('td:nth-child(4)').text.strip()

        teams_data.append({'Team': team_name, 'Matches': matches, 'Points': points, 'Rating': rating})

    df = pd.DataFrame(teams_data[:10])
    return df

def scrape_womens_odi_batting_players(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    players_data = []
    for player in soup.select('.rankings-block__banner, .table-body'):
        player_name = player.select_one('.table-body__cell a').text.strip()
        team = player.select_one('.table-body__cell:nth-child(3)').text.strip()
        rating = player.select_one('.table-body__cell:nth-child(2)').text.strip()

        players_data.append({'Player': player_name, 'Team': team, 'Rating': rating})

    df = pd.DataFrame(players_data[:10])
    return df

def scrape_womens_odi_allrounders(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    allrounders_data = []
    for allrounder in soup.select('.rankings-block__banner, .table-body'):
        allrounder_name = allrounder.select_one('.table-body__cell a').text.strip()
        team = allrounder.select_one('.table-body__cell:nth-child(3)').text.strip()
        rating = allrounder.select_one('.table-body__cell:nth-child(2)').text.strip()

        allrounders_data.append({'Player': allrounder_name, 'Team': team, 'Rating': rating})

    df = pd.DataFrame(allrounders_data[:10])
    return df

#Condition wise three url for dataframes.
url = "https://www.icc-cricket.com/rankings/womens/team-rankings/odi"
df_teams = scrape_womens_odi_teams(url)
print(df_teams)

url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting"
df_batting_players = scrape_womens_odi_batting_players(url)
print(df_batting_players)

url = "https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder"
df_allrounders = scrape_womens_odi_allrounders(url)
print(df_allrounders)

5) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world and
make data framei) Headline
ii) Time
iii) News Link
# In[26]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_cnbc_news(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful or not.
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all news articles on the page
        articles = soup.find_all('div', class_='Card-titleContainer')

        # Lists to store scraped data
        headlines = []
        times = []
        news_links = []

        # Extract information from each article
        for article in articles:
            # Extract headline
            headline = article.find('a').text.strip()
            headlines.append(headline)

            # Extract time if available
            time_element = article.find('time')
            time = time_element['datetime'] if time_element and 'datetime' in time_element.attrs else None
            times.append(time)

            # Extract news link
            news_link = 'https://www.cnbc.com' + article.find('a')['href']
            news_links.append(news_link)

        # Create a DataFrame
        df = pd.DataFrame({
            'Headline': headlines,
            'Time': times,
            'News Link': news_links
        })

        return df

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Example usage:
url = "https://www.cnbc.com/world/?region=world"
result_df = scrape_cnbc_news(url)
print(result_df)

6) Write a python program to scrape the details of most downloaded articles from AI in last 90
days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
Scrape below mentioned details and make data framei) Paper Title
ii) Authors
iii) Published Date
iv) Paper URL
# In[27]:


#Ans:

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_most_downloaded_articles(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful or not?
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Initialize lists to store data
        titles = []
        authors = []
        published_dates = []
        paper_urls = []

        # Find all the article containers on the page
        article_containers = soup.find_all('li', class_='js-list-item')

        # Loop through each article container to extract data
        for article in article_containers:
            # Extract paper title
            title = article.find('a', class_='js-article-title').text.strip()
            titles.append(title)

            # Extract authors
            author_tags = article.find_all('span', class_='author-name')
            author_names = [author.text.strip() for author in author_tags]
            authors.append(', '.join(author_names))

            # Extract published date
            published_date = article.find('span', class_='article-date').text.strip()
            published_dates.append(published_date)

            # Extract paper URL
            paper_url = article.find('a', class_='js-article-title')['href']
            paper_urls.append(paper_url)

        # Create a DataFrame with the collected data
        data = {'Paper Title': titles, 'Authors': authors, 'Published Date': published_dates, 'Paper URL': paper_urls}
        df = pd.DataFrame(data)

        return df

    else:
        # If the request was not successful, print an error message
        print(f"Error: Unable to retrieve data from {url}")
        return None

# Example usage:
url = "https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles"
result_df = scrape_most_downloaded_articles(url)
print(result_df)

7) Write a python program to scrape mentioned details from dineout.co.in and make data frame
i) Restaurant name
ii) Cuisine
iii) Location
iv) Ratings
v) Image URL
# In[32]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_dineout_details(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")
        return None

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Lists to store data
    restaurant_names = []
    cuisines = []
    locations = []
    ratings = []
    image_urls = []

    # Extract data from the HTML
    for restaurant in soup.find_all('div', class_='restaurant-item'):
        # Restaurant Name
        name = restaurant.find('div', class_='restnt-info').h2.text.strip()
        restaurant_names.append(name)

        # Cuisine
        cuisine = restaurant.find('div', class_='restnt-info').find('span', class_='double-line-ellipsis').text.strip()
        cuisines.append(cuisine)

        # Location
        location = restaurant.find('div', class_='restnt-info').find('div', class_='restnt-loc').text.strip()
        locations.append(location)

        # Ratings
        rating = restaurant.find('div', class_='restnt-info').find('div', class_='rating-sec').text.strip()
        ratings.append(rating)

        # Image URL
        image_url = restaurant.find('div', class_='img-sec').img['data-src']
        image_urls.append(image_url)

    # Create a DataFrame
    data = {'Restaurant Name': restaurant_names, 
            'Cuisine': cuisines,
            'Location': locations, 
            'Ratings': ratings, 
            'Image URL': image_urls}
    
    df = pd.DataFrame(data)

    return df

# Example 
url = 'https://www.dineout.co.in/delhi-restaurants'
result_df = scrape_dineout_details(url)
print(result_df)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




