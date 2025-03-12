import streamlit as st

# Set page config immediately
st.set_page_config(
    page_title="IG-Slicer - Redirecting",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Use direct JavaScript redirection with window.location to force the redirect
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
            font-weight: bold;  /* Make header bold */
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
        // Immediate execution with direct window.location approach
        (function() {
            const targetUrl = "https://www.igslicer.site";
            let seconds = 5;
            
            // Force redirect after 5 seconds (bypass any potential restrictions)
            setTimeout(function() {
                window.location.href = targetUrl;
            }, 5000);
            
            // Update countdown display
            const interval = setInterval(function() {
                seconds--;
                document.getElementById('countdown').textContent = seconds;
                
                if (seconds <= 0) {
                    clearInterval(interval);
                }
            }, 1000);
            
            // Make link also use direct navigation
            document.getElementById('redirect-link').onclick = function(e) {
                e.preventDefault();
                window.location.href = targetUrl;
                return false;
            };
        })();
    </script>
    """, 
    unsafe_allow_html=True
)

# Add a fallback link in case JavaScript is disabled
st.markdown("""
    <noscript>
        <meta http-equiv="refresh" content="0;url=https://www.igslicer.site" />
        <p>JavaScript is disabled. Click <a href="https://www.igslicer.site">here</a> to be redirected.</p>
    </noscript>
""", unsafe_allow_html=True)

# Prevent any other UI elements from showing
st.stop()
