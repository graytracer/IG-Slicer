import streamlit as st
import time
import streamlit.components.v1 as components

# Configure the page
st.set_page_config(
    page_title="IG-Slicer - Redirecting...",
    layout="centered"
)

# Custom HTML with meta refresh and JavaScript redirect
html_content = """
    <html>
        <head>
            <meta http-equiv="refresh" content="4;url=https://www.igslicer.site" />
            <style>
                .redirect-container {
                    text-align: center;
                    padding: 40px;
                    font-family: sans-serif;
                }
                .redirect-message {
                    font-size: 24px;
                    margin-bottom: 20px;
                }
                .new-url {
                    color: #FF4B4B;
                    font-size: 20px;
                    text-decoration: none;
                }
                .countdown {
                    font-size: 18px;
                    margin-top: 20px;
                    color: #666;
                }
            </style>
            <script>
                setTimeout(function() {
                    window.location.href = 'https://www.igslicer.site';
                }, 4000);
            </script>
        </head>
        <body>
            <div class="redirect-container">
                <div class="redirect-message">
                    IG-Slicer has moved to a new home!
                </div>
                <a href="https://www.igslicer.site" class="new-url">
                    www.igslicer.site
                </a>
                <div class="countdown">
                    Redirecting in 4 seconds...
                </div>
            </div>
        </body>
    </html>
"""

# Render the HTML
components.html(html_content, height=300) 
