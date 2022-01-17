import re

def location_format(location):
    choice_regex = '^([a-d]|[A-D])[1-4]$'
    try:
        location = location[0] + location[1]
        
        if(re.search(choice_regex, location)):
            return True
        else:
            return False
    except:
        return False