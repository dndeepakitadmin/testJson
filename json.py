import streamlit as st
import json
from google.oauth2 import service_account
import gspread

st.title("GCP Service Account JSON Test")

# Paste your JSON securely here (better: store it in Streamlit secrets)
service_account_json = st.secrets["gcp"]["service_account_json"]

try:
    # Parse credentials
    credentials_info = json.loads(service_account_json)
    creds = service_account.Credentials.from_service_account_info(credentials_info)
    st.success("✅ JSON is valid and credentials object created")

    # Optional: Test Google Sheets access
    client = gspread.authorize(creds)
    st.info("Trying to list accessible spreadsheets...")

    spreadsheets = client.openall()
    if spreadsheets:
        st.write("Accessible Sheets:")
        for sheet in spreadsheets:
            st.write("-", sheet.title)
    else:
        st.warning("No spreadsheets accessible with this service account.")

except Exception as e:
    st.error(f"❌ Error: {e}")
