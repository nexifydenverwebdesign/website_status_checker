import requests
import time

def check_website_status(urls):
    """Checks the status of a list of websites."""
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            # Check if the status code is 200 (OK)
            if response.status_code == 200:
                print(f"[ONLINE] {url} is up!")
            else:
                print(f"[DOWN] {url} returned status code {response.status_code}")
        except requests.RequestException as e:
            print(f"[DOWN] {url} - Error: {e}")

def main():
    # List of websites to check
    websites = [
        "http://www.google.com",
        "http://www.github.com",
        "http://www.nonexistentwebsite1234.com"
    ]
    
    print("Website Status Checker\n")
    
    while True:
        check_website_status(websites)
        print("\nWaiting for the next check...\n")
        time.sleep(60)  # Wait for 60 seconds before the next check

if __name__ == "__main__":
    main()
