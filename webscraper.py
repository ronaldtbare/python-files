
import requests
import random
from bs4 import BeautifulSoup
import datetime

random_number =  random.randint(1,99999)
url = "https://pixelford.com/blog"

# had to set user-agent to random number because site was blocking bc too many site hits.
# The user-agent is always passed when a website is accessed. source->network->headers->user-agent
response = requests.get(url, headers = {'user-agent': f'{random_number}'})
html = response.content

soup = BeautifulSoup(html, 'html.parser')
blogs = soup.find_all('article', class_="type-post")

for blog in blogs:
    title = blog.find('a', class_="entry-title-link").get_text()
    
    blog_datetime_string = blog.find('time', class_="entry-time").get('datetime')

    # converts the string to a datetime object
    blog_datetime = datetime.datetime.fromisoformat(blog_datetime_string) 
    pretty_date = blog_datetime.strftime("%b %m, %Y %-I:%M %p") # formats the datetime object
    
    print(f"{pretty_date} - {title}")


# tag_list =[]
# for a_tag in a_tags:
#     print(a_tag.get_text())
#     tag_list.append(a_tag.get_text())


# print(tag_list)

# # Challenge
# # Use map function to create a list of all the title tags

# map_results = list(map(lambda a_tag: a_tag.get_text(), a_tags))
# print()
# print("**** Using map ****")
# print(map_results)
