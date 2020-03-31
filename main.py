from stem import Signal
from stem.control import Controller
from splinter import Browser
import csv
import time
import random
from bs4 import BeautifulSoup


path_geckodriver = 'YOUR_PATH_GECKODRIVER'
proxyIP = "127.0.0.1"
proxyPort = 9150
proxy_settings = {
    "network.proxy.type": 1,
    "network.proxy.socks": proxyIP,
    "network.proxy.socks_port": proxyPort,
    "network.proxy.socks_remote_dns": True,
}


def main(URL):
    print "Scraping " + URL
    browser = run_browser(URL)
    response = browser.html.encode('utf-8')
    browser.quit()
    time.sleep(2)  # Wait few seconds between each request
    return response


def run_browser(url):
    switch_ip()
    browser = Browser(
        'firefox',
        profile_preferences=proxy_settings,
        user_agent=pick_random_user_agent())
    browser.driver.set_window_size(500, 1000)
    browser.driver.set_window_position(0, 0)
    print_ip_address(browser)
    browser.visit(url)
    return browser


def switch_ip():
    with Controller.from_port(port=9151) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)


def pick_random_user_agent():
    with open('user_agents.csv') as file:
        reader = csv.reader(file)
        chosen_row = random.choice(list(reader))
        return chosen_row[0]


def print_ip_address(browser):
    browser.visit('https://api.ipify.org?format=json')
    soup = BeautifulSoup(browser.html.encode('utf-8'), 'html.parser')
    print(soup.find('pre').text)


if __name__ == '__main__':
    URL = 'YOUR_URL'
    RESPONSE = main(URL)
