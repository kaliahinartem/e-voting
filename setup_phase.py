from helpers import get_random_in_range
from collections import OrderedDict
import binascii

#creates array with unique tracking numbers for each voter in range
#from min_track to max_track
def create_tracking_numbers(number_of_voters, min_track, max_track):
	tracking_numbers = []

	while len(tracking_numbers) < number_of_voters:
		tracking_numbers.append(int(get_random_in_range(min_track, max_track)))
		tmp = list(OrderedDict.fromkeys(tracking_numbers))
		if tmp != tracking_numbers:
			tracking_numbers = tmp
			continue

	return tracking_numbers

print(create_tracking_numbers(10, 1, 10))