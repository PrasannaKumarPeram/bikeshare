import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('######Hello!There Let\'s see the US bikeshare data######\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while (1):
        city = input("Enter city name you like to explore(chicago,new york city,washington) !!!::").lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("\n*****Invalid input given.Please Check Once!*****\n")
            
            
    # get user input for month (all, january, february, ... , june)
    while (1):    
        month = input("Want details about a particular month? If yes, type month name from within first six months(january, february,                       march,april,may,june) else type 'all':--").lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print("\n*****Invalid input given.Please Check Once!*****\n")
            
            
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while (1):
        day = input("Want details about  a particular day? If yes, type day name(monday,tuesday,wednesday,thursday,friday,saturday,sunday)                  else type 'all'").lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("\n*****Invalid input given.Please Check Once!*****\n")
    return city, month, day
    print("\n\n\n")
    


def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


   
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)
        month +=1
        df = df[df['month'] == month]

    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):

    print('\nThe Most Frequent Time of Travel is...\n')
    start = time.time()

    # display the most common month
    print("Most common month:-", df['month'].mode()[0], "\n")
    # display the most common day of week
    print("Most common day of week:-", df['day_of_week'].mode()[0], "\n")
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("Most common start hour", df['hour'].mode()[0])
    print("\nTrip time is %s seconds." % (time.time() - start))
    print("\n\n\n")


def station_stats(df):
    print('\nThe Most Popular Stations and Trip is...\n')
    start = time.time()

    print("Most commonly used start station :-", df['Start Station'].mode()[0], "\n")

    print("Most commonly used end station :-", df['End Station'].mode()[0], "\n")

    df['combination'] = df['Start Station'] + (" " + df['End Station'])
    print("Most frequent trip from start and end stations is :- ", df['combination'].mode()[0])

    print("\nTrip time is %s seconds" % (time.time() - start))
    print("\n\n\n")


def trip_duration_stats(df):

    print('\nTotal Trip Duration is...\n')
    start = time.time()

    # display total travel time
    print("The total travel time is", df['Trip Duration'].sum(), "\n")

    # display mean travel time
    print("The total mean of travel time is", df['Trip Duration'].mean())

    print("\nTrip time is %s seconds." % (time.time() - start))
    print("\n\n\n")


def user_stats(df, city):

    print('\nFinding User Stats! Wait for a while...\n')
    start = time.time()

    # Display counts of user types
    utypes = df.groupby(['User Type'])['User Type'].count()
    print(utypes, "\n")
    if city != 'washington':
        # Display counts of gender
        gen = df.groupby(['Gender'])['Gender'].count()
        print(gen)
        # Display earliest, most recent, and most common year of birth
        most_recent_yob = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse=True)[0][0]
        early_yob = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        most_common_yob = df['Birth Year'].mode()[0]
        print("Earliest year of birth :- ", early_yob, "\n")
        print("Most recent year of birth :- ", most_recent_yob, "\n")
        print("Most common year of birth :- ", most_common_yob, "\n")

    print("\nThis took %s seconds." % (time.time() - start))
    print("\n\n\n")
                                               
                                               
                                               
    x = 1
    while (x):
        raw = input('\nWant to see more data? Enter \'yes\' or \'no\'.\n')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while (1):
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #calling functions
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        #weather to check for another city or not
        k = input('\nWould you like to See another city? Enter \'yes\' or \'no\'.\n')
        if k.lower() == 'yes':
            pass
        else:
            break


if __name__ == "__main__":
	main()
