import requests
from bs4 import BeautifulSoup

url = input("Enter the link of the CNN news: ")

def get_html_content(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Referer": "https://www.cnn.com/",
    "Accept-Language": "en-US,en;q=0.5"
}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page: {response.status_code}")
        return None

def parse_article(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    title = soup.find('h1').get_text() if soup.find('h1') else 'No title found'

    article_content = soup.find_all('p')
    article_text = '\n\n'.join([
    p.get_text().lstrip() if p.get_text().startswith(' ') else p.get_text() 
    for p in article_content])

    return title, article_text

def save_to_file(title, article_text):
    with open('text.txt', 'w', encoding='utf-8') as file:
        file.write(f"Title: {title}\n\n{article_text}")


html_content = get_html_content(url)
if html_content:
    title, article_text = parse_article(html_content)
    print(f"Title: {title}\n")
    print(article_text)
    
    save_to_file(title, article_text)
    print("\nArticle saved to text.txt")