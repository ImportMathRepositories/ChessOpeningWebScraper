# Importing Beautiful Soup and urllib2 for web scraping, random for move selection
import bs4
import urllib2
import random

# Base url for the opening database
BASE_URL = 'https://www.365chess.com'
OPENING = '/opening.php'

# XML and HTML processing library
LXML = 'lxml'

# ID of the div containing the table
SIDEBAR_2 = 'sidebar2'

# HTML tags and keywords
DIV = 'div'
TABLE = 'table'
TR = 'tr'
TD = 'td'
ID = 'id'
HREF = 'href'

# Dictionary keys
MOVE = 'move'
NUMBER = 'number'
URL_SUFFIX = 'url_suffix'

# Name the index given a move
def index_test():
	print('Popularity Test: Name the Index')
	current_position = get_table_from_url(BASE_URL + OPENING)
	in_game = True

	while in_game:
		current_choice = choose_weighted_index(current_position)
		print(current_position[current_choice][MOVE])
		user_choice = input()

		# User input should use 1 indexing
		if current_choice == user_choice - 1:
			print('Correct!')
			current_suffix = current_position[current_choice][URL_SUFFIX]

			if 'javascript' in current_suffix or 'login_page' in current_suffix:
				print('You Win!')
				in_game = False
			else:
				current_position = get_table_from_url(BASE_URL + current_suffix)
		else:
			print('Incorrect! %d was the correct response' % (current_choice + 1))
			print('Game Over!')
			in_game = False

# Name the move given an index
def move_test():
	print('Popularity Test: Name the Move')
	current_position = get_table_from_url(BASE_URL + OPENING)
	in_game = True

	while in_game:
		current_choice = choose_weighted_index(current_position)
		print('Move Choice %d' % (current_choice + 1))
		user_choice = input()

		# Strings must be exactly equal
		if current_position[current_choice][MOVE] == user_choice:
			print('Correct!')
			current_suffix = current_position[current_choice][URL_SUFFIX]

			if 'javascript' in current_suffix or 'login_page' in current_suffix:
				print('You Win!')
				in_game = False
			else:
				current_position = get_table_from_url(BASE_URL + current_suffix)
		else:
			print('Incorrect! %s was the correct response' % current_position[current_choice][MOVE])
			print('Game Over!')
			in_game = False

# Chooses a random move index based on popularity
def choose_weighted_index(move_list):
	total_games = sum(move[NUMBER] for move in move_list)
	game_choice = random.randint(1, total_games)

	for index in range(len(move_list)):
		current_number = move_list[index][NUMBER]
		if game_choice <= current_number:
			return index
		else:
			game_choice -= current_number

	# This line should never be reached. Nonetheless, -1 will index the last move
	return -1

# Returns list of moves given a url string
def get_table_from_url(url):
	move_list = []
	html = urllib2.urlopen(url)
	soup = bs4.BeautifulSoup(html, LXML)
	
	sidebar = soup.find(DIV, {ID: SIDEBAR_2})
	table_list = sidebar.find_all(TABLE)

	# Hardcoding the position table at index 1
	position_table = table_list[1]
	row_list = position_table.find_all(TR)

	# First row at index 2, additional rows at multiples of 4
	for index in range(2, len(row_list), 4):
		move_dict = {}
		current_row = row_list[index]
		column_list = current_row.find_all(TD)

		# Move and href at index 0
		move_and_href = column_list[0].a
		move_dict[MOVE] = move_and_href.getText()
		move_dict[URL_SUFFIX] = move_and_href[HREF]

		# Number of games at index 1 (catch error for singular games)
		games_number = column_list[1].getText()
		try:
			move_dict[NUMBER] = int(games_number)
		except ValueError:
			move_dict[NUMBER] = 1

		move_list.append(move_dict)

	return move_list
