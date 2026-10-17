import os  
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

    FILE_NAME = "fitness_activities.csv"

    def __init__(self, name, age):
        super().__init__(name, age)

        self.coulmns = ['Date', 'Steps', 'Calories_burned', 'Distance', 'Activity']

        self.data = pd.DataFrame(columns=self.coulmns)
        self.load_data()


    def load_data(self):
        source = self.FILE_NAME

        if not os.path.exists(source):
            if os.path.exists("fitness_activities.csv"):
                source = "fitness_activities.csv"
            else:
                print("No saved fitness data found.")
                return

            
        try:
            df = pd.read_csv(source)

            aliases = { "date": 'Date', "steps": 'Steps', "calories_burned": 'Calories_burned', "distance": 'Distance', "activity": 'Activity' }
            
            df.columns = [aliases.get(col.lower(), col) for col in df.columns]

            for col in self.coulmns:   
                if col not in df.columns:
                    df[col] = np.nan    

            df["date"] = pd.to_datetime(df["Date"], errors='coerce').dt.strftime('%Y-%m-%d')

            self.data = df

            print(f"Loaded[{len(self.data)}] fitness data from {source}.")

            if source != self.FILE_NAME:
                print("Legacy CSV detected. Missing dates and durations "
                    "cannot be inferred automatically.")

                self.save_data_to_csv()

        except (OSError, pd.errors.ParserError, ValueError) as error:
            print("Error loading data:", error)

    def display_data(self):
        print(f"\nName: {self.name}, Age: {self.age}")
        print("Fitness Data:")
        print(self.data.to_string(index=False))

    def display_all_data(self):
        print("All Fitness Data:")
        print(self.data.to_string(index=False))

    def log_activity(self):
        try:
            date = input("Enter date (YYYY-MM-DD): ").strip()
            parsed_date = pd.to_datetime(date, format="%Y-%m-%d",
                                         errors="raise")

            activity = input("Enter activity type: ").strip()
            if not activity:
                print("Activity type cannot be empty.")
                return

            duration = float(input("Enter duration (minutes): "))
            calories = float(input("Enter calories burned: "))

            if not np.isfinite(duration) or duration <= 0:
                print("Duration must be a positive number.")
                return

            if not np.isfinite(calories) or calories <= 0:
                print("Calories must be a positive number.")
                return

            new_data = pd.DataFrame([{
                "Date": parsed_date.strftime("%Y-%m-%d"),
                "Activity Type": activity,
                "Duration (Minutes)": duration,
                "Calories Burned": calories
            }])

            self.data = pd.concat(
                [self.data, new_data], ignore_index=True
            )

            print("Activity added successfully!")
            self.save_data_to_csv()

        except (ValueError, TypeError):
            print("Invalid input. Check the date and numeric values.")

    def add_data(self):
        self.log_activity()

    def calculate_metrics(self):
        if self.data.empty:
            print("No data to analyze.")
            return

        df = self.data.copy()
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

        duration = pd.to_numeric(
            df["Duration (Minutes)"], errors="coerce"
        )
        calories = pd.to_numeric(
            df["Calories Burned"], errors="coerce"
        )

        valid = duration.notna() & calories.notna()
        duration = duration[valid].to_numpy(dtype=float)
        calories = calories[valid].to_numpy(dtype=float)

        if len(duration) == 0:
            print("No valid duration and calorie records available.")
            return

        print("\nFitness Metrics (NumPy)")
        print("Average Duration:", round(np.mean(duration), 2), "minutes")
        print("Total Duration:", round(np.sum(duration), 2), "minutes")
        print("Average Calories:", round(np.mean(calories), 2))
        print("Total Calories:", round(np.sum(calories), 2))
        print(
            "Average Calories per Minute:",
            round(np.sum(calories) / np.sum(duration), 2)
        )

        daily = df.loc[valid].copy()
        daily["Duration (Minutes)"] = pd.to_numeric(
            daily["Duration (Minutes)"], errors="coerce"
        )
        daily["Calories Burned"] = pd.to_numeric(
            daily["Calories Burned"], errors="coerce"
        )
        daily = daily.dropna(subset=["Date"])
        daily["Date"] = pd.to_datetime(daily["Date"])

        if not daily.empty:
            daily_avg = daily.groupby(daily["Date"].dt.date).agg({
                "Duration (Minutes)": "mean",
                "Calories Burned": "mean"
            })
            print("\nDaily Averages:")
            print(daily_avg)

            daily_totals = daily.groupby(
                daily["Date"].dt.date
            )["Calories Burned"].sum().sort_index()

            if len(daily_totals) >= 2:
                first = daily_totals.iloc[0]
                last = daily_totals.iloc[-1]

                if first != 0:
                    improvement = ((last - first) / abs(first)) * 100
                    print(
                        "Calories percentage improvement:",
                        round(improvement, 2), "%"
                    )
                else:
                    print(
                        "Percentage improvement unavailable: "
                        "first day's calories are zero."
                    )

                growth = daily_totals.pct_change() * 100
                print("\nDaily calorie growth rates (%):")
                print(growth.round(2))

    def analyze_data(self):
        self.calculate_metrics()

    # Pandas analysis
    def analyze_data_pandas(self):
        if self.data.empty:
            print("No data to analyze.")
            return

        print("\nData Analysis using Pandas:")
        print(self.data.describe(include="all"))

        print("\nActivity Summary:")
        print(self.data.groupby("Activity Type", dropna=False).agg({
            "Duration (Minutes)": "sum",
            "Calories Burned": "sum"
        }))

        self.data["Calories per Minute"] = (
            pd.to_numeric(self.data["Calories Burned"], errors="coerce")
            / pd.to_numeric(
                self.data["Duration (Minutes)"], errors="coerce"
            )
        )

        print("\nData with Calories per Minute:")
        print(self.data.to_string(index=False))

    # GroupBy analysis
    def analyze_data_groupby(self):
        if self.data.empty:
            print("No data to analyze.")
            return

        print("\nAnalysis by Activity:")
        print(self.data.groupby("Activity Type", dropna=False).agg({
            "Duration (Minutes)": ["sum", "mean"],
            "Calories Burned": ["sum", "mean"]
        }))

    # Reusable filtering: dictionary or callable condition
    def filter_activities(self, condition):
        df = self.data.copy()

        if callable(condition):
            return df.loc[condition(df)].copy()

        if isinstance(condition, dict):
            for column, value in condition.items():
                if column not in df.columns:
                    raise ValueError(f"Unknown column: {column}")

                if isinstance(value, tuple) and len(value) == 2:
                    low, high = value
                    df = df[
                        pd.to_numeric(df[column], errors="coerce")
                        .between(low, high)
                    ]
                else:
                    df = df[df[column] == value]

            return df

        raise ValueError("Condition must be a dictionary or callable.")

    # Filter records between two dates
    def filter_by_date_range(self):
        try:
            start = pd.to_datetime(
                input("Start date (YYYY-MM-DD): ").strip(),
                format="%Y-%m-%d", errors="raise"
            )
            end = pd.to_datetime(
                input("End date (YYYY-MM-DD): ").strip(),
                format="%Y-%m-%d", errors="raise"
            )

            if start > end:
                print("Start date must not be after end date.")
                return

            dates = pd.to_datetime(self.data["Date"], errors="coerce")
            result = self.data.loc[
                dates.between(start, end)
            ]

            print("\nRecords in selected date range:")
            print(result.to_string(index=False))

        except (ValueError, TypeError):
            print("Invalid date. Use YYYY-MM-DD.")

    # Weekly trend analysis
    def weekly_trend_analysis(self):
        if self.data.empty:
            print("No data to analyze.")
            return

        df = self.data.copy()
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Duration (Minutes)"] = pd.to_numeric(
            df["Duration (Minutes)"], errors="coerce"
        )
        df["Calories Burned"] = pd.to_numeric(
            df["Calories Burned"], errors="coerce"
        )
        df = df.dropna(subset=["Date"])

        if df.empty:
            print("No valid dates available for weekly analysis.")
            return

        df["Week"] = df["Date"].dt.to_period("W").astype(str)
        weekly = df.groupby("Week").agg({
            "Duration (Minutes)": "sum",
            "Calories Burned": "sum"
        })

        print("\nWeekly Fitness Trends:")
        print(weekly)

        weekly.plot(kind="line", marker="o", figsize=(10, 6))
        plt.title("Weekly Duration and Calories Burned")
        plt.xlabel("Week")
        plt.ylabel("Total")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Generate a report
    def generate_report(self):
        if self.data.empty:
            print("No data available for report.")
            return

        print("\n========== FITNESS REPORT ==========")
        print("Total activities:", len(self.data))
        print("\nActivity-wise summary:")

        report = self.data.groupby("Activity Type", dropna=False).agg({
            "Duration (Minutes)": ["sum", "mean"],
            "Calories Burned": ["sum", "mean"]
        })
        print(report)

        print("\nOverall metrics:")
        self.calculate_metrics()

    # Save CSV
    def save_data_to_csv(self, filename=None):
        filename = filename or self.FILE_NAME

        try:
            # Always write the required schema first
            for col in self.columns:
                if col not in self.data.columns:
                    self.data[col] = np.nan

            self.data.to_csv(filename, index=False)
            print(f"Data saved to {filename} successfully!")

        except (OSError, ValueError) as error:
            print("Error saving data:", error)

    # Charts
    def plot_data(self):
        if self.data.empty:
            print("No data to plot.")
            return

        print("\n1. Bar Chart - Duration by Activity")
        print("2. Line Chart - Calories Over Time")
        print("3. Pie Chart - Duration by Activity")
        print("4. Heatmap - Duration and Calories Correlation")

        choice = input("Choose a plot type (1-4): ").strip()

        df = self.data.copy()
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Duration (Minutes)"] = pd.to_numeric(
            df["Duration (Minutes)"], errors="coerce"
        )
        df["Calories Burned"] = pd.to_numeric(
            df["Calories Burned"], errors="coerce"
        )

        if choice == "1":
            grouped = df.groupby("Activity Type")[
                "Duration (Minutes)"
            ].sum().dropna()

            if grouped.empty:
                print("No duration data available.")
                return

            grouped.plot(kind="bar", figsize=(10, 6))
            plt.title("Time Spent on Each Activity")
            plt.xlabel("Activity Type")
            plt.ylabel("Duration (Minutes)")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        elif choice == "2":
            daily = df.dropna(subset=["Date"]).groupby("Date")[
                "Calories Burned"
            ].sum()

            if daily.empty:
                print("No valid date and calorie data available.")
                return

            plt.figure(figsize=(10, 6))
            plt.plot(
                daily.index, daily.values,
                marker="o", label="Calories Burned"
            )
            plt.title("Calories Burned Over Time")
            plt.xlabel("Date")
            plt.ylabel("Calories Burned")
            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        elif choice == "3":
            grouped = df.groupby("Activity Type")[
                "Duration (Minutes)"
            ].sum().dropna()
            grouped = grouped[grouped > 0]

            if grouped.empty:
                print("No positive duration data available.")
                return

            plt.figure(figsize=(8, 8))
            plt.pie(
                grouped, labels=grouped.index,
                autopct="%1.1f%%", startangle=90
            )
            plt.title("Activity Distribution by Duration")
            plt.axis("equal")
            plt.show()

        elif choice == "4":
            numeric = df[[
                "Duration (Minutes)", "Calories Burned"
            ]].dropna()

            if len(numeric) < 2:
                print("At least two valid records are needed.")
                return

            if (numeric.nunique() < 2).any():
                print("Correlation requires variation in both columns.")
                return

            correlation = numeric.corr()

            plt.figure(figsize=(8, 5))
            sns.heatmap(
                correlation, annot=True,
                cmap="coolwarm", linewidths=0.5,
                vmin=-1, vmax=1
            )
            plt.title("Duration and Calories Correlation")
            plt.tight_layout()
            plt.show()

        else:
            print("Invalid choice. Please select 1-4.")


def main():
    tracker = FitnessTracker("Dhara", 18)
    tracker.display_data()

    print("\nWelcome to the Fitness Tracker!")

    while True:
        print("\nMenu:")
        print("1. Add Fitness Data")
        print("2. Display All Fitness Data")
        print("3. Analyze Data (NumPy)")
        print("4. Analyze Data (Pandas)")
        print("5. Analyze Data (GroupBy)")
        print("6. Save Data to CSV")
        print("7. Plot Data")
        print("8. Filter by Date Range")
        print("9. Weekly Trend Analysis")
        print("10.Generate Fitness Report")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":
            tracker.log_activity()
        elif choice == "2":
            tracker.display_all_data()
        elif choice == "3":
            tracker.calculate_metrics()
        elif choice == "4":
            tracker.analyze_data_pandas()
        elif choice == "5":
            tracker.analyze_data_groupby()
        elif choice == "6":
            tracker.save_data_to_csv()
        elif choice == "7":
            tracker.plot_data()
        elif choice == "8":
            tracker.filter_by_date_range()
        elif choice == "9":
            tracker.weekly_trend_analysis()
        elif choice == "10":
            tracker.generate_report()
        elif choice == "11":
            print("Exiting the Fitness Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
