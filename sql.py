import os
import streamlit as st
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0],question])
    print("Response: " + response.text)
    return response.text

def read_sql_query(query,db_name):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = [
    '''
    You are an expert in converting english questions to sql query.
    the SQL database name is "students" and has the following columns - NAME, CLASS, SECTION.
    your code will be passed in a function to execute the query, so dont include anything other than the query in  your code.
    \n\n For example:\n
    Example 1:\n
    How many students are in class 10?\n
    The SQL Query will be something like this
    SELECT COUNT(*) FROM STUDENT WHERE CLASS = 10;
    \n\n
    Example 2:\n
    What are the names of the students in class 10?\n
    The SQL Query will be something like this
    SELECT NAME FROM STUDENT WHERE CLASS = 10;
    \n\n
    also the sql code should not have ``` in begginning and end, it should not have \n at the end, it should just have the sql query.
    '''
]

st.set_page_config(page_title="GemSql", page_icon="🌍")
st.header("GemSql for Sql Query Generator")

question = st.text_input("Enter your query question : ")
submit = st.button("Submit")

if submit:
    response = get_gemini_response(question,prompt)
    st.subheader("Your SQL Query is")
    st.warning(response)
    response = read_sql_query(response,"student.db")
    st.subheader("The results are")
    for row in response:
        st.warning(row)