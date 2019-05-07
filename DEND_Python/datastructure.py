list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[-2])
print(list_of_random_things[:3])
print(list_of_random_things[2:])
print(3.4 in list_of_random_things) # wow

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month

num_days = days_in_month[month-1]

print(num_days)

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[7:])
print(eclipse_dates[-3:])