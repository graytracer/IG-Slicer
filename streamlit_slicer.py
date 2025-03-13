from readline import redisplay
import streamlit as st
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Redirector script started")

# Target URL
target_url = "https://www.igslicer.site"
logger.info(f"Target URL set to: {target_url}")

# Set minimal page config, removing borders and padding
st.set_page_config(
    page_title="IG-Slicer - Redirecting",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Create a clean, minimal HTML page that matches the IG-Slicer aesthetics
html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>IG-Slicer Has Moved</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Import the same fonts as IG-Slicer -->
    <link href="https://fonts.googleapis.com/css2?family=Chakra+Petch:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body, html {{
            height: 100%;
            margin: 0;
            padding: 0;
            font-family: 'Space Mono', monospace;
            background-color: #0F1116;
        }}
        .container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 20px;
            box-sizing: border-box;
            text-align: center;
        }}
        .card {{
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.05);
            padding: 40px;
            max-width: 500px;
            width: 100%;
            border-top: 3px solid #FFE600;
            text-align: center;
        }}
        .logo-container {{
            display: inline-block;
            position: relative;
            margin-bottom: 30px;
            text-align: center;
        }}
        .logo-text {{
            font-family: 'Chakra Petch', sans-serif;
            font-size: 3rem;
            font-weight: 700;
            letter-spacing: 4px;
            color: #000;
            text-transform: uppercase;
        }}
        .logo-tag {{
            font-family: 'Chakra Petch', sans-serif;
            position: absolute;
            top: 0;
            right: -40px;
            color: #FFE600;
            font-size: 1.5rem;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
        }}
        h1 {{
            font-family: 'Chakra Petch', sans-serif;
            font-size: 1.8rem;
            font-weight: 600;
            margin: 0 0 15px 0;
            color: #000;
            text-transform: uppercase;
            text-align: center;
        }}
        p {{
            font-family: 'Space Mono', monospace;
            font-size: 1rem;
            color: #333;
            margin-bottom: 25px;
            line-height: 1.6;
            text-align: center;
        }}
        .button-container {{
            display: flex;
            flex-direction: column;
            width: 100%;
            max-width: 320px;
            margin: 20px auto;
        }}
        .button {{
            font-family: 'Space Mono', monospace;
            padding: 16px 24px;
            border-radius: 4px;
            font-size: 1rem;
            font-weight: 700;
            cursor: pointer;
            text-decoration: none;
            text-align: center;
            display: block;
            transition: all 0.2s ease;
            text-transform: uppercase;
        }}
        .primary-button {{
            background-color: #FFE600;
            color: black;
            border: none;
        }}
        .primary-button:hover {{
            background-color: #FFD700;
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(255, 230, 0, 0.3);
        }}
        .note {{
            font-family: 'Space Mono', monospace;
            font-size: 0.85rem;
            color: #666;
            margin-top: 25px;
            padding-top: 15px;
            border-top: 1px solid #eee;
            max-width: 400px;
            margin-left: auto;
            margin-right: auto;
            text-align: center;
        }}
        .highlight {{
            background-color: #fffde7;
            padding: 2px 5px;
            border-radius: 3px;
            font-weight: 700;
        }}
        .countdown {{
            margin: 20px 0;
            font-family: 'Space Mono', monospace;
            font-size: 1rem;
            color: #333;
            text-align: center;
        }}
        .timer {{
            font-weight: 700;
            font-size: 1.3rem;
            color: #FFE600;
            background-color: #000;
            padding: 2px 10px;
            border-radius: 4px;
            display: inline-block;
            min-width: 30px;
        }}
        
        .popup-message {{
            display: none;
            background-color: #fff8e1;
            border: 1px solid #ffe082;
            border-radius: 4px;
            padding: 15px;
            margin: 15px 0;
            font-size: 0.9rem;
            color: #5d4037;
            text-align: center;
            animation: fadeIn 0.5s;
        }}
        
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        
        /* Mobile styles */
        @media (max-width: 767px) {{
            .card {{
                padding: 30px 20px;
            }}
            .logo-text {{
                font-size: 2.5rem;
                letter-spacing: 2px;
            }}
            .logo-tag {{
                font-size: 1.2rem;
                right: -30px;
            }}
            h1 {{
                font-size: 1.5rem;
            }}
            p {{
                font-size: 0.9rem;
            }}
            .button {{
                padding: 14px 20px;
                font-size: 0.9rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <div class="logo-container">
                <span class="logo-text">IG-SLICER</span>
                <span class="logo-tag">V2</span>
            </div>
            
            <h1>slicer got upgraded😎🔥</h1>
            <p> You'll be auto-redirected to the upgraded website. If not, click the below button to fly.</p>
            
            <div class="countdown">
                Redirecting in <span class="timer" id="countdown-timer">7</span> seconds...
            </div>
            
            <div id="popup-message" class="popup-message">
                <strong>Pop-up blocked!</strong> Click the button below to go to the new website.
            </div>
            
            <div class="button-container">
                <a href="{target_url}" class="button primary-button" target="_blank" id="redirect-button">
                    Go to igslicer.site
                </a>
            </div>
            
            <div class="note">
                <p>Don't forget to <span class="highlight">install the web-app</span> for better user experience!</p>
            </div>
        </div>  
    </div>
    
    <script>
        // Countdown timer for auto-redirect
        let secondsLeft = 7;
        const timerElement = document.getElementById('countdown-timer');
        const popupMessage = document.getElementById('popup-message');
        let redirectAttempted = false;
        
        function updateTimer() {{
            timerElement.textContent = secondsLeft;
            secondsLeft--;
            
            // When timer reaches zero, try to open in new window
            if (secondsLeft < 0 && !redirectAttempted) {{
                redirectAttempted = true;
                
                // Try to open in a new window - this may trigger the browser's popup blocker
                const newWindow = window.open("{target_url}", "_blank", "noopener,noreferrer");
                
                // Check if popup was blocked
                setTimeout(function() {{
                    if (!newWindow || newWindow.closed || typeof newWindow.closed == 'undefined') {{
                        // Show message if popup blocked
                        popupMessage.style.display = "block";
                        console.log("Popup blocked by browser");
                    }}
                }}, 500);
                
                return; // Stop the timer
            }}
            
            if (secondsLeft >= 0) {{
                // Continue timer
                setTimeout(updateTimer, 1000);
            }}
        }}
        
        // Start the timer immediately
        updateTimer();
        
        // For the manual button - just use default behavior
        document.getElementById('redirect-button').addEventListener('click', function() {{
            console.log("Manual redirect button clicked");
        }});
        
        // Debug timer
        console.log("Timer initialized");
    </script>
</body>
</html>
"""

# Hide all Streamlit elements
hide_streamlit_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 0; padding-bottom: 0;}
    iframe {height: 100vh !important; border: none !important;}
    .stApp {
        overflow: hidden !important;
    }
    body {
        overflow: hidden !important;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Render the HTML component
st.components.v1.html(
    html,
    height=800,
    scrolling=False
)

logger.info("IG-Slicer style redirector page with popup redirection")
