# Extracts a collection of birth dates from the user and determines
# if each individual is at least 21 years of age.
from datetime import date

def main():
    # Date before which a person must have been born to be 21 or older.
    bornBefore = date(1988, 1, 6)

    # Extract birth dates from the user and determine if 21 or older.
    date1 = promptAndExtractDate()
    # print date1
    # print type(date1)
    while date1 is not None :
        if date1 <= bornBefore :
            print( "Is at least 21 years of age: ", str(date1) )
        date1 = promptAndExtractDate()
        
# Prompts for and extracts the Gregorian date components. Returns a
# Date object or None when the user has finished entering dates.
def promptAndExtractDate():
    print( "Enter a birth date." )
    month = int( input("month (0 to quit): ") )
    if month == 0 :
        return None
    else:
        day = int( input("day: ") )
        year = int( input("year: ") )
        return date( year, month, day)
# Call the main routine.
main()
