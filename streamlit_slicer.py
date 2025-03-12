import streamlit as st
from PIL import Image
import io
import base64
import zipfile
import os
from datetime import datetime

# Set page config immediately
st.set_page_config(
    page_title="IG-Slicer - Redirecting",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Create automatic redirect using JavaScript location.replace() which changes the browser URL
st.markdown(
    """
    <style>
        .redirect-container {
            text-align: center;
            padding: 50px;
            margin-top: 100px;
            background-color: #f0f2f6;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .redirect-title {
            font-size: 2.5em;
            margin-bottom: 20px;
            color: #262730;
        }
        .redirect-message {
            font-size: 1.5em;
            margin-bottom: 30px;
            color: #262730;
        }
        .redirect-link {
            font-size: 1.2em;
            color: #4B9FE1;
            text-decoration: underline;
            cursor: pointer;
        }
        .url-display {
            font-size: 1.3em;
            color: #0a5c0a;
            margin: 15px 0;
            font-weight: bold;
            background-color: #e8f4e8;
            padding: 10px;
            border-radius: 5px;
            display: inline-block;
        }
        .countdown {
            font-size: 1.2em;
            margin-top: 20px;
            color: #555;
        }
    </style>
    <div class="redirect-container">
        <div class="redirect-title">IG-Slicer Has Moved!</div>
        <div class="redirect-message">We've launched a brand new web app with improved features.</div>
        <div class="url-display">www.igslicer.site</div>
        <div><a href="https://www.igslicer.site" class="redirect-link" onclick="redirectNow(); return false;">Go there now</a></div>
        <div class="countdown">Redirecting automatically in 5 seconds...</div>
    </div>
    <script>
        // Function to redirect immediately
        function redirectNow() {
            window.location.replace('https://www.igslicer.site');
        }
        
        // Countdown and auto-redirect
        var seconds = 5;
        function countdown() {
            var countdown = document.querySelector('.countdown');
            seconds--;
            if (seconds > 0) {
                countdown.innerHTML = 'Redirecting automatically in ' + seconds + ' seconds...';
                setTimeout(countdown, 1000);
            } else {
                countdown.innerHTML = 'Redirecting now...';
                redirectNow();
            }
        }
        setTimeout(countdown, 1000);
    </script>
    """, 
    unsafe_allow_html=True
)

# Optionally, you can keep a minimal version of your original code below to handle 
# cases where the redirect doesn't work, but hide it behind an expander
with st.expander("Having trouble with the redirect? Click here to use the legacy version"):
    class StreamlitImageSlicer:
        def __init__(self):
            # Initialize session state
            if 'y_offset' not in st.session_state:
                st.session_state.y_offset = 0
            if 'processed_image' not in st.session_state:
                st.session_state.processed_image = None
            if 'final_image' not in st.session_state:
                st.session_state.final_image = None
            if 'bg_color' not in st.session_state:
                st.session_state.bg_color = 'black'

        def create_ui(self):
            st.title("Legacy IG-Slicer")
            st.warning("This is the old version. Please visit our new site at [www.igslicer.site](https://www.igslicer.site) for the best experience.")
            
            with st.sidebar:
                uploaded_file = st.file_uploader("Choose image: (suggested.img-width:≥3112px)", type=['png', 'jpg', 'jpeg'])
                grid_type = st.selectbox("Grid Type:", ["1x3", "2x3", "3x3"])
                bg_color = st.selectbox("Background Color (If Need) :", ["black", "white"])

            # Display notice about the new site
            st.markdown("""
                ## IG-Slicer has a new home!
                Our app has moved to [www.igslicer.site](https://www.igslicer.site) with improved features.
                
                This legacy version will be maintained for a limited time.
            """)

            # Rest of your original code would go here, but simplified for brevity
            if uploaded_file is not None:
                st.info("Processing is available on our new site. Please visit [www.igslicer.site](https://www.igslicer.site)")

    if st.button("Load Legacy Version"):
        app = StreamlitImageSlicer()
        app.create_ui()
