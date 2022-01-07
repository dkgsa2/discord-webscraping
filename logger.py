# importing module
import logging

def logger(text):
    """
    logging
    :param text:
    :return:
    """
    # Create and configure logger
    logging.basicConfig(filename="autolog.log",
                        format='%(asctime)s %(message)s',
                        filemode='a')

    # Creating an object
    logger = logging.getLogger()

    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    logger.info(text)

