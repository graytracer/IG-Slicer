import streamlit as st

# Set page config immediately
st.set_page_config(
    page_title="IG-Slicer - Redirecting",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Create JavaScript-based redirect that updates URL in browser history
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
        }
        .countdown {
            font-size: 1.2em;
            margin-top: 20px;
            color: #555;
        }
        /* Hide Streamlit elements */
        #MainMenu, footer, header {
            visibility: hidden;
        }
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
    </style>
    <div class="redirect-container">
        <div class="redirect-title">IG-Slicer Has Moved!</div>
        <div class="redirect-message">We've launched a brand new web app with improved features.</div>
        <a href="https://www.igslicer.site" class="redirect-link" id="redirect-link">Visit www.igslicer.site now</a>
        <div class="countdown">Redirecting automatically in <span id="countdown">5</span> seconds...</div>
    </div>
    <script>
        // More reliable window.location.replace method
        var seconds = 5;
        var targetUrl = "https://www.igslicer.site";
        
        function countdown() {
            var countdownElement = document.getElementById('countdown');
            seconds--;
            countdownElement.textContent = seconds;
            
            if (seconds <= 0) {
                // This method replaces the current URL in browser history
                window.location.replace(targetUrl);
            } else {
                setTimeout(countdown, 1000);
            }
        }
        
        // Start countdown
        setTimeout(countdown, 1000);
        
        // Also handle click on redirect link
        document.getElementById('redirect-link').addEventListener('click', function(e) {
            e.preventDefault();
            window.location.replace(targetUrl);
        });
    </script>
    """, 
    unsafe_allow_html=True
)

# Prevent any other UI elements from showing
st.stop()
