import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(
        x ='Year',
        y ='CSIRO Adjusted Sea Level',
        data = df
    )
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    # Create first line of best fit
    result = stats.linregress(x, y) # Using linregress to obtain m1 and c1
    m1 = result.slope
    c1 = result.intercept

    x1 = list(range(1880, 2050)) # Generating x and y values for best fit line 1
    y1 = []
    for year in x1:
        y1.append(c1 + m1*year)
    plt.plot(x1, y1, label='Line of best fit 1')
    

    # Create second line of best fit
    df2 = df.loc[df['Year'] >= 2000] # Extracting smaller data frame to use in 2nd line
    x = df2['Year']
    y = df2['CSIRO Adjusted Sea Level']
    result = stats.linregress(x, y) # Using lineregress to obtain m2 and c2
    m2 = result.slope
    c2 = result.intercept

    x2 = list(range(2000, 2050)) # Generating x and y values for best fit line 2
    y2 =[]
    for year in x2:
        y2.append(c2 + m2*year)
    plt.plot(x2, y2, label='Line of best fit 2')
    


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
