import requests
from datetime import datetime
import time

def get_epoch_time(date_str):
    dt = datetime.strptime(date_str, '%Y/%m/%d')
    return int(time.mktime(dt.timetuple()))

def fetch_data(ticker, from_date, to_date, retries=3, backoff_factor=2):
    from_epoch = get_epoch_time(from_date)
    to_epoch = get_epoch_time(to_date)

    url = (
        f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}"
        f"?period1={from_epoch}&period2={to_epoch}"
        f"&interval=1d&events=history&includeAdjustedClose=true"
    )

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/125.0.0.0 Safari/537.36"
        )
    }

    for attempt in range(1, retries + 1):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content
        elif response.status_code == 429:
            wait = backoff_factor ** attempt
            print(f"Rate limited. Retrying in {wait} seconds...")
            time.sleep(wait)
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            break
    return None

def main():
    ticker = input("Enter the ticker symbol: ").strip().upper()
    from_date = input("Enter start date in yyyy/mm/dd format: ").strip()
    to_date = input("Enter end date in yyyy/mm/dd format: ").strip()

    content = fetch_data(ticker, from_date, to_date)

    if content:
        current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{ticker}_{current_datetime}.csv"
        with open(filename, 'wb') as file:
            file.write(content)
        print(f"Data saved to {filename}")
    else:
        print("Failed to retrieve data.")

if __name__ == "__main__":
    main()
