import streamlit as st
import requests


def fetch(session, url):
    try:
        result = session.get(url)
        return result.json()
    except Exception:
        return {}


def mapper(value):
    if value == 'Yes':
        return 1
    elif value == 'No':
        return 0
    elif value == 'Urban':
        return 1
    elif value == 'Semi-urban':
        return 0.5
    elif value == 'Rural':
        return 0


def main():
    st.set_page_config(page_title="Loan Repayment Prediction")
    st.title("Loan Repayment Prediction System")
    session = requests.Session()
    with st.form("my_form"):
        flag_mobil = st.radio("Does the applicant own a mobile?", ('Yes', 'No'), key=1)
        flag_cont_mobile = st.number_input("How many mobiles?", key=21)
        flag_emp_phone = st.radio("Does the applicant\'s employees own phone?", ('Yes', 'No'), key=2)
        region_rating_client_w_city = st.radio("What kind of area do you work in?", ('Urban', 'Semi-urban', 'Rural'),
                                               key=3)
        region_rating_client = st.radio("What kind of area are you from?", ('Urban', 'Semi-urban', 'Rural'), key=4)
        count_fam_mem = st.number_input("How many family members?", key=5)
        flag_own_car = st.radio("Do you own a car?", ('Yes', 'No'), key=6)
        flag_phone = st.radio("Do you own a telephone at home?", ('Yes', 'No'), key=7)
        amt_req_credit_bureau_year = st.number_input(
            "How many times the applicant has applied/enquired for a loan in the last 1 year?", key=8)
        reg_city_not_work_city = st.radio(
            "Is applicant\'s registered city of residence different from their work city?", ('Yes', 'No'), key=9)
        flag_work_phone = st.radio("Do you own a telephone at office?", ('Yes', 'No'), key=10)
        days_employed = st.number_input("How many days have you been employed for?", key=11)
        employment_years = st.number_input("How many years have you worked at the current company?", key=12)
        live_city_not_work_city = st.radio("Do you live in the same city where the office is?", ('Yes', 'No'), key=13)
        cnt_children = st.number_input("How many children do you have?", key=14)
        amt_income_total = st.number_input("What is your total annual income?", key=15)
        obs_30_cnt_social_circle = st.number_input("Number of social connections in last 30 days?", key=16)
        obs_60_cnt_social_circle = st.number_input("Number of social connections in last 60 days?", key=17)
        amt_goods_price = st.number_input("What is the loan amount being requested?", key=18)
        amt_req_credit_bureau_qrt = st.number_input(
            "How many times the applicant has applied/enquired for a loan in the last quarter?", key=19)
        flag_email = st.radio("Do you have an email ID?", ('Yes', 'No'), key=20)

        submitted = st.form_submit_button("Analyze loan re-payability now")

        if submitted:
            st.write("Result")

            flag_mobil = mapper(flag_mobil)
            flag_emp_phone = mapper(flag_emp_phone)
            region_rating_client_w_city = mapper(region_rating_client_w_city)
            region_rating_client = mapper(region_rating_client)
            flag_own_car = mapper(flag_own_car)
            flag_phone = mapper(flag_phone)
            reg_city_not_work_city = mapper(reg_city_not_work_city)
            flag_work_phone = mapper(flag_work_phone)
            live_city_not_work_city = mapper(live_city_not_work_city)
            flag_email = mapper(flag_email)

            api_input = f"http://192.168.1.11:3000/predict?params={flag_mobil} {flag_cont_mobile} {flag_emp_phone} {region_rating_client_w_city} {region_rating_client} {count_fam_mem} {flag_own_car} {flag_phone} {amt_req_credit_bureau_year} {reg_city_not_work_city} {flag_work_phone} {days_employed} {employment_years} {live_city_not_work_city} {cnt_children} {amt_income_total} {obs_30_cnt_social_circle} {obs_60_cnt_social_circle} {amt_goods_price} {amt_req_credit_bureau_qrt} {flag_email}"
            # data = fetch(session,
            #              f"http://192.168.1.11:3000/predict?params={flag_mobil} {flag_cont_mobile} {flag_emp_phone} {region_rating_client_w_city} {region_rating_client} {count_fam_mem} {flag_own_car} {flag_phone} {amt_req_credit_bureau_year} {reg_city_not_work_city} {flag_work_phone} {days_employed} {employment_years} {live_city_not_work_city} {cnt_children} {amt_income_total} {obs_30_cnt_social_circle} {obs_60_cnt_social_circle} {amt_goods_price} {amt_req_credit_bureau_qrt} {flag_email}")

            # new_input = f"http://192.168.1.11:3000/predict?params=0 1 1 1 1 0.052631579 0 0 0.04 0 0 0.005289629 0.005289629 0 0 0.213284583 0.005747126 0.005813953 0.108866442 0 1"
            # print("new input: ", new_input)

            data = fetch(session, api_input)
            if data is None:
                st.error("Server is currently busy.")
            if data:
                st.write("The applicant won\'t be able to repay.")
            else:
                st.write("The applicant shall be able to repay.")


if __name__ == '__main__':
    main()
