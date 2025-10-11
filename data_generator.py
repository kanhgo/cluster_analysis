import pandas as pd
import numpy as np
import random

# N.B. The random module is a built-in part of the Python standard library.
# And does not need to me listed in requirements for installation


def generate_synthetic_transit_data(num_entries=500):
    """
    Generates synthetic public transit trip data with 500 entries
    intentionally structured around three key usage clusters:

    1. Morning Commute (High duration, early time)
    2. Mid-day Errands (Short duration, mid-day time)
    3. Late Night Transit (Medium duration, late time)

    Args:
        num_entries (int): The total number of trip records to generate.

    Returns:
        pd.DataFrame: A DataFrame containing the synthetic trip data.
    """

    data = []

    # Define a rough distribution for the three clusters
    # This ensures the model has distinct groups to find
    cluster_sizes = np.random.multinomial(num_entries, [0.45, 0.35, 0.20])

    # ------------------------------------------------------------------
    # Cluster 1: Morning Commute (e.g., 7:00 AM - 9:00 AM)
    # ------------------------------------------------------------------
    for _ in range(cluster_sizes[0]):
        # Time of Day (in minutes past midnight): roughly 7:00 AM to 9:00 AM
        time_minutes = random.randint(420, 540)
        # Day of Week: heavily weighted toward Weekdays (1-5)
        day_of_week = random.choice([1, 2, 3, 4, 5, 5])
        # Distance (km) and Duration (seconds): longer, typical commute
        distance = random.uniform(8.0, 20.0)
        duration = random.randint(1800, 3600)  # 30 mins to 1 hour
        # Stops: Fewer stops relative to distance (express route)
        stops = random.randint(3, 10)

        data.append([time_minutes, day_of_week, distance, duration, stops])

    # ------------------------------------------------------------------
    # Cluster 2: Mid-day Errands (e.g., 11:00 AM - 3:00 PM)
    # ------------------------------------------------------------------
    for _ in range(cluster_sizes[1]):
        # Time of Day: roughly 11:00 AM to 3:00 PM
        time_minutes = random.randint(660, 900)
        # Day of Week: more balanced, but still mostly weekdays
        day_of_week = random.choice([1, 2, 3, 4, 5, 6, 7])
        # Distance and Duration: short, local trips
        distance = random.uniform(1.5, 7.0)
        duration = random.randint(600, 1500)  # 10 to 25 mins
        # Stops: higher density of stops relative to distance
        stops = random.randint(5, 12)

        data.append([time_minutes, day_of_week, distance, duration, stops])

    # ------------------------------------------------------------------
    # Cluster 3: Late Night Transit (e.g., 9:00 PM - 1:00 AM)
    # ------------------------------------------------------------------
    for _ in range(cluster_sizes[2]):
        # Time of Day: Late evening/early morning (e.g., 9 PM to 1 AM)
        time_minutes = random.choice(list(range(1260, 1440)) + list(range(0, 60)))
        # Day of Week: higher weekend weight
        day_of_week = random.choice([5, 6, 7, 7])
        # Distance and Duration: medium length, slower service
        distance = random.uniform(5.0, 12.0)
        duration = random.randint(2400, 4800)  # 40 mins to 1 hour 20 mins
        # Stops: wide range due to less frequency
        stops = random.randint(4, 15)

        data.append([time_minutes, day_of_week, distance, duration, stops])

    # Create the DataFrame
    df = pd.DataFrame(
        data,
        columns=[
            "Time_of_Day_Minutes",
            "Day_of_Week",
            "Distance_KM",
            "Trip_Duration_Sec",
            "Num_Stops",
        ],
    )

    # Add a unique Trip ID
    df["Trip_ID"] = [f"T{i+1:04d}" for i in range(len(df))]
    # The f-string specifies starting with T followed by a number based on the row number.
    # The formatting instructions (right of colon) ensure 4 characters (digits), 
    # with any unused space padded with the character zero (0) 

    # Shuffle the rows so the clusters are mixed up and not sequential
    df = df.sample(frac=1).reset_index(drop=True)
    # sample method returns a random sample of rows (or columns) from a DataFrame.
    # with the fraction argument set to 1, you are telling the method to select all rows (100% fraction)

    return df


if __name__ == "__main__":
    transit_df = generate_synthetic_transit_data(num_entries=500)
    print(transit_df.head(10))
    print(f"\nSuccessfully generated {len(transit_df)} trip records.")

    # You can save this file for easy use in your K-Means analysis
    transit_df.to_csv("synthetic_transit_data.csv", index=False)

# The if __name__ == "__main__": defines the entry point of the script and prevents the code from running 
# automatically when the file is imported elsewhere. 
# For example, in another .py file, if I use "import data_generator", I then have to call the function directly
# df = data_generator.generate_synthetic_transit_data(num_entries=300).
# This occurs because in this .py file, __name__ == "data_generator" and not __main_ as occurs when working locally (in terminal)