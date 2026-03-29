import streamlit as st
from datetime import date

# 1. 페이지 설정
st.set_page_config(page_title="고3 갓생 추적기", page_icon="🔥")
st.title("🎓 2026 대입 성공을 위한 갓생 추적기")

# 2. 사용자 입력 영역
st.info("💡 아래 내용을 수정하여 나만의 목표를 설정해 보세요!")
name = st.text_input("당신의 이름을 입력하세요", placeholder="예: 홍길동")
goal = st.text_input("올해의 최종 목표 대학/학과 또는 다짐", placeholder="예: OO대학교 합격!")

# 3. 수능 디데이 계산 (2026년 수능 예정일 기준)
today = date.today()
exam_day = date(2026, 11, 12) 
d_day = (exam_day - today).days

# 4. 대시보드 레이아웃
col1, col2 = st.columns(2)
with col1:
    st.metric(label="📅 오늘 날짜", value=str(today))
with col2:
    st.metric(label="⚔️ 수능 D-Day", value=f"{d_day}일")

# 5. 인터랙티브 버튼
if st.button("내 목표 선언하기! 🚀"):
    if name and goal:
        st.success(f"[{name}]님의 목표: '{goal}'")
        st.balloons()
    else:
        st.warning("이름과 목표를 모두 입력해 주세요!")

st.divider()
st.caption("이 코드를 수정하여 여러분만의 실생활 문제 해결 프로그램을 만들어 보세요.")
