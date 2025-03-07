#UNWSP Programming PythonCos2005DEsp25
#Week#7_Program#1 Rainfall
#03/7/2025
#Abraham. N. Andersen

#Design a program that lets the user enter the total rainfall for each of 12 months into a list.
#The program should calculate and display the total rainfall for the year, the average monthly
#rainfall, and the months with the highest and lowest amounts.

def rainfall_tracker():
    """Tracks rainfall for 12 months, calculating totals, averages, and extremes."""

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    rainfall = []

    # Get rainfall data from the user
    for month in months:
        while True:
            try:
                rain = float(input(f"Enter rainfall for {month} (in inches): "))
                if rain >= 0: #Make sure the input is a positive number.
                    rainfall.append(rain)
                    break #Exit the while loop when the input is valid.
                else:
                    print("Rainfall cannot be a negative number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Calculate total rainfall
    total_rainfall = sum(rainfall)

    # Calculate average monthly rainfall
    average_rainfall = total_rainfall / 12

    # Find the month with the highest rainfall
    highest_rainfall = max(rainfall)
    highest_month_index = rainfall.index(highest_rainfall)
    highest_month = months[highest_month_index]

    # Find the month with the lowest rainfall
    lowest_rainfall = min(rainfall)
    lowest_month_index = rainfall.index(lowest_rainfall)
    lowest_month = months[lowest_month_index]

    # Display the results
    print("\nRainfall Summary:")
    print(f"Total rainfall for the year: {total_rainfall:.2f} inches")
    print(f"Average monthly rainfall: {average_rainfall:.2f} inches")
    print(f"Month with highest rainfall: {highest_month} ({highest_rainfall:.2f} inches)")
    print(f"Month with lowest rainfall: {lowest_month} ({lowest_rainfall:.2f} inches)")

# Run the program
rainfall_tracker()