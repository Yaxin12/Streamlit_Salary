import streamlit as st
import pandas as pd
import altair as alt

# Assuming you have already calculated grouped_data
# and reset the index to create grouped_dataset

df = pd.read_csv("higher_ed_employee_salaries.csv")
#st.dataframe(df)
df = df.dropna() 
#group by years and find the mean
grouped_data = df.groupby(['Year', 'Job Description'])['Earnings'].mean()

# Resetting the index and renaming columns
grouped_df = grouped_data.reset_index()
grouped_df = grouped_df.rename(columns={'Earnings': 'Average Earnings'})

# Sidebar for selecting job description
job_description = st.sidebar.selectbox("Pick your job", grouped_df['Job Description'].unique())

# Filter data by selected job description
filtered_df = grouped_df[grouped_df['Job Description'] == job_description]

# Create Altair chart
mm_chart = alt.Chart(filtered_df).mark_line().encode(
    x='Year',
    y='Average Earnings'
).properties(
    title=f"Average Earnings Over Time for {job_description}"
)

# Display Altair chart
st.altair_chart(mm_chart)
