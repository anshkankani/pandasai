from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
import pandasai
from pandasai.llm import GoogleGemini
from pandasai import SmartDataframe
import psycopg2
from pandasai.connectors import PostgreSQLConnector
import sqlalchemy

load_dotenv()
API_KEY = os.environ['GEMINI_API_KEY']

llm = GoogleGemini(api_key = API_KEY)

st.title('PANDASAI implementation')
uploaded_file = st.file_uploader('Enter csv file',type=['xlsx','csv'])
if(uploaded_file is not None):
    try:
        df = pd.read_excel(uploaded_file)
    except:
        pass
    try:
        df = pd.read_csv(uploaded_file)
    except:
        pass
    prompt = st.text_area('Enter your query')

    if st.button('Generate'):
        if prompt:
            # st.write('pandasai is generating an answer, please wait...')
            sdf = SmartDataframe(df,config={'llm':llm, 'enforce_privacy':True})
            st.write(sdf.chat(prompt))
            st.write(sdf.last_code_generated)
        else:
            st.warning('please enter a prompt')

            
#to connect to postgres sql
# try:
#     postgres_connector = PostgreSQLConnector(
#          config={
#         "host": "localhost",
#         "port": 5432,
#         "database": "example_db",
#         "username": "postgres",
#         "password": "root",
#         "table": "transactions",
#          }
#     )
#     st.write("Connection established successfully!")
# except Exception as e:
#     st.write("Error connecting to the database:", e)

