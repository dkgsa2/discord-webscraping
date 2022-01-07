from webhook_basic import basic_webhook
from web_scraping import create_browser, get_page, find_results, list_to_text, is_identical_to_last_result
from logger import logger

def main():
    """
    main function

    :return:
    """
    role = '748634076675833865'

    page = get_page()
    link_list = find_results(page)
    content = list_to_text(link_list, role)
    to_log = is_identical_to_last_result(content)
    logger(to_log)

if __name__ == '__main__':
    main()