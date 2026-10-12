# Prectical-Exam
# 🏃 Fitness Tracker & Activity Analytics

**Track Your Activities | Analyze Your Progress | Build Healthy Habits**

---

## 📌 Introduction

The **Fitness Tracker & Activity Analytics** project is a Python-based application designed to record, manage, analyze, and visualize fitness activity data.

This application allows users to record daily steps, calories burned, distance covered, activity type, and date. It provides meaningful insights through numerical calculations, data analysis, and graphical visualization.

The project combines Object-Oriented Programming (OOP), NumPy, Pandas, Matplotlib, and Seaborn to create a simple fitness data analysis system.

## 🎯 Objectives

- To record and manage daily fitness activities.
- To calculate total and average steps, calories, and distance.
- To analyze fitness data using NumPy and Pandas.
- To group activities and compare their performance.
- To visualize fitness information through different charts.
- To export fitness records into a CSV file.
- To understand abstraction and inheritance in Python.

## ✨ Features

### 📝 1. Fitness Data Management

- Add new fitness activity records.
- Store date, steps, calories burned, distance, and activity type.
- Display personal details and fitness records.
- View all recorded fitness activities.

### 🔢 2. NumPy Analysis

Perform numerical calculations to find:

- Average steps.
- Total steps.
- Average calories burned.
- Total calories burned.
- Average distance covered.
- Total distance covered.

### 🐼 3. Pandas Analysis

- Generate descriptive statistical summaries.
- Calculate total steps, calories, and distance.
- Count the number of records for each activity.
- Organize fitness records in a structured DataFrame.

### 📊 4. GroupBy Analysis

Analyze fitness data by activity type:

- Total steps by activity.
- Total calories burned by activity.
- Total distance covered by activity.

### 📈 5. Data Visualization

The application provides four visualization options:

- **Bar Chart:** Compare steps across activities.
- **Line Chart:** Analyze calories burned over time.
- **Pie Chart:** Display the distribution of recorded activities.
- **Heatmap:** Show correlations between steps, calories burned, and distance.

### 💾 6. CSV File Export

- Save fitness records into a CSV file.
- Enter a custom filename or use the default filename.
- Keep fitness records in a structured format for future use.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| NumPy | Numerical calculations |
| Pandas | Data manipulation and analysis |
| Matplotlib | Data visualization |
| Seaborn | Statistical charts and heatmaps |
| ABC Module | Abstraction using abstract classes |
| CSV | Exporting fitness records |

## 🏗️ OOP Concepts Used

### 1. Abstraction

The `Person` abstract class defines an abstract method that must be implemented by its child class.

### 2. Inheritance

The `FitnessTracker` class inherits properties and methods from the `Person` class.

### 3. Constructor

The constructor initializes personal details and the fitness dataset.

### 4. Method Overriding

The `FitnessTracker` class implements the `display_data()` method defined in the abstract parent class.

### 5. Classes and Objects

The project organizes related functionality into a class and uses an object to manage fitness operations.

## 🔄 Project Workflow

1. Start the Fitness Tracker application.
2. Display the user's personal information.
3. Choose an option from the main menu.
4. Add fitness activity data.
5. View the recorded fitness information.
6. Analyze data using NumPy or Pandas.
7. Group fitness records by activity.
8. Generate charts to understand the data visually.
9. Save the records to a CSV file.
10. Exit the application.

## 📋 Main Menu Options

| Option | Description |
|---|---|
| 1 | Add Fitness Data |
| 2 | Display All Fitness Data |
| 3 | Analyze Data Using NumPy |
| 4 | Analyze Data Using Pandas |
| 5 | Analyze Data Using GroupBy |
| 6 | Save Data to CSV |
| 7 | Plot Data |
| 8 | Exit |

## 🗂️ Dataset Information

The fitness dataset contains the following columns:

| Column Name | Description |
|---|---|
| Date | Date of the fitness activity |
| Steps | Number of steps recorded |
| Calories_burned | Calories burned during the activity |
| Distance | Distance covered in kilometres |
| Activity | Type of activity performed |

## 🚀 Getting Started

### Prerequisites

- Python installed on your computer.
- A code editor such as VS Code or IDLE.
- Basic knowledge of Python programming.

### Required Libraries

- NumPy
- Pandas
- Matplotlib
- Seaborn

### How to Run the Project

1. Save the Python program in a `.py` file.
2. Open the project folder in VS Code or another Python editor.
3. Install the required libraries.
4. Run the Python program.
5. Select an option from the main menu.
6. Enter fitness records and explore the analysis features.

## 💡 Example Use Case

A user records daily walking activity by entering the date, number of steps, calories burned, distance covered, and activity type.

The application can calculate total and average steps, summarize calories burned, compare activity types, and display the results through charts.

## 📚 What I Learned

Through this project, I learned and practised:

- Python classes and objects.
- Abstraction and inheritance.
- Abstract methods and method overriding.
- NumPy arrays and numerical calculations.
- Pandas DataFrames and descriptive statistics.
- GroupBy operations for activity-based analysis.
- Data visualization using Matplotlib and Seaborn.
- Creating bar charts, line charts, pie charts, and heatmaps.
- Exporting data to CSV files.
- Developing a menu-driven Python application.

## 🔮 Future Improvements

- Automatically load previously saved fitness data.
- Add input validation for dates and numerical values.
- Generate weekly and monthly fitness reports.
- Add daily step and distance goals.
- Create an interactive dashboard.
- Support multiple users and their fitness records.

## ⚠️ Project Notes

- The application starts with an empty fitness dataset.
- Users need to add records before performing analysis or plotting charts.
- The current version exports records to CSV but does not automatically reload them when the application restarts.
- The default personal details can be modified according to the user's requirements.

---

⭐ **Thank you for visiting my Fitness Tracker project!**
