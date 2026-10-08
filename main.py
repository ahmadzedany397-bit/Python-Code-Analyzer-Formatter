import streamlit as st
import black
from radon.complexity import cc_visit

st.set_page_config(page_title="Python Analyzer WebApp",layout="wide")
my_rules = black.Mode()

left_col, right_col = st.columns(2)
with left_col:
    user_code = st.text_area("Write your code here:")
    clean = None
    grade_message = None
    button = st.button("format")
    if button:
        try:
            st.write("formatting")
            clean = black.format_str(user_code, mode=my_rules)
            results = cc_visit(user_code)
            if not results:
                grade_message = "no grade is given since the code has neither Functions nor classes.!"
            else:
                 first_function = results[0]
                 grade_message = f"Your grade is: {first_function.complexity}"
        except black.parsing.InvalidInput:
            st.write("That is not valid Python code!")
with right_col:
    if button and clean is not None:
        st.write("finished formatting")
        st.write(grade_message)
        st.code(clean, language="python")
    else:
            st.code("no code yet", language="python")
    












