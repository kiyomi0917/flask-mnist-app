import datetime
import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington)
    city = input("Enter a city (Chicago, New York City, Washington): ").lower()
    while city not in CITY_DATA:
        city = input("Invalid city. Please enter a valid city (Chicago, New York City, Washington): ").lower()

    # get user input for month (all, january, february, ... , june)
    month = input("Enter a month (January, February, March, April, May, June, or All): ").title()
    while month not in ['January', 'February', 'March', 'April', 'May', 'June', 'All']:
        month = input("Invalid month. Please enter a valid month (January, February, March, April, May, June, or All): ").title()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter a day of the week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All): ").title()
    while day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']:
        day = input("Invalid day. Please enter a valid day of the week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All): ").title()

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
    # Load dataset for specified city
    filename = CITY_DATA[city]
    df = new_func(filename)

    # Convert "Start Time" column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # Create month and day_of_week columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()

    # Filter by month if applicable
    if month != "All":
        month_num = datetime.datetime.strptime(month, "%B").month
        df = df[df["month"] == month_num]

    # Filter by day of week if applicable
    if day != "All":
        df = df[df["day_of_week"] == day]

    return df

def new_func(filename):
    return pd.read_csv(filename)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month
    common_month = df['Start Time'].dt.month.mode()[0]
    print('The most common month is:', common_month)

    # display the most common day of week
    common_day = df['Start Time'].dt.day_name().mode()[0]
    print('The most common day of the week is:', common_day)

    # display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is:', common_hour)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station is:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station is:', common_end_station)

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].value_counts().idxmax()
    print('The most frequent combination of start station and end station trip is:', common_trip)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""


    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
	trip_durations = [10, 20, 30, 40, 50]
	average_trip_duration = statistics.mean(trip_durations)

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""


    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n", user_types)



    # Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("Counts of gender:\n", gender_counts)
    else:
        print("Gender information is not available for this dataset.")



    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print("Earliest birth year:", earliest_birth_year)
        print("Most recent birth year:", most_recent_birth_year)
        print("Most common birth year:", most_common_birth_year)
    else:
        print("Birth year information is not available for this.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        # Prompt user if they would like to see raw data
        start_row = 0
        end_row = 5
        while True:
            raw_data = input('\nWould you like to see raw data? Enter yes or no.\n')
            if raw_data.lower() != 'yes':
                break
            print(df.iloc[start_row:end_row])
            start_row += 5
            end_row += 5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()