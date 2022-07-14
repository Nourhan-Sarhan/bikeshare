import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv','Chicago':'chicago.csv',
              'new york city': 'new_york_city.csv','New york city':'new_york_city.csv',
              'washington': 'washington.csv','Washington':'washington.csv' }

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

    #Define the variable that used for the city the user will input it
    city = input("Please choose your city name: \n[ Chicago, New York City or Washington ] ").lower() 
    
    #use while loop to ensure the valid inputs from user 
    while city not in CITY_DATA.keys():
            print("\nPlease check your input again")
            print("Restarting... Please enter your city name in a correct formate")
            city = input("[ Chicago, New York City or Washington ] ").lower()
            
    print("\nVery Good... your choise is {} as your city name.\n".format(city.title()))
    # TO DO: get user input for month (all, january, february, ... , june)
    # get user input for month (all, january, february,march,april ... , june)
    # create a dictionary to store month and define the variable that will used for the selected month 
    MONTHS_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    
    month = input("Please enter the month from: \n[ January, February, March, April, May, June, or All ] ").lower()
    
    #use while loop to ensure the correct inputs from user
    while month not in MONTHS_DATA.keys():
        print("\nInvalid input. Please try again in the accepted input format.")
        print("Restarting... Please enter the correct month")
        #print("\nYou have chosen {month.title()} as your month.")
        month = input("[ January, February, March, April, May, June, or All ] ").lower()
            
    print("\nVery Good.. your choise is {} as your month.\n".format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # get user input for day of week (all, tuesday, monday, sunday...friday )
    # create a dictionary to store data about day and define the variable that will used for the selected day
    DAYS_DATA = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7, 'all': 8}
    day = input("Please enter the day from: \n[ Monday, Tuesday', Wednesday, Thursday, Friday, Saturday, Sunday, or All ] ").lower()
    
    #use while loop to ensure the correct inputs from user
    while day not in DAYS_DATA:
        print("\nPlease enter a day in the week of your choice for which you're seeking the data:")
       # print("\nGreet Accepted input:\nDay name; not case sensitive (e.g. monday or MONDAY).\nDay name in title case (e.g. Monday).")
        print("\n(to view all the data for all days in a week You can also input 'all' or 'All' .)")
        print("Restarting... Please enter the day")
        day = input(" [ Monday, Tuesday', Wednesday, Thursday, Friday, Saturday, Sunday, or All ] ").lower()
    
    print("\nVery Good.. your choise is {} as your day.\n".format(day.title()))

    print('*'*50)
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("the Most Common Month in all Months is: {}".format(common_month))


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("the Most common day in all days is: {}".format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    
    common_hour = df['hour'].mode()[0]
    print("the Most common hour is : {}".format(common_hour))
    
    #Prints the time taken to perform the calculation..You will find this in all the functions involving any calculation throughout this    program
    
    print("\nThis took %s seconds." % (time.time() - start_time))
   
    print('*'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Most commonly used start station is: {}".format(common_start_station))


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("Most commonly used end station is: {}".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
     #Uses str.cat to combine two columns in the df.. and Assigns the result to a new column 'frequent station'
    #Uses mode function on this new column to find out the most frequent combination
    #of start station and end estation trip
    df['frequent station'] = df['Start Station'] .str.cat (df['End Station'])
    frequent_station = df['frequent station'].mode()[0]
    print("Most commonly frequent_station through the trip is: {}".format(frequent_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*50)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration_time = df['Trip Duration'].sum()
    print("Total travel time = {}".format(total_duration_time))

    # TO DO: display mean travel time
    average_duration_time = df['Trip Duration'].mean()
    print("Mean travel time = {}".format(average_duration_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    #The total users are counted using value_counts method
    #They are then displayed by their types (e.g. Subscriber or Customer)
    user_type = df['User Type'].value_counts()
    print(f"The types of users by number are :\n\n{user_type}")
    # TO DO: Display counts of gender
     #This try clause is implemented to used for display the number of users by Gender..However, not every df may have the Gender column
    try:
        gender = df['Gender'].value_counts()
        print(f"\nThe types of users by gender are :\n\n{gender}")
    except:
        print("\nThere is no 'Gender' column in this file.")

    # TO DO: Display earliest, most recent, and most common year of birth
    #Similarly, this try clause is there to ensure only df containing
    #'Birth Year' column are displayed
   
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")
    except:
        print("There are no birth year details in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('*'*50)

def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
        prompt the user if they want to see 5 lines of raw data of choose  city,
        Display that data if the answer is 'yes',
        Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration,
        Stop the program when the user says 'no' or there is no more raw data to display.
    Args:
        param1 (df): The dataframe you wish to work with.
    Returns:
        None.
    """
    print(df.head())
    print("\nWelcome.. there is more data if you want to see it.")
    #index_user variable is initialized as a tag 
    user_index = 5
    answer = input("If you want to disply more data, please enter: [ yes or no ] ").lower()
    response_data = ['yes', 'no']
    
     #use while loop to ensure the correct inputs from user
    while answer not in response_data:
        print("\nPlease check your input again")
        answer = input("Restarting... If you want to disply more data, please enter: [ yes or no ] ").lower()
         # use if to check the input from user  
    if answer == "yes":  
        while user_index < df.shape[0]:                     # df.shape[0] gives number of row count
            print(df.iloc[user_index:user_index+5])         # use iloc to Locate user index
            answer = input("Again... If you want to disply more data, please enter: [ yes or no ] ").lower()
            user_index += 5
            if answer != "yes":
               print("Finally... we are finished.")
               break
    # answer != 'yes'
    else:
        print("Finally... we are finished.")
        
        
    print('*'*50)
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
