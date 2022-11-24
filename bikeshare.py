import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
CITIES = list(CITY_DATA.keys())
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input('Which city do you interested in? Please choose from: Chicago, New York city, or Washington.\n').lower())
        if city in CITIES:
            print(f'You chose {city}.')
            break
        else:
            print(f'The answer is wromg, {city} is not in the list of cities, sorry. Try once again.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = str(input('Please provide the name of a month: January, February, March, April, May, June, or all.\n').lower())
        if month in MONTHS:
            print(f'You chose {month}.')
            break
        else:
            print(f'The answer is wrong, {month} is not listed above, sorry. Try once again.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = str(input('Please provide the name of a day: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all.\n').lower())
        if day in DAYS:
            print(f'You chose {day}.')
            break
        else:
            print(f'The answer is wrong, {day} is not listed above, sorry. Try once again.')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.strftime('%A')
    
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != "all":
        df = df[df['day'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    frequent_month = df['month'].mode()[0]
    print("Most frequent month:", frequent_month)

    # TO DO: display the most common day of week
    frequent_day_of_week = df['day'].mode()[0]
    print("Most frequent day:", frequent_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    frequent_start_hour = df['hour'].mode()[0]
    print("Most frequent hour:", frequent_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most popular station to start the trip is:", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most popular station to end the trip is:", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = df['Start Station'] + 'to' + df['End Station']
    print(f'The most frequent combination of start and end stations is: {frequent_combination.mode()[0]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The mean travel time is: ", mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print(f"The earliest year of birth is:{df['Birth Year'].min()}")
        print(f"The most recent year of birth is:{df['Birth Year'].max()}")
        print(f"The most common year of birth is:{df['Birth Year'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    raw_data_review = input('Would you like to see 5 rows of raw data, please answer: yes or no.').lower()
    i = 0
    
    while True:
        print(df.iloc[i:i+5,:])
        i += 5
        
        raw_data_review_continue = input('Would you like to see 5 more rows, please answer: yes or no.').lower()
        if raw_data_review_continue == 'yes':
            print(df.iloc[i:i+5,:])
        else:
            print("\nThe review is finished")
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
