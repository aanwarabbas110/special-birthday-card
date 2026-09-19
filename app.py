import streamlit as st

# ==============================
# APP SETTINGS
# ==============================

st.set_page_config(
    page_title="Special Birthday Surprise",
    page_icon="🎂",
    layout="centered"
)

# ==============================
# PERSONAL DETAILS
# ==============================

friend_name = "Ali"
photo_path = "birthday_photo.jpg"

# ==============================
# BIRTHDAY WISHES
# ==============================

wish1 = (
    "Tumhari zindagi ka yeh naya saal tumhein tumhare khwabon "
    "aur goals ke aur qareeb le kar aaye. Khud par hamesha "
    "yaqeen rakhna aur kabhi haar mat maanna! ✨"
)

wish2 = (
    "Tumhari zindagi ka har naya din tumhare liye naye mauqay, "
    "kamyabi aur khushiyan lekar aaye. Allah tumhein hamesha "
    "khush aur kamyab rakhe. 🎉"
)

wish3 = (
    "Hamesha mehnat karte raho, seekhte raho aur apne khwabon "
    "ki taraf barhte raho. Tumhare behtareen din abhi aana "
    "baqi hain! ✨"
)

surprise_message = (
    "Tumhari zindagi hamesha khushiyon, kamyabi aur "
    "achay logon se bhari rahe. Apne dreams par yaqeen "
    "rakhna aur hamesha muskurate rehna! 💖✨"
)

# ==============================
# BEAUTIFUL DESIGN
# ==============================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #fff0f6,
        #f3e8ff,
        #e0f2fe
    );
}

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    font-size: 19px;
    margin-bottom: 25px;
}

.wish-box {
    background: white;
    padding: 20px;
    border-radius: 18px;
    margin: 15px 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    font-size: 18px;
    line-height: 1.7;
}

.card {
    background: white;
    padding: 30px;
    border-radius: 30px;
    text-align: center;
    border: 3px solid #ff69b4;
    box-shadow: 0 8px 30px rgba(0,0,0,0.12);
    margin-top: 25px;
}

.card-title {
    font-size: 38px;
    font-weight: 800;
    margin-bottom: 20px;
}

.card-message {
    background: #fff0f6;
    padding: 25px;
    border-radius: 20px;
    margin-top: 25px;
    font-size: 18px;
    line-height: 1.8;
    text-align: left;
}

.surprise {
    background: #ffffff;
    padding: 25px;
    border-radius: 22px;
    margin-top: 20px;
    text-align: center;
    box-shadow: 0 5px 20px rgba(0,0,0,0.10);
    font-size: 20px;
}

.footer {
    text-align: center;
    font-size: 18px;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# TITLE
# ==============================

st.markdown(
    '<div class="main-title">🎂 Special Birthday Surprise 🎉</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">✨ A special surprise created just for you ✨</div>',
    unsafe_allow_html=True
)

st.divider()

# ==============================
# SURPRISE BUTTON
# ==============================

st.subheader("🎁 Your Special Surprise")

if st.button(
    "🎁 Open Your Surprise",
    use_container_width=True
):

    st.balloons()

    st.success("🎉 Surprise Unlocked!")

    st.markdown(
        f"""
        <div class="surprise">

        💌 <b>A Special Message For You</b>

        <br><br>

        {surprise_message}

        <br><br>

        🌟 Always believe in yourself! 🌟

        </div>
        """,
        unsafe_allow_html=True
    )

with open("birthday_music.wav", "rb") as audio_file:
    audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/wav")



# ==============================
# BIRTHDAY WISHES
# ==============================

st.subheader("💌 Birthday Wishes")

st.markdown(
    f'<div class="wish-box">✨ {wish1}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="wish-box">🎉 {wish2}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="wish-box">🥳 {wish3}</div>',
    unsafe_allow_html=True
)

st.divider()

# ==============================
# CREATE BIRTHDAY CARD
# ==============================

if st.button(
    "🎂 Create Birthday Card 🎉",
    use_container_width=True
):

    st.balloons()

    st.success("🎉 Birthday Card Created Successfully!")

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="card-title">

        🎂 Happy Birthday, {friend_name}! 🎉

        </div>
        """,
        unsafe_allow_html=True
    )

    # PHOTO
    st.image(
        photo_path,
        width=350
    )

    # WISHES
    st.markdown(
        f"""
        <div class="card-message">

        ✨ {wish1}

        <br><br>

        🎉 {wish2}

        <br><br>

        🥳 {wish3}

        <br><br>

        <strong>Best Regards,</strong>

        <br>

        <strong>Anwar Ali 🌟</strong>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="footer">

        🎈 Have an Amazing Day! 🎈

        <br><br>

        💖 Keep Smiling & Keep Shining 💖

        <br><br>

        🎉 Enjoy Your Special Day! 🎉

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )