import requests
from bs4 import BeautifulSoup


def get_details():
	"""
	Connects to the google Blog and retrieves Name, Organization and Country of all GPWs
	:return: a list containing fullname, Organization worked with and the country of the winner.
	"""

	all_details = list()
	html_data = requests.get('https://opensource.googleblog.com/2017/01/announcing-google-code-in-2016-winners.html').text
	soup = BeautifulSoup(html_data, 'html.parser')
	table_elem = soup.find('table')
	all_records = table_elem.find('tbody').findAll('tr')
	for record in all_records:
		print(record)
		clean_records = record.findAll('td')
		details = dict()
		details['full_name'] = ''.join(clean_records[0].findAll(text=True)).strip()
		details['organization'] = ''.join(clean_records[1].findAll(text=True)).strip()
		details['country'] = ''.join(clean_records[2].findAll(text=True)).strip()
		all_details.append(details)

	return all_details

if __name__ == '__main__':
	get_details()
