all_trips = '''
| Deniz Karakay | A | SCoRe |
| August van de Ven | A | SCoRe |
| Scott Moses | A | MovingBlocks |
| Isaac Ong | A | MovingBlocks |
| Oana Roșca | A | FOSSASIA |
| Kaisar Arkhan (Yuki) | A | FOSSASIA |
| Daniel Hsing | A | MetaBrainz |
| Anshuman Agarwal | A | MetaBrainz |
| Cristian Garcia | A | Sugar Labs |
| Tymon Radzik | A | Sugar Labs |
| Dhruv Shrivastava | A | Mifos |
| Sawan Kumar | A | Mifos |
| Jacqueline Bronger | A | Systers |
| Soham Sen | A | Systers |
| Filip Grzywok | A | Wikimedia |
| Justin Du | A | Wikimedia |
| Evgeny Shulgin | B | CCExtractor |
| Alexandru Bratosin | B | CCExtractor |
| Sergey Popov | B | KDE |
| Ilya Bizyaev | B | KDE |
| Sampriti Panda | B | Zulip |
| Tommy Ip | B | Zulip |
| Utkarsh Dixit | B | Drupal |
| Dhanat Satta-awalo | B | Drupal |
| Collin Grimm | B | OpenMRS |
| Mira Yang | B | OpenMRS |
| Joshua Pan | B | Copyleft Games Group |
| Shriank Kanaparti | B | Copyleft Games Group |
| Shardul Chiplunkar | B | Apertium |
| Matthew Marting | B | Apertium |
| Raefaldhi Amartya Junior | B | Haiku |
| Vanisha Kesswani | B | Haiku |
| Michal Hanus | B | BRL-CAD |
| Sudhanshu Agarwal | B | BRL-CAD |
'''


def get_details():
	org_to_trip = dict()
	name_to_trip = dict()
	for details in [x for x in all_trips.split('\n') if x]:
		detail = [y for y in details.strip().split('|') if y]
		org_to_trip[detail[2].strip()] = detail[1].strip()
		name_to_trip[detail[0].strip()] = detail[1].strip()

	return org_to_trip, name_to_trip

if __name__ == '__main__':
	get_details()
