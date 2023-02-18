
import src.read_config_file as read_config
import src.scraper as scraper

# Get URL address from config.txt file
# In config file are some urls. Insert number in read_config.read_url(<number>)
# 0 - first url is for men jacket
# 1 - second url is for woman jacket
Selected_url = read_config.read_url(0)

# Start scraper, using url selected before
scraper.scrape_web(Selected_url)























