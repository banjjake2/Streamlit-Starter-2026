import streamlit as st

st.title("🚀 실생활 문제 해결 프로젝트")
st.write("학번과 이름을 입력하고 프로젝트를 시작하세요.")

name = st.text_input("이름")
if name:
    st.success(f"{name}님, 환영합니다! 이제 코드를 수정해 문제를 해결해 보세요.")
