import streamlit as st
import requests


def fetch(session, url):
    try:
        result = session.get(url)
        return result.json()
    except Exception:
        return {}


def main():
    st.set_page_config(page_title="Loan Repayment Prediction")
    st.title("Loan Repayment Prediction System")
    session = requests.Session()
    with st.form("my_form"):
        flag_mobil = st.radio("Does the applicant own a mobile?", ('Yes', 'No'), key=1)
        flag_cont_mobile = st.number_input("How many mobiles?", key=5)
        flag_emp_phone = st.radio("Does the applicant\'s employees own phone?", ('Yes', 'No'), key=2)
        flag_mobil = st.radio("Does the applicant own a mobile?", ('Yes', 'No'), key=3)
        flag_mobil = st.radio("Does the applicant own a mobile?", ('Yes', 'No'), key=4)

        submitted = st.form_submit_button("Submit")

        if submitted:
            st.write("Result")
            data = fetch(session, f"http://192.168.43.8:3000/predict?params=0 1 1 1 1 0.052631579 0 0 0.04 0 0 0.005289629 0.005289629 0 0 0.213284583 0.005747126 0.005813953 0.108866442 0 1")
            if data:
                st.write(data, caption=f"The user will be able to repay: {data}")
            else:
                st.error("Error")


if __name__ == '__main__':
    main()