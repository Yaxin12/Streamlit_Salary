import streamlit as st
import pandas as pd
import altair as alt


st.title('Higher Education Employee Salaries')
st.write('Pick a job description on the left pane to view the average salary of that role over time')

st.write(f'<span style="font-size: x-small;">Mugilan Thiayagrajan was here!!!</span>', unsafe_allow_html=True)
#st.write('Mugilan Thiayagrajan was here!!!')


# Add the caching decorator
@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

# Load the data CSV file
salary = load_data("data/higher_ed_employee_salaries.csv")


#st.dataframe(df)
#df.drop.null()
#group by years and find the mean
grouped_data = salary.groupby(['Year', 'Job Description'])['Earnings'].mean()

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
st.altair_chart(mm_chart, use_container_width=True)
