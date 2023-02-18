
# Read URL from configuration file
import re


def read_url(url_number):

    # Open the file and read the contents
    with open('.\config\config.txt', 'r') as file:
        contents = file.read()

    # Define the regular expression pattern for a URL
    pattern = re.compile(r'(https?://\S+)')

    # Find all matches in the text and return them as a list of strings
    matches = re.findall(pattern, contents)

    # Print the matches
    i = 0
    for url in matches:

        if url_number == i:
            return url
        i += 1

