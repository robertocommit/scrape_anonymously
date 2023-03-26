# Tor Web Scraper README

Welcome to Tor Web Scraper! This Python script allows you to anonymously scrape websites using the Tor network and a headless Firefox browser. The script is simple, efficient, and easy to use. Let's take a look at its functionality and how to use it.

## Features
- Anonymity through the Tor network
- Randomized user agents for added stealth
- Headless Firefox browser with Splinter and BeautifulSoup
- Easy IP switching with the Tor control port

## Dependencies
To use this script, you need to install the following Python packages:

- stem
- splinter
- beautifulsoup4

You can install these packages using pip:

```shell
pip install stem splinter beautifulsoup4
```

Additionally, you need to have the following software installed on your system:

- Tor Browser
- Firefox
- GeckoDriver

## How to Use

1. First, download and install the required software and packages mentioned above.
2. Set the path to GeckoDriver by updating the path_geckodriver variable in the script.
3. Set the URL you want to scrape by updating the URL variable at the end of the script.
4. Ensure that Tor Browser is running before running the script. This is necessary for the proxy settings to work correctly.
5. Run the script using python tor_web_scraper.py.

## Code Overview

### main function
The main function takes a URL as an argument and starts the scraping process. It first prints the URL being scraped, then initializes the browser and gets the HTML response. After the browser quits, it waits for a few seconds before returning the response.

### run_browser function
The run_browser function initializes the headless Firefox browser with the appropriate proxy settings, sets a random user agent, and resizes the window. It then prints the current IP address, visits the target URL, and returns the browser instance.

### switch_ip function
The switch_ip function connects to the Tor control port and sends the NEWNYM signal to change the IP address.

### pick_random_user_agent function
This function reads a CSV file containing a list of user agents and selects one at random to be used for the browser.

### print_ip_address function
The print_ip_address function visits the https://api.ipify.org?format=json URL to display the current IP address being used.

## Customization
You can customize the script according to your needs by modifying the existing functions or adding new ones. Feel free to extend its functionality or integrate it into larger projects.

Happy scraping!
