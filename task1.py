import streamlit as st
import pandas as pd
import numpy as np

def generate_synthetic_data(num_people):
    # Generate synthetic data
    genders = ['male', 'female']
    ages = np.random.randint(18, 60, num_people)
    shirt_colors = np.random.choice(['blue', 'white','black','yellow','orange','pink','purple','green', 'red'], num_people)

    # Create DataFrame
    data = {
        'gender': np.random.choice(genders, num_people),
        'age': ages,
        'shirt_color': shirt_colors
    }

    return pd.DataFrame(data)

def apply_rules(df):
    # Apply rules for age based on shirt color
    df.loc[df['shirt_color'] == 'white', 'age'] = 23
    df.loc[df['shirt_color'] == 'black', 'age'] = 'child'
    return df

def detect_people_features(df):
    # Check if there are at least 2 people in the meeting
    if len(df) < 2:
        st.write("Not enough people in the meeting")
        return
    
    # Count the number of males and females
    male_count = len(df[df['gender'] == 'male'])
    female_count = len(df[df['gender'] == 'female'])

    # Display number of males and females in the meeting
    st.write("Number of males in the meeting:", male_count)
    st.write("Number of females in the meeting:", female_count)

    # Display ages of individuals in the meeting
    st.write("Ages of individuals in the meeting:")
    st.write(df[['gender', 'age']])

# Main Streamlit app code
def main():
    st.title("MEETING ROOM FEATURE DETECTION")
    
    # Generate synthetic data
    num_people = st.slider("Number of people in the meeting", min_value=1, max_value=200, value=10)
    df = generate_synthetic_data(num_people)
    
    # Apply rules based on shirt color
    df = apply_rules(df)
    
    # Detect people features and display results
    detect_people_features(df)

if __name__ == "__main__":
    main()

#streamlit run task1.py
