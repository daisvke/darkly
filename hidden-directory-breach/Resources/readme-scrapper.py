import sys
import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def print_file_content(file_url):
	try:
		# Send a GET request to the file URL
		response = requests.get(file_url)
		# Raise an error for bad responses
		response.raise_for_status()
		# Print the content of the file
		print(response.text)

	except Exception as e:
		print(f"An error occurred: {e}")

def scrape_website(root_addr, directory):
	"""
	This function recursively accesses all the links from the webpage
	and open each README file.
	"""
	url = root_addr + directory
	# Send a GET request to the website
	response = requests.get(url)

	# Check if the request was successful (status code 200)
	if response.status_code == 200:
		# Parse the HTML content of the page
		soup = BeautifulSoup(response.content, 'html.parser')

		# Find all links on the page
		links = soup.find_all('a', href=True)

		# Extract and print file and directory URLs
		for link in links:
			href = link['href']
			full_url = urljoin(url, href)
			# We exclude the first link on each page that leads
			# to the previous directory 
			if href != "../":
				# If the link is not a README file we access the link
				# to get the included link set
				if href.lower() != "readme":
					print(full_url)
					scrape_website(url + "/", href)
				else: print_file_content(full_url)
				
if __name__ == "__main__":
    # Check if an IP address is provided as a command-line argument
	if len(sys.argv) != 2:
		print("Usage: ", sys.argv[0], " <IP_ADDR>")
		sys.exit(1)

# Get the IP address from the command-line argument
ip = sys.argv[1]

scrape_website("http://" + ip + "/", ".hidden")
