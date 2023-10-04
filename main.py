import requests
from bs4 import BeautifulSoup
import os
import textwrap
import sys
import wikipedia

# Check if the user provided enough command-line arguments
if len(sys.argv) < 3:
    print("Usage: python main.py <site> <query>\nExample: python main.py wikipedia pwd")
    sys.exit(1)

site = str(sys.argv[1])
query = str(sys.argv[2])
print("Want to know about the command: " + query)
print("Fetching information for the command " + query + " from " + site + ".")

if site == "wikipedia" or site == "wiki":
    try:
        result = wikipedia.summary(f"'{query}' linux command", sentences=7)
        print(result)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"DisambiguationError: {e}")
    except wikipedia.exceptions.PageError as e:
        print(f"PageError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("Invalid site. Please use 'wikipedia' or 'wiki' as the site.")
