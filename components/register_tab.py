import streamlit as st

from models.customer import Customer
from services.formater import INPUT_DATE_FORMAT, DATETIME_DATE_FORMAT
from services.lang_manager import LanguageManager as lm

SCREEN = "REGISTER"


def init_customer(customer=None):
    if "customer" not in st.session_state:
        st.session_state.customer = Customer.create_empty_customer()
    elif customer is None:
        st.session_state.customer = st.session_state.customer
    else:
        st.session_state.customer = customer


def set_user_created(status):
    st.session_state.user_created = status


def clean_session():
    if "user_created" in st.session_state:
        del st.session_state.user_created
    if "customer" in st.session_state:
        del st.session_state.customer


@st.dialog(lm.get_field(SCREEN, "confirm_register_title"), width="large")
def register_confirmation(customer, db):
    st.warning(lm.get_field(SCREEN, "confirm_register_warning"))
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(f"{lm.get_field(SCREEN, "register_fields", "dni")}: {customer.dni}")
        st.text(f"{lm.get_field(SCREEN, "register_fields", "name")}: {customer.name}")
        st.text(f"{lm.get_field(SCREEN, "register_fields", "f_surname")}: {customer.surname1}")
        st.text(f"{lm.get_field(SCREEN, "register_fields", "s_surname")}: {customer.surname2}")
        st.text(f"""{lm.get_field(SCREEN, "register_fields", "birthdate")}: {customer.birthdate.strftime(DATETIME_DATE_FORMAT)}""") # noqa
        st.text(f"{lm.get_field(SCREEN, "register_fields", "phone")}: {customer.phone}")
        st.text(f"{lm.get_field(SCREEN, "register_fields", "email")}: {customer.email}")
    with col2:
        st.text(f"{lm.get_field(SCREEN, "register_fields", "street")}: {customer.street}")
        st.text(f"{lm.get_field(SCREEN, "register_fields", "portal")}: {customer.portal}")
        st.text(f"{lm.get_field(SCREEN, "register_fields", "door")}: {customer.door}")
        st.text(f"{lm.get_field(SCREEN, "register_fields", "city")}: {customer.city}")
        st.text(f"{lm.get_field(SCREEN, "register_fields", "cp")}: {customer.cp}")
    with col3:
        st.text(f"{lm.get_field(SCREEN, "register_fields", "iban")}: {customer.iban}")
        st.text(f"{lm.get_field(SCREEN, "register_fields", "quota")}: {customer.quota}")
        st.text(f"""{lm.get_field(SCREEN, "register_fields", "up_date")}: {customer.register_date.strftime(DATETIME_DATE_FORMAT)}""") # noqa

    but_col1, but_col2, *_ = st.columns([1] * 9)
    with but_col1:
        ok = st.button(f"{lm.get_field(SCREEN, "buttons", "confirm")}")
    with but_col2:
        ko = st.button(f"{lm.get_field(SCREEN, "buttons", "cancel")}")

    if ok:
        result = db.insert_customer(customer)
        set_user_created(result)
        init_customer(Customer.create_empty_customer())
        st.rerun()
    if ko:
        st.rerun()


def register_customer(db):
    st.header("Panel de Registro")
    init_customer()
    with st.form("register_form", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text_input(f"{lm.get_field(SCREEN, "register_fields", "dni")}",
                          key="dni", value=st.session_state.customer.dni)
            st.text_input(f"{lm.get_field(SCREEN, "register_fields", "name")}",
                          key="name", value=st.session_state.customer.name)
            st.text_input(f"{lm.get_field(SCREEN, "register_fields", "f_surname")}",
                          key="f_surname", value=st.session_state.customer.surname1)
            st.text_input(f"{lm.get_field(SCREEN, "register_fields", "s_surname")}",
                          key="s_surname", value=st.session_state.customer.surname2)
            st.date_input(f"{lm.get_field(SCREEN, "register_fields", "birthdate")}", key="birthday",
                          value=st.session_state.customer.birthdate, format=INPUT_DATE_FORMAT)
            st.text_input(f"{lm.get_field(SCREEN, "register_fields", "phone")}",
                          key="phone", value=st.session_state.customer.phone)
            st.text_input(f"{lm.get_field(SCREEN, "register_fields", "email")}",
                          key="email", value=st.session_state.customer.email)
        with col2:
            st.text_input(f"{lm.get_field(SCREEN, "register_fields", "street")}",
                          key="street", value=st.session_state.customer.street)
            st.text_input(f"{lm.get_field(SCREEN, "register_fields", "portal")}",
                          key="portal", value=st.session_state.customer.portal)
            st.text_input(f"{lm.get_field(SCREEN, "register_fields", "door")}",
                          key="door", value=st.session_state.customer.door)
            st.text_input(f"{lm.get_field(SCREEN, "register_fields", "city")}",
                          key="city", value=st.session_state.customer.city)
            st.text_input(f"{lm.get_field(SCREEN, "register_fields", "cp")}",
                          key="cp", value=st.session_state.customer.cp)
        with col3:
            st.text_input(f"{lm.get_field(SCREEN, "register_fields", "iban")}",
                          key="iban", value=st.session_state.customer.iban)
            st.number_input(f"{lm.get_field(SCREEN, "register_fields", "quota")}",
                            key="quota", value=st.session_state.customer.quota)
            st.date_input(f"{lm.get_field(SCREEN, "register_fields", "up_date")}",
                          key="register_date",
                          value=st.session_state.customer.register_date, format=INPUT_DATE_FORMAT)

        submitted = st.form_submit_button(f"{lm.get_field(SCREEN, "buttons", "confirm")}")

        if submitted:
            customer = Customer(dni=st.session_state.dni, name=st.session_state.name,
                                surname1=st.session_state.f_surname, surname2=st.session_state.s_surname,
                                birthdate=st.session_state.birthday, phone=st.session_state.phone,
                                email=st.session_state.email, street=st.session_state.street,
                                portal=st.session_state.portal, door=st.session_state.door,
                                cp=st.session_state.cp, city=st.session_state.city, iban=st.session_state.iban,
                                register_date=st.session_state.register_date, quota=st.session_state.quota, active=True)
            init_customer(customer)
            register_confirmation(customer, db)

        if "user_created" in st.session_state:
            if st.session_state.user_created:
                st.toast(f"{lm.get_field(SCREEN, "toast", "ok")}", icon="✅")
                clean_session()
            elif not st.session_state.user_created:
                st.toast(f"{lm.get_field(SCREEN, "toast", "ko")}", icon="❌")
                if "user_created" in st.session_state:
                    del st.session_state.user_created

    del_button = st.button(f"{lm.get_field(SCREEN, "buttons", "clean_fields")}")

    if del_button:
        clean_session()
        st.rerun()
