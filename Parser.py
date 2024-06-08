import requests
from bs4 import BeautifulSoup

def get_rbc_news():
    url = "https://www.rbc.ru/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve the web page")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    news_items = []

    # Найдите все блоки с новостями
    for item in soup.find_all("a", class_="news-feed__item"):
        title = item.find("span", class_="news-feed__item__title").get_text(strip=True)
        link = item.get("href")
        news_items.append({"title": title, "link": link})

    return news_items

def filter_news_by_topic(news_items, topic):
    filtered_news = [item for item in news_items if topic.lower() in item["title"].lower()]
    return filtered_news

if __name__ == "__main__":
    topic = input("Enter the topic to filter news: ")

    news_items = get_rbc_news()
    if not news_items:
        print("No news found or failed to retrieve news.")
    else:
        filtered_news = filter_news_by_topic(news_items, topic)
        if filtered_news:
            print(f"News about {topic}:")
            for news in filtered_news:
                print(f"Title: {news['title']}")
                print(f"Link: {news['link']}")
                print()
        else:
            print(f"No news found about {topic}.")
