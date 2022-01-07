from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from urllib.parse import urljoin
from webhook_basic import basic_webhook

# URL for epic games store
store_url = "https://www.epicgames.com/store/en-US/"

# previous results file
previous_results = r'Previous_Result.txt'

def create_browser():
    """
    create browser to reliably acquire the page

    :param webdriver_path:
    :return browser:
    """
    # create a selenium object that mimics the browser

    browser_options = Options()
    #service = Service(webdriver_path) --legacy

    # headless tag created an invisible browser
    CHROMEDRIVER_PATH = r'/app/.chromedriver/bin/chromedriver'
    GOOGLE_CHROME_BIN = r'/app/.apt/usr/bin/google-chrome'
    browser_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    browser_options.add_argument("--headless")
    browser_options.add_argument("--disable-dev-shm-usage")
    browser_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    #browser = webdriver.Chrome(service=service, options=browser_options) --legacy
    print("Done Creating Browser")
    return browser


def get_page(webdriver_path):
    """
    getting the page and making it into a soup object

    :param webdriver_path:
    :return page:
    """
    browser = create_browser(webdriver_path)
    browser.get(store_url)
    page = browser.page_source
    browser.close()
    return page

def find_results(page):
    """
    find results from page and return a link list of free games

    :param page: page to search in store
    :return link_list:
    """
    soup = BeautifulSoup(page, "html.parser")
    link_list = []
    substr = "Free Now"
    results = soup.find_all('a', attrs={'aria-label': True, 'href': True})
    for result in results:
        if substr in result['aria-label']:
            link_list.append(urljoin(store_url, result['href']))

    return link_list


def list_to_text(link_list : list, role : str):
    """
    make a text from a list and add the mentioned role

    :param link_list: list, list of links
    :param role: str, role to mention
    :return: text: str, concated text
    """
    if link_list:
        formatted_role = f"<@&{role}>"
        link_list.insert(0,formatted_role)
        text = '\n'.join(map(str, link_list))
        return text


def is_identical_to_last_result(link_text):
    """
    check if the new result is identical to the previous one
    if true do nothing , if false send to discord

    :param link_text:
    :return:
    """
    with open(previous_results,'r+') as pr:
        file_content = pr.read()
    if file_content == link_text:
        to_write = "didnt write"
        print(to_write)
        pass
    else:
        with open(previous_results, 'w+') as pr:
            pr.write(link_text)
            to_write = f"Written:\t{link_text}"
            print(to_write)
            basic_webhook(link_text)
    return to_write




