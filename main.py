import blog_details
import gci_api
import trip_details
import json


def main():
	blog_info = blog_details.get_details()
	api_info = gci_api.get_details()
	org_to_trip, name_to_trip = trip_details.get_details()
	winners = list()
	template = json.loads(open('template.json').read())['winners'][0]

	for student in blog_info:
		student_info = template.copy()
		student_info['full_name'] = student['full_name']
		student_info['organization'] = student['organization']
		student_info['country'] = student['country']
		try:
			student_info['trip'] = org_to_trip[student['organization']]
		except KeyError:
			try:
				student_info['trip'] = name_to_trip[student['full_name']]
			except Exception as e:
				print('Error ({}) raised for {}. Incomplete data may be present'.format(e, student['full_name']))
		except Exception as e:
			print('Error ({}) raised for {}. Incomplete data may be present'.format(e, student['full_name']))
		for record in api_info:
			if record['full_name'] == student['full_name']:
				student_info['tasks_completed'] = record['completed_tasks']
				student_info['GCI_ID'] = record['gci_id']
		winners.append(student_info)

	final_json = json.dumps({'winners': winners}, sort_keys=True, indent=4)

	final_json_file = open('winner_data.json', 'w')
	final_json_file.write(final_json)
	final_json_file.close()

if __name__ == '__main__':
	main()
