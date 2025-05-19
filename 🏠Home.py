import streamlit as st

# Page Configuration
st.set_page_config(page_title="Sanskrit Scope", layout="wide")

# Title
st.title("📚 Sanskrit Scope")


# About the App Section
st.markdown("### 🧭 About the App")
st.markdown("""
**Sanskrit Scope** is a cultural-tech initiative that blends machine learning, data visualization, and interactive tools to **preserve and promote India’s ancient Sanskrit-based heritage**.

This app allows you to:
- Explore endangered art forms rooted in Sanskrit and Vedic traditions
- Discover and recommend cultural travel destinations
- Interact with a smart **chatbot** for heritage and tourism queries
- Plan your visits with a **seasonal cultural calendar**

Whether you're a traveler, researcher, or heritage enthusiast, **Sanskrit Scope** is your window into timeless knowledge.
""")

# Features at a Glance
st.markdown("### 🛠️ Core Modules")
st.markdown("""
- 🎨 **Endangered Art Forms**  
  Explore rare and declining traditions across Indian regions.

- 🧭 **Cultural Spot Recommender**  
  Get personalized travel suggestions powered by AI to support heritage-rich destinations.

- 🤖 **Chatbot**  
  Ask questions about locations, practices, festivals, and art forms.

- 📅 **Seasonality & Cultural Calendar View**  
  Plan journeys around festivals, rituals, and best seasons to travel.
""")

# Sidebar Navigation
# Sidebar Navigation
st.sidebar.header("📌 Navigate")
st.sidebar.markdown("""
- 🏠 **Home**
- 🎨 **Endangered art forms**  
- 🧭 **Cultural Spot Recommender**  
- 🤖 **Chatbot**  
- 📅 **Seasonality & Cultural Calendar View**  
""")

# Why Sanskrit Scope Section
st.markdown("---")
st.markdown("## 🌟 Why Sanskrit Scope?")
st.markdown("""
India’s spiritual and cultural heritage, especially linked with **Sanskrit traditions**, is at risk of fading. **Sanskrit Scope** empowers you to reconnect, support, and celebrate this timeless legacy.

### 💡 Join the Movement
- 📚 **Learn** about Sanskrit-based art, knowledge, and traditions  
- 🧵 **Support** local communities and practitioners  
- 🌿 **Experience** responsible and meaningful travel  
""")

# Contact & Social Footer
st.markdown("---")
st.markdown("## 📬 Contact & Stay Connected")
st.markdown("""
- 🌐 **Author**: [Simran Shaikh](https://github.com/SimranShaikh20)  
""")

# Final Prompt
st.success("Use the left sidebar to begin your journey into Sanskrit heritage! 📜🛤️✨")
st.image(r'images/bg.jpg', use_container_width=True)
