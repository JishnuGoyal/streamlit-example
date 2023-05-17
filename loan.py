import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

col_names = ['FLAG_MOBIL', 'FLAG_CONT_MOBILE', 'FLAG_EMP_PHONE', 'REGION_RATING_CLIENT_W_CITY', 'REGION_RATING_CLIENT',
             'CNT_FAM_MEMBERS', 'FLAG_OWN_CAR', 'FLAG_PHONE', 'AMT_REQ_CREDIT_BUREAU_YEAR', 'REG_CITY_NOT_WORK_CITY',
             'FLAG_WORK_PHONE', 'DAYS_EMPLOYED', 'EMPLOYMENT_YEARS', 'LIVE_CITY_NOT_WORK_CITY', 'CNT_CHILDREN',
             'AMT_INCOME_TOTAL', 'OBS_30_CNT_SOCIAL_CIRCLE', 'OBS_60_CNT_SOCIAL_CIRCLE', 'AMT_GOODS_PRICE',
             'AMT_REQ_CREDIT_BUREAU_QRT', 'FLAG_EMAIL']


# Read in data from the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
def load_data(sheets_url):
    # csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(sheets_url, names=col_names, on_bad_lines='skip')


def main():
    X = load_data(st.secrets["x_res_url"])
    y = load_data(st.secrets["y_res_url"])

    # Print results.
    st.dataframe(X, use_container_width=True)
    st.dataframe(y, use_container_width=True)

    y = y['TARGET']

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)


if __name__ == '__main__':
    main()
