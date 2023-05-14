import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)


X = load_data(st.secrets["x_res_url"])
y = load_data(st.secrets["y_res_url"])

# Print results.
for row in X.itertuples():
    st.write(f"{row}")

for row in y.itertuples():
    st.write(f"{row}")

y = y['TARGET']

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)
