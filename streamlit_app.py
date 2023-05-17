import requests
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


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
            data = fetch(session, f"https://picsum.photos/id/info")
            if data:
                st.write(data['download_url'], caption=f"The user will be able to repay: {data['author']}")
            else:
                st.error("Error")


if __name__ == '__main__':
    main()
