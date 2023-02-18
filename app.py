import src.read_config_file as read_config
import src.scraper as scraper
import src.sql as sql
import logging
import datetime

# Configure the logger
logging.basicConfig(filename='.\logs\main.log', level=logging.ERROR)

# Get the current date and time for errors
now = datetime.datetime.now()

jackets_dict = {}

try:

    # In config.txt file are some urls. Insert number in read_config.read_url(<number>)
    # 0 - first url is for men jacket from Audimas shop
    # 1 - second url is for woman jacket Audimas shop
    Selected_url = read_config.read_url(1)

    # Start scraper, using url selected before
    jackets_dict = scraper.scrape_web(Selected_url)

    # Save data from scraper to sql
    sql.send_data_to_sql(jackets_dict)

except EnvironmentError as e:
    # Log the error to the main.log file
    logging.error(f"{str(e)} {now}")

except AttributeError as e:
    # Log the error to the main.log file
    logging.error(f"{str(e)} {now}")

except KeyError as e:
    #Log the error to the main.log file
    logging.error(f"{str(e)} {now}")




























