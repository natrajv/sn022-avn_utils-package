from datetime import datetime

def get_mytimestamp():
	# Get current datetime
	current_time = datetime.now()

	# Format datetime to yyyymmdd_hhmm
	formatted_time = current_time.strftime("%Y%m%d_%H%M")

	return formatted_time

'''
* Example usage:
import avn_utils.core.utils as myutils
print(myutils.get_mytimestamp())
* This will print the current timestamp in the format yyyymmdd_hhmm
'''