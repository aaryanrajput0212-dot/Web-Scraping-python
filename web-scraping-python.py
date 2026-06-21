import requests
from bs4 import BeautifulSoup


def scrape_quotes():
    url = "https://quotes.toscrape.com/"

    try:
        response = requests.get(url, timeout=10)

        print(f"\nStatus Code: {response.status_code}")

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("div", class_="quote")

        print("\n========== QUOTES ==========\n")

        if not quotes:
            print("No quotes found.")
            return

        for i, quote in enumerate(quotes[:10], start=1):

            text = quote.find("span", class_="text").get_text(strip=True)

            author = quote.find(
                "small",
                class_="author"
            ).get_text(strip=True)

            print(f"{i}. {text}")
            print(f"   - {author}")
            print()

    except Exception as e:
        print("\nError:", e)


while True:

    print("\n===== WEB SCRAPER =====")
    print("1. View Quotes")
    print("2. Exit")

    choice = input("Choose Option: ")

    if choice == "1":
        scrape_quotes()

    elif choice == "2":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice.")