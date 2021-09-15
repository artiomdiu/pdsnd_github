"""
Created 2021-08-24

The script imports data from three major cities in US (Chicago, New York City and Washington)
and computes descriptive statistics.
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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
    city = ''
    while city not in ('chicago', 'new_york_city', 'washington'):
        city = input(
            'Please type which city statistics whould you like to see (Chicago, New York City or Washington): ').lower().replace(" ", "_")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while month not in (
            'all', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'):
        month = input('Please choose a month (all, january, february, .., december): ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
        day = input('Please choose a day (all, monday, tuesday, ..., sunday): ').lower()

    print('-' * 40)
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
    df = pd.read_csv('{}.csv'.format(city))
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        month_mask = df['Start Time'].dt.month
        df = df[month_mask == month]
        #print('[DEBUG] month: {}'.format(df['Start Time']))

    # filter by day if applicable
    if day != 'all':
        # use the index of the months list to get the corresponding int
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)

        # filter by month to create the new dataframe
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        day_mask = df['Start Time'].dt.dayofweek
        df = df[day_mask == day]
        
    # filter by day of week if applicable
    #if day != 'all':
        # filter by day of week to create the new dataframe
        #df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Convert the Start Time column to datetime format
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['Month'] = df['Start Time'].dt.month
    common_month = df['Month'].mode()[0]
    print('Most common month is ', common_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of week is ', common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour is ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('Most popular start station is ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('Most popular end station is ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_popular_station_combo = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most popular combination of start and end stations is ', most_popular_station_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('Counts of user types:')
    print(user_type_count)
    print('\n')

    # TO DO: Display counts of gender
    while True:
        try:
            gender_count = df['Gender'].value_counts()
            print('Counts of gender:')
            print(gender_count)
            print('\n')
            break
        except:
            break

    # TO DO: Display earliest, most recent, and most common year of birth
    while True:
        try:
            min_birth_year = df['Birth Year'].min()
            max_birth_year = df['Birth Year'].max()
            common_birth_year = df['Birth Year'].mode()[0]
            print('Earliest year of birth is ', min_birth_year)
            print('Most recent year of birth is ', max_birth_year)
            print('Most common year of birth is ', common_birth_year)
            break
        except:
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:(start_loc + 5)])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
