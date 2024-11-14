# Website Status Checker

### Overview
`website-status-checker` is a Python script that allows you to check the status of multiple websites and monitor their uptime. It fetches HTTP status codes from each website, reporting if they are online (status code 200) or down (any other status code). This tool is especially useful for web administrators, developers, or anyone needing to monitor the health and uptime of multiple websites.

The script works by making periodic HTTP requests to a list of websites, checking whether they are accessible, and printing the results in real-time.

---

### Features
- **Multiple Website Checks**: Monitor the status of several websites simultaneously.
- **Status Code Detection**: Identifies successful (HTTP 200) and unsuccessful responses (any other status code).
- **Error Handling**: Handles exceptions like invalid URLs, timeouts, or connection errors gracefully.
- **Automatic Refresh**: Runs in an infinite loop, checking website status periodically (e.g., every 60 seconds).
- **Customizable Website List**: Easily modify the list of websites you want to monitor.
- **Readable Output**: Outputs the status of each website in a clear, readable format.

---

### Installation

Before running the script, ensure you have Python installed on your machine.

1. **Clone the repository** (or download the script):

   ```bash
   git clone https://github.com/yourusername/website-status-checker.git
   cd website-status-checker

    Install the required Python library:

    This script uses the requests library to send HTTP requests. You can install it via pip:

    pip install requests

### Usage

    Download or clone the script to your local machine.

    Open a terminal and navigate to the directory containing the script.

    Run the script using Python:

    python website_status_checker.py

    The script will begin checking the status of the websites listed in the websites list. By default, it checks every 60 seconds.

    Modify the websites list in the script to add or remove the websites you want to monitor.

### How It Works

    Website List: You provide a list of websites to monitor by modifying the websites variable in the script.
    HTTP Requests: The script makes HTTP GET requests to each website using the requests.get() method, with a 10-second timeout.
    Status Code Check: The script checks the HTTP status code:
        If the status code is 200, it prints that the website is online.
        If any other status code is returned, it considers the website down and prints the status code.
        If there is an error (e.g., DNS resolution failed, timeout), it catches the exception and prints an error message.
    Periodic Checks: The script checks the websites in a loop every 60 seconds (or the interval you set).


### Example Output

<p><strong>Website Status Checker</strong></p>
<p><span style="color:green;">[ONLINE]</span> <code>http://www.google.com</code> is up!</p>
<p><span style="color:green;">[ONLINE]</span> <code>http://www.github.com</code> is up!</p>
<p><span style="color:red;">[DOWN]</span> <code>http://www.nonexistentwebsite1234.com</code> - <span style="color:orange;">Error:</span> <span style="color:grey;">HTTPConnectionPool(host='www.nonexistentwebsite1234.com', port=80): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7ffacb374b50>: Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))</span></p>
<p><em>Waiting for the next check...</em></p>

In the example above:

    Online Websites (google.com and github.com) are shown in green.
    Down Website (nonexistentwebsite1234.com) is shown in red and an error message in grey.
    The error message is highlighted in orange for clarity.

### Customizing the Script

    Add More Websites: To monitor more websites, simply add their URLs to the websites list in the main() function:

websites = [
    "http://www.example.com",
    "http://www.someotherwebsite.com"
]

Change the Check Interval: If you want to check websites more or less frequently, adjust the time.sleep(60) value. For example, time.sleep(300) checks every 5 minutes.

Send Notifications: You could extend the script by integrating it with email or SMS APIs (like Twilio for SMS or SMTP for email notifications) to alert you when a website goes down.
