import time
import pandas as pd
import numpy as np

CITY_DATA   =   { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA  =   { 'january': '1', 'february': '2', 
                'march': '3', 'april': '4', 'may': '5', 'june': '6', 'nf': '0' }

DAY_DATA    =   { 'monday': '1', 'tuesday' :'2', 'wednesday': '3',
                'thursday': '4', 'friday': '5', 'saturday': '6', 'sunday': '7', 'nf': '0' }


def get_filters():
    print('='*70 + '\nHello! Let\'s explore some US bikeshare data!')

    try:
        print('='*70 + '\nData is available for the following cities:\n' + '='*70)
        for cities in CITY_DATA:
            print('>>> ', cities.title())

        while True:    
            city = input('='*70 + '\nPlease enter the name of the city you want to analyze: ').lower()
            
            if city in CITY_DATA:
                break
            else:
                print('\n>>> Your input does not match the given choices! <<<')

        print('='*70 + '\nThe following months are available for evaluation (nf = no filter):\n' + '='*70)
        
        for months in MONTH_DATA:
            print('>>>', months.title())
        
        while True:
            month = input('='*70 + '\nPlease enter the name of the month or "nf" for no filter: ').lower()
            
            if month in MONTH_DATA:
                break
            else:
                print('\n>>> Your input does not match the given choices! <<<')
        
        print('='*70 + '\nThe following days are available for evaluation (nf = no filter):\n' + '='*70)
        for days in DAY_DATA:
            print('>>>', days.title())

        while True:
            day = input('='*70 + '\nPlease enter the name of the day or "nf" for no filter: ').lower()
                    
            if day in DAY_DATA:
                break                    
            else:                                                
                print('\n>>> Your input does not match the given choices! <<<')


    except Exception as e:
            print(e) 
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

    df['month'] = df['Start Time'].dt.strftime('%B')
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')
    df['Hour'] = df['Start Time'].dt.strftime('%I %p')

    #Filter by month if applicable
    if month != 'nf':
        #Filter by month to create the new dataframe
        df = df[df['month'] == month.title()]

    #Filter by day of week if applicable
    if day != 'nf':
        #Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\n\n\n... Calculating The most frequent times of travel\n(filterd by >>> City:', city.title(),'| Month:', month.title(), '| Day: ', day.title(),' <<<)\n')
    start_time = time.time()

    # if no month and day selected print all stats
    if month == 'nf' and day == 'nf':
        print('The most common month is : >>> {} <<<'.format(df['month'].mode()[0]))
        print('The most common day is : >>> {} <<<'.format(df['day_of_week'].mode()[0]))
        print('The most common start hour is : >>> {} <<<'.format(df['Hour'].mode()[0]))

    # if month is selected only print day and hour stats
    elif (month != 'nf') and (day == 'nf'):     
        print('The most common day is : >>> {} <<<'.format(df['day_of_week'].mode()[0]))        
        print('The most common start hour is : >>> {} <<<'.format(df['Hour'].mode()[0]))
                         
    # if no month is selected and day is selected only print mon and hour stats
    elif month == 'nf' and day != 'nf':
        print('The most common month is : >>> {} <<<'.format(df['month'].mode()[0]))
        print('The most common start hour is : >>> {} <<<'.format(df['Hour'].mode()[0]))
        
    # if both month and day is selected only print most common hour
    elif month != 'nf' and day != 'nf':
        print('The most common start hour is : >>> {} <<<'.format(df['Hour'].mode()[0]))      
        
    print('='*70, '\nThis took %s seconds.' % (time.time() - start_time))
    print('='*70)
    input("Press Enter to continue...")
    

def station_stats(df, city, month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\n\n\n... Calculating The Most Popular Stations and Trip\n(filterd by >>> City:', city.title(),'| Month:', month.title(), '| Day: ', day.title(),' <<<)\n')
    start_time = time.time()
    time.sleep(.900)

    # display most commonly used start station
    print('The most common used start station is : >>> {} <<<'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('The most common used end station is : >>> {} <<<'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' <<< and >>> ' + df['End Station']
    print('The most common trip is : >>> {} <<<'.format(df['trip'].mode()[0]))

    print('='*70, '\nThis took %s seconds.' % (time.time() - start_time))
    print('='*70)
    input("Press Enter to continue...")
    

def trip_duration_stats(df, city, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\n\n\n... Calculating Trip Duration\n(filterd by >>> City:', city.title(),'| Month:', month.title(), '| Day: ', day.title(),' <<<)\n')
    start_time = time.time()
    time.sleep(.900)

    # display total travel time
    print('Total travel time : >>> ',(df['Trip Duration'].sum() // 60 ),' <<< minutes') 

    # display mean travel time
    print('mean travel time : >>> ',(df['Trip Duration'].mean() // 60 ),' <<< minutes') 

    print('='*70, '\nThis took %s seconds.' % (time.time() - start_time))
    print('='*70)
    input("Press Enter to continue...")
    

def user_stats(df, city, month, day):
    """Displays statistics on bikeshare users."""

    print('\n\n\n... Calculating User Stats\n(filterd by >>> City:', city.title(),'| Month:', month.title(), '| Day: ', day.title(),' <<<)\n')
    start_time = time.time()
    time.sleep(.900)

    # Display counts of user types
    print(df['User Type'].value_counts().to_frame())

    # Display counts of gender
    if city != 'washington':
        print(df['Gender'].value_counts().to_frame())

    # Display earliest, most recent, and most common year of birth
        print('The most common year of birth is: ',int(df['Birth Year'].mode()[0]))
        print('The most recent year of birth is: ',int(df['Birth Year'].max()))
        print('The most earliest year of birth is: ',int(df['Birth Year'].min()))
    else:
        print('='*70)
        print('\nThere is no more data for city ' + city.title())
      
    print('='*70, '\nThis took %s seconds.' % (time.time() - start_time))
    print('='*70)
    input("Press Enter to continue...")
    

def raw_data(df, city, month, day):
    print('\n\n\nThere are >>> ' + str(len(df)) + ' rows <<< of raw data available.')

    num_row = 5
    num_row_start = 0
    num_row_end = num_row -1

    pd.set_option('display.max_columns',200) #prevents collapsed columns

    print('Do you want to se some raw data from current dataset?')

    while True:
        raw_data = input('>>> yes(y) or no(n) <<<').lower()
        if raw_data == 'yes' or raw_data == 'y':
            print('='*70)
            print('(filterd by >>> City:', city.title(),'| Month:', month.title(), '| Day: ', day.title(),' <<<)')
            print('='*70)
            print('\n >>> Showing rows # {} to {}:'.format(num_row_start + 1, num_row_end + 1))
            print('\n', df.iloc[num_row_start : num_row_end + 1])
            num_row_start += num_row
            num_row_end += num_row
                
            print('\n >>> Do you want so see the next {} rows? <<<'.format(num_row))
            continue

        elif raw_data == 'no' or raw_data == 'n':
            break
        else:
            continue
                
    
def main():
    #while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city, month, day)
        station_stats(df, city, month, day)
        trip_duration_stats(df, city, month, day)
        user_stats(df, city, month, day)
        raw_data(df, city, month, day)

        
        while True:
            restart = input('\nWould you like to restart? Enter yes(y) or no (n). \n').lower()
            if restart not in('y','n','yes','no'):
                print('>>> Enter valid response! <<<') 
            elif restart in ('n','no'):
                print('\n\n\n\n\n\n>>> >>> Good bye and have a nice day! <<< <<<\n\n\n\n\n\n')
                break
            else:
                main()

if __name__ == "__main__":
	main()