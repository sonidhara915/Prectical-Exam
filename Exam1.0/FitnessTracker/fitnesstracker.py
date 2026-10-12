import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @abstractmethod
    def display_data(self):
        pass

class FitnessTracker(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.data = pd.DataFrame(columns=['Date', 'Steps', 'Calories_burned', 'Distance', 'Activity'])

    def display_data(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print("Fitness Data:")
        print(self.data)

    def display_all_data(self):
        print("All Fitness Data:")
        print(self.data)

    def add_data(self):

        date = input("Enter the date (YYYY-MM-DD): ")
        steps = int(input("Enter the number of steps: "))
        calories_burned = float(input("Enter the calories burned: "))
        distance = float(input("Enter the distance covered (in km): "))
        activity = input("Enter the activity: ")

        new_data = pd.DataFrame({
            'Date': [date],
            'Steps': [steps],
            'Calories_burned': [calories_burned],
            'Distance': [distance],
            'Activity': [activity]
        })

        self.data = pd.concat([self.data, new_data], ignore_index=True)
        print("Data added successfully!")


     # numpy analysis
    def analyze_data(self):
        if self.data.empty:
            print("No data to analyze.")
            return

        steps_array = self.data['Steps'].to_numpy()
        calories_array = self.data['Calories_burned'].to_numpy()
        distance_array = self.data['Distance'].to_numpy()

        print(f"Average Steps: {np.mean(steps_array)}")
        print(f"Total Steps: {np.sum(steps_array)}")
        print(f"Average Calories Burned: {np.mean(calories_array)}")
        print(f"Total Calories Burned: {np.sum(calories_array)}")
        print(f"Average Distance: {np.mean(distance_array)} km")
        print(f"Total Distance: {np.sum(distance_array)} km")


    # pandas analysis
    def analyze_data_pandas(self):
        if self.data.empty:
            print("No data to analyze.")
            return

        print("Data Analysis using Pandas:")
        print(self.data.describe())
        print("\nTotal Steps:", self.data['Steps'].sum())
        print("Total Calories Burned:", self.data['Calories_burned'].sum())
        print("Total Distance Covered:", self.data['Distance'].sum(), "km")
        print("Activity Breakdown:")
        print(self.data['Activity'].value_counts())

    # using groupby for analysis
    def analyze_data_groupby(self):
        if self.data.empty:
            print("No data to analyze.")
            return

        grouped_data_steps = self.data.groupby('Activity')["Steps"].sum()
        grouped_data_calories = self.data.groupby('Activity')["Calories_burned"].sum()
        grouped_data_distance = self.data.groupby('Activity')["Distance"].sum()

        print("Data Analysis using GroupBy:")
        print("Total Steps by Activity:")
        print(grouped_data_steps)
        print("\nTotal Calories Burned by Activity:")
        print(grouped_data_calories)
        print("\nTotal Distance by Activity:")
        print(grouped_data_distance)

    # dataframe to csv
    def save_data_to_csv(self, filename):
        if filename is None:
            filename = "fitness_activities.csv"
        self.data.to_csv(filename, index=False)
        print(f"Data saved to {filename} successfully!")

    # matplotlib analysis
    def plot_data(self):
        if self.data.empty:
            print("No data to plot.")
            return

        print("1. Bar Chart")
        print("2. Line Chart")
        print("3. Pie Chart")
        print("4. Heatmap")
        choice = input("Choose a plot type (1-4): ").lower()    
        
        if choice == '1':
      # bar chart
      
            plt.figure(figsize=(10, 6))
            sns.barplot(x='Activity', y='Steps', data=self.data)
            plt.title('Steps by Activity')
            plt.xlabel('Activity')
            plt.ylabel('Steps')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

    # line chart
        elif choice == '2':
            plt.figure(figsize=(10, 6))
            sns.lineplot(x='Date', y='Calories_burned', data=self.data, marker='o')
            plt.title('Calories Burned Over Time') 
            plt.xlabel('Date')
            plt.ylabel('Calories Burned')
            plt.legend()
            plt.show()

    # pie chart
        elif choice == '3':
            activity_counts = self.data['Activity'].value_counts()
            plt.figure(figsize=(8, 8))
            plt.pie(activity_counts, labels=activity_counts.index, autopct='%1.1f%%', startangle=90)
            plt.title('Activity Distribution')
            plt.axis('equal')
            plt.show()

    # heatmap
        elif choice == '4':
            plt.figure(figsize=(10, 6))
            correlation_matrix = self.data[['Steps', 'Calories_burned', 'Distance']].corr()
            sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
            plt.title('Correlation Heatmap')
            plt.show()

        else:
            print("Invalid choice. Please try again.")


def main():
    tracker = FitnessTracker("Dhara", 18)
    tracker.display_data()

    print("Welcome to the Fitness Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add Fitness Data")
        print("2. Display All Fitness Data")
        print("3. Analyze Data (NumPy)")
        print("4. Analyze Data (Pandas)")
        print("5. Analyze Data (GroupBy)")
        print("6. Save Data to CSV")
        print("7. Plot Data")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            tracker.add_data()
        elif choice == '2':
            tracker.display_data()
        elif choice == '3':
            tracker.analyze_data()
        elif choice == '4':
            tracker.analyze_data_pandas()
        elif choice == '5':
            tracker.analyze_data_groupby()
        elif choice == '6':
            filename = input("Enter the filename to save data (default: fitness_activities.csv): ").strip()
            if not filename:
                filename = "fitness_activities.csv"
            tracker.save_data_to_csv(filename)
        elif choice == '7':
            tracker.plot_data()
        elif choice == '8':
            print("Exiting the Fitness Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
