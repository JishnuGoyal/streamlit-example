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
        flag_mobil = st.radio("Does the applicant own a mobile?", ('Yes', 'No'))
        flag_cont_mobile = st.number_input("How many mobiles?")
        flag_emp_phone = st.radio("Does the applicant\'s employees own phone?", ('Yes', 'No'))
        flag_mobil = st.radio("Does the applicant own a mobile?", ('Yes', 'No'))
        flag_mobil = st.radio("Does the applicant own a mobile?", ('Yes', 'No'))

        submitted = st.form_submit_button("Submit")

        if submitted:
            st.write("Result")
            data = fetch(session, f"https://picsum.photos/id/{index}/info")
            if data:
                st.write(data['download_url'], caption=f"The user will be able to repay: {data['author']}")
            else:
                st.error("Error")


if __name__ == '__main__':
    main()