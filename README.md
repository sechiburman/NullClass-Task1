# Meeting Room Feature Detection

This project is a Streamlit application that detects and displays the number of males and females in a meeting room, along with their ages, based on synthetic data. It applies specific rules based on the color of shirts worn by individuals.

## Features

- Generate synthetic data for the number of people in a meeting room.
- Apply rules to determine the age of individuals based on the color of their shirts.
- Display the number of males and females in the meeting room.
- Display the ages of individuals in the meeting room.
- Provide a warning if fewer than 2 people are present in the meeting room.

## Requirements

The required Python packages are listed in `requirements.txt`. The packages must be installed in the system to run the source code file (task1.py).

## Running the Application

To run the application, use the following command in the cmd:
streamlit run task1.py

## Detailed Explanation of the Code
1. Generating Synthetic Data:
generate_synthetic_data(num_people): This function generates synthetic data for a specified number of people, including their gender, age, and shirt color.

2. Applying Rules Based on Shirt Color:
apply_rules(df): This function applies rules to the data based on the color of the shirts:
If the shirt color is white, the age is set to 23.
If the shirt color is black, the individual is considered a child.

3. Detecting and Displaying People Features:
detect_people_features(df): This function checks if there are at least 2 people in the meeting room. If not, it displays a warning. Otherwise, it counts and displays the number of males and females and the ages of individuals in the meeting room.

4. Main Streamlit Application:
main(): This function contains the main logic of the Streamlit application. It includes a slider to specify the number of people in the meeting room, generates the synthetic data, applies the rules, and displays the results.

## Usage

1. Slider for Number of People:
Use the slider to select the number of people in the meeting room (minimum 1, maximum 200, default 10).

2. Displaying Results:
The application will display the number of males and females, along with the ages of individuals in the meeting room.

## Example
After running the application, you will see a Streamlit interface with a slider to select the number of people. The application will generate synthetic data and display the results as described above.

## Note
This application is based on synthetic data and rules defined for the purpose of this project. It may not reflect real-world scenarios accurately.
