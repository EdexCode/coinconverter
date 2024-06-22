import requests
from bs4 import BeautifulSoup

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def convert(amount, from_currency, to_currency):
    url = f"https://www.google.com/search?q={amount}+{from_currency}+to+{to_currency}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.find("span", class_="DFlfde SwHCTb")
        if result:
            converted_amount = result.text.strip()
            return converted_amount
        else:
            return "Conversion rate not found on the page."

    except requests.exceptions.RequestException as e:
        return f"Error fetching conversion rate: {e}"