import streamlit as st
import hmac
from streamlit import session_state


st.set_page_config(page_title='Stock info', layout='centered')

def main():

    def login_form() -> None:
        with st.form('Credentials'):
            st.text_input('Username', placeholder='Your username here', key='username')
            st.text_input('Password', placeholder='Your password here', type='password', key='password')
            st.divider()
            st.form_submit_button('Submit', on_click=password_check)

    def password_check():
        if (st.session_state['username'] in st.secrets['passwords'] and
                hmac.compare_digest(st.session_state['password'], st.secrets.passwords[st.session_state['username']])):
            st.session_state['logged_in'] = True
            del st.session_state['password']
        else:
            st.session_state['logged_in'] = False
            st.error('Login failed. Try again.')

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    def login():
        if st.button('Login', ):
            login_form()

    def logout():
        if st.button('Logout'):
            st.session_state['logged_in'] = False
            st.rerun()

    login = st.Page(login, title='login', icon='🍕')
    logout = st.Page(logout, title='logout', icon='🍜')


    st.header('Financial instrument analysis')

    if session_state['logged_in']:
        st.selectbox('Choose instrument:', ['AAPL', 'MSFT', 'INTC', 'BA'], placeholder='Choose instrument', key='instrument')

    stock_description = st.Page(page='maintenance/stock_description.py', title='Description', icon='🔬')
    stock_history = st.Page(page='maintenance/stock_history.py', title='Stock price history', icon='🧩')
    stock_forecasts = st.Page(page='maintenance/stock_forecasts.py', title='Forecast', icon='♾️')
    stock_update = st.Page(page='presentation/database_operations.py', title='Data update', icon='🎡')
    page_info = st.Page(page='presentation/info_about.py', title='"About this" page', icon='🐣')


    if session_state['logged_in']:
        pg = st.navigation({'Instrument':[stock_description,
                                          stock_history,
                                          stock_forecasts],
                            'Maintenance':[stock_update,
                                           page_info],
                            'Logout':[logout]}
                           )
    else:
        pg = st.navigation([login])

    return pg

app=main()

if __name__ == '__main__':
    app.run()
