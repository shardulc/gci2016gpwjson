import requests
import json


def get_details():
	"""
	retrieves completed task list and gci id from the official gci web app api
	:return: list of dictionary mapping completed task number and id with name
	"""

	all_details = list()
	orgs = json.loads(requests.get('https://codein.withgoogle.com/api/program/2016/organization/').text)['results']
	for org in orgs:
		for winner in org['winners']:
			if winner.startswith('winner'):
				details = dict()
				details['completed_tasks'] = org['winners'][winner]['completed_task_instance_count']
				details['full_name'] = org['winners'][winner]['profile']['given_name'] + ' ' + org['winners'][winner]['profile']['other_names']
				details['gci_id'] = org['winners'][winner]['profile']['id']
				all_details.append(details)

	return all_details

if __name__ == '__main__':
	get_details()
