
import src.read_config_file as read_config
import src.scraper as scraper

# Get URL address from config.txt file
# In config file are some urls. Insert number in read_config.read_url(<number>)
# 0 - first url
# 1 - second url
Selected_url = read_config.read_url(1)

# Start scraper, using url selected before
scraper.read_url(Selected_url)






















