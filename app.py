mport random
import streamlit as st

st.title("🎮 لعبة تخمين الأرقام")

# تهيئة المتغيرات في ذاكرة المتصفح (Session State)
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 20)
    st.session_state.attempts = 0
    st.session_state.game_over = False

name = st.text_input("ما هو اسمك؟")

if name:
    st.write(f"مرحباً {name}! خمن رقماً بين 1 و 20. لديك 5 محاولات فقط.")

    # خانة إدخال الرقم
    guess = st.number_input(
        "أدخل تخمينك:", min_value=1, max_value=20, step=1, key="guess_input"
    )

    if st.button("تأكيد التخمين") and not st.session_state.game_over:
        st.session_state.attempts += 1

        if guess < st.session_state.number:
            st.warning(
                f"تخمينك منخفض جداً! (المحاولة {st.session_state.attempts}/5)"
            )
        elif guess > st.session_state.number:
            st.warning(
                f"تخمينك مرتفع جداً! (المحاولة {st.session_state.attempts}/5)"
            )
        else:
            st.success(
                f"أحسنت يا {name}! لقد حزرت الرقم الصحيح في {st.session_state.attempts} محاولات! 🎉"
            )
            st.session_state.game_over = True

        if st.session_state.attempts >= 5 and guess != st.session_state.number:
            st.error(f"للأسف انتهت المحاولات! الرقم الصحيح كان: {st.session_state.number}")
            st.session_state.game_over = True

    if st.session_state.game_over:
        if st.button("لعب من جديد 🔄"):
            del st.session_state.number
            del st.session_state.attempts
            del st.session_state.game_over
            st.rerun()