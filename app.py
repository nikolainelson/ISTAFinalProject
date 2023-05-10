import pandas as pd
import streamlit as st

st.set_page_config(page_title="Types of Workouts", page_icon=":trophy:", layout="wide")

df = pd.read_csv(r'C:\Users\nikol\OneDrive\Documents\megaGym2.csv')
df = df.dropna(subset=['Equipment'])
#df_filled = df['Rating'].fillna(0)
count = 0

body_parts = df['BodyPart'].drop_duplicates()
equipment_s = df['Equipment'].drop_duplicates()
difficulty_level = df['Level'].drop_duplicates()

#----Side bar-----
st.sidebar.header("Please Filter Here:")
BodyPart = st.sidebar.selectbox(
    "Select Part of Body:",
    sorted(body_parts)
    #options=df["BodyPart"].unique(),
    #default=df["BodyPart"].unique()
)

Level = st.sidebar.selectbox(
    "Select Workout Difficulty Level:",
    sorted(difficulty_level)
    #options=df["Level"].unique(),
    #default=df["Level"].unique()
)

Equipment = st.sidebar.selectbox(
    "Select Type of Equipment:",
    sorted(equipment_s)
    #options=df["Equipment"].unique(),
    #default=df["Equipment"].unique()
)

df_selection = df.query("BodyPart == @BodyPart & Level == @Level & Equipment == @Equipment")

#----Main Page-----
st.title(":trophy: Workout Encyclopedia")
st.subheader("Created by Nikolai Nelson")
st.markdown("##")
#image = r'C:\Users\nikol\OneDrive\Desktop\GymPicFinal.png'
#st.image(image)
st.subheader("This application helps users select workouts based on body part, "
             "workout equipment, and difficulty of the exercise.")
st.subheader("Note: Not all workouts have descriptions.")
st.markdown("##")
workouts_available = int(df['Number'].sum())
total_workouts = int(df_selection["Number"].sum())
#avg_rating = (df_selection["Rating"].mean())
#Workout_rating = ":star:" * int(round(avg_rating, 0))

left_column, middle_column = st.columns(2)
with middle_column:
    st.subheader("Total Workouts with Filters:")
    st.subheader(f"{total_workouts:,}")
with left_column:
    st.subheader("Total Available Workouts:")
    st.subheader(f'{workouts_available:,}')

st.markdown("---")

selected_columns = ['Title', 'Desc', 'BodyPart', 'Equipment']
st.dataframe(df_selection[selected_columns].style.set_properties(**{'font-size': '16px'}), width = 1750)

st.markdown("---")

left_column, right_column = st.columns(2)
with left_column:
    st.subheader('Was this information helpful?')
    value = st.slider('Select a Value:', min_value=0, max_value=5, step=1)
    count = count + value
with right_column:
    st.subheader("Average Rating:")
    st.write(value * ':star:')#.style.set_properties(**{'font-size': '20px'})
