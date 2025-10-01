import streamlit as st
import json

st.title("🔑 GCP Service Account JSON Test")

try:
    # Load JSON string from secrets
    service_account_info = json.loads(st.secrets["gcp"]["service_account_json"])

    # Show success message
    st.success("✅ Service account JSON loaded successfully!")

    # Display it for verification (hides private key for safety)
    masked_info = {k: ("*****" if "key" in k else v) for k, v in service_account_info.items()}
    st.json(masked_info)

except KeyError as e:
    st.error(f"❌ Missing key in secrets.toml: {e}")
    st.write("Make sure you added `[gcp]` and `service_account_json` in your secrets.")

except json.JSONDecodeError:
    st.error("❌ The service_account_json is not valid JSON. Please check formatting.")

except Exception as e:
    st.error(f"⚠️ Unexpected error: {e}")
