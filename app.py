import streamlit as st
st.set_page_config(page_title="Cultural Lens", layout="wide")

st.image(r'images/Traveller Image.png')

st.title("🧭 Cultural Lens")
st.markdown("""
Welcome to **Cultural Lens**, a data-driven platform to explore, preserve, and promote India’s diverse art forms through responsible tourism.

### 🔍 What you can do:
- **Explore endangered art forms** across India
- **Predict tourism trends** for cultural hotspots
- **Generate personalized travel spots** to support lesser-known traditions
""")

# Add a sidebar with navigation options
st.sidebar.header("Navigate")
st.sidebar.markdown("""
- 🗺️ **Explore Regions**: Discover art forms by regions
- 🛤️ **Plan Your Journey**: Create custom travel places
- 🌟 **Contribute**: Share your experiences and insights
""")

# Add a call-to-action section
st.markdown("""
## 🌟 Why Cultural Lens?
India is home to a treasure trove of art forms, many of which are at risk of fading away. By exploring and supporting these traditions, you become a part of their preservation story.

### 📌 Join the Movement
- **Learn** about the rich culture of India
- **Support** artisans and local communities
- **Experience** the joy of responsible tourism

---
Use the left sidebar to start your cultural journey! 🎨🛤️📈
""")

# Add a footer with contact information
st.markdown("""
📬 **Contact Us**: For inquiries, collaborations, or feedback, reach out at [cultural.lens@example.com](mailto:cultural.lens@example.com)

🌐 **Follow Us**: Stay updated on [Instagram](https://instagram.com/cultural_lens) | [Twitter](https://twitter.com/cultural_lens)
""")
