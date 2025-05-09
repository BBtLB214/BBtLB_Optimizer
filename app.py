import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "BBtLB_Optimizer")))
import streamlit as st
import gspread
from main import run_full_pipeline  # assuming run_full_pipeline() exists in BBtLB_Optimizer/main.py
import ServiceAccountCredentials
import pandas as pd

st.set_page_config(page_title="BBtLB Fantasy Lineup Generator", layout="wide")
st.title("🧠 Big Bank Take Little Bank (BBtLB)")

# Connect to Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["gcp_service_account"], scope)
client = gspread.authorize(creds)

SHEET_NAME = "Players"
SHEET_URL = st.secrets["gsheets_url"]
sheet = client.open_by_url(SHEET_URL).worksheet(SHEET_NAME)
data = sheet.get_all_records()
df = pd.DataFrame(data)

st.subheader("📊 Player Projections")
st.dataframe(df)

