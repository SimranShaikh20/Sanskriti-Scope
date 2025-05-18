import streamlit as st

# ---- Festival Calendar Data ----
festival_calendar = {
    "January": [
        {"festival": "Pongal", "state": "Tamil Nadu", "description": "Harvest festival celebrated with cooking and dances."},
        {"festival": "Lohri", "state": "Punjab", "description": "Bonfire festival marking the end of winter."},
        {"festival": "Makar Sankranti", "state": "Pan India", "description": "Celebration of the sun's movement with kites and sweets."},
        {"festival": "Republic Day", "state": "Delhi", "description": "Parade and cultural showcase at Rajpath."}
    ],
    "February": [
        {"festival": "Shivratri", "state": "Pan India", "description": "Night dedicated to Lord Shiva worship."},
        {"festival": "Taj Mahotsav", "state": "Uttar Pradesh", "description": "Art and craft fair near Taj Mahal."},
        {"festival": "Guru Ravidas Jayanti", "state": "North India", "description": "Celebration of the birth of Guru Ravidas."}
    ],
    "March": [
        {"festival": "Holi", "state": "Pan India", "description": "Festival of colors and joy."},
        {"festival": "Ramzan (start)", "state": "Pan India", "description": "Beginning of the holy month of fasting for Muslims (dates vary)."},
        {"festival": "Easter (if applicable)", "state": "Pan India", "description": "Christian celebration of resurrection of Jesus Christ (date varies)."}
    ],
    "April": [
        {"festival": "Good Friday", "state": "Pan India", "description": "Christian commemoration of Jesus' crucifixion."},
        {"festival": "Baisakhi", "state": "Punjab", "description": "Harvest and Sikh New Year celebration."},
        {"festival": "Mahavir Jayanti", "state": "Pan India", "description": "Jain festival celebrating Lord Mahavir's birth."},
        {"festival": "Ram Navami", "state": "Pan India", "description": "Lord Rama's birth anniversary."}
    ],
    "May": [
        {"festival": "Eid-ul-Fitr", "state": "Pan India", "description": "Muslim celebration marking the end of Ramadan."},
        {"festival": "Buddha Purnima", "state": "Bihar", "description": "Marks Lord Buddha's birth, enlightenment and death."},
        {"festival": "Thrissur Pooram", "state": "Kerala", "description": "Temple festival with decorated elephants and percussion."}
    ],
    "June": [
        {"festival": "Sant Kabir Jayanti", "state": "Uttar Pradesh", "description": "Birth anniversary of saint Kabir Das."},
        {"festival": "Eid-ul-Adha (Bakrid)", "state": "Pan India", "description": "Islamic festival of sacrifice (date varies)."}
    ],
    "July": [
        {"festival": "Guru Purnima", "state": "Pan India", "description": "Day to honor spiritual and academic teachers."},
        {"festival": "Bonalu", "state": "Telangana", "description": "Hindu festival dedicated to Goddess Mahakali."},
        {"festival": "Muharram (start)", "state": "Pan India", "description": "Islamic new year and remembrance of martyrdom of Imam Hussain (date varies)."}
    ],
    "August": [
        {"festival": "Raksha Bandhan", "state": "Pan India", "description": "Celebration of sibling bonds."},
        {"festival": "Janmashtami", "state": "Pan India", "description": "Birthday of Lord Krishna."},
        {"festival": "Independence Day", "state": "Pan India", "description": "Celebration of India’s freedom with flag hoisting and parades."},
        {"festival": "Onam", "state": "Kerala", "description": "Harvest festival celebrated with Pookalam and boat races."},
        {"festival": "Parsi New Year (Navroz)", "state": "Maharashtra, Gujarat", "description": "Zoroastrian celebration of new year."}
    ],
    "September": [
        {"festival": "Ganesh Chaturthi", "state": "Maharashtra", "description": "Welcoming Lord Ganesha with idols and immersion."},
        {"festival": "Anant Chaturdashi", "state": "Pan India", "description": "Conclusion of Ganesh festival."},
        {"festival": "Milad-un-Nabi", "state": "Pan India", "description": "Birthday of Prophet Muhammad (date varies)."}
    ],
    "October": [
        {"festival": "Navratri", "state": "Gujarat", "description": "Nine nights of Garba and worship of Goddess Durga."},
        {"festival": "Durga Puja", "state": "West Bengal", "description": "Five-day worship of Goddess Durga with pandals and processions."},
        {"festival": "Dussehra", "state": "Pan India", "description": "Victory of good over evil, marking end of Navratri."},
        {"festival": "Gandhi Jayanti", "state": "Pan India", "description": "Birthday of Mahatma Gandhi."}
    ],
    "November": [
        {"festival": "Diwali", "state": "Pan India", "description": "Festival of lights symbolizing victory of light over darkness."},
        {"festival": "Chhath Puja", "state": "Bihar", "description": "Sun worship performed at riverbanks."},
        {"festival": "Guru Nanak Jayanti", "state": "Punjab", "description": "Sikh celebration of the birth of Guru Nanak Dev Ji."}
    ],
    "December": [
        {"festival": "Christmas", "state": "Pan India", "description": "Celebration of the birth of Jesus Christ with joy and carols."},
        {"festival": "Hornbill Festival", "state": "Nagaland", "description": "Tribal celebration showcasing Naga culture and dance."},
        {"festival": "Losar", "state": "Ladakh & Arunachal", "description": "Tibetan Buddhist New Year with rituals and dance."}
    ]
}

# ---- Extract unique months and states ----
months = list(festival_calendar.keys())
all_states = sorted({fest["state"] for month in festival_calendar.values() for fest in month})
all_states = ["All"] + all_states  # Add 'All' option

# ---- Streamlit UI ----
st.set_page_config(page_title="Cultural Calendar", layout="centered")
st.title("🗓️ Cultural Calendar Explorer")

selected_month = st.selectbox("📅 Select Month", months)
selected_state = st.selectbox("📍 Select State", all_states)

# ---- Filter festivals based on month and state ----
festivals = festival_calendar.get(selected_month, [])

filtered_festivals = [
    fest for fest in festivals
    if selected_state == "All"
    or fest["state"] == selected_state
    or fest["state"] == "Pan India"
]

# ---- Display Result ----
if filtered_festivals:
    st.subheader(f"🎊 Festivals in {selected_state} during {selected_month}")
    for fest in filtered_festivals:
        st.markdown(f"### 🎉 {fest['festival']}")
        st.markdown(f"**State:** {fest['state']}")
        st.markdown(f"**Description:** {fest['description']}")
        st.markdown("---")
else:
    st.warning(f"No festivals found for {selected_state} in {selected_month}.")

