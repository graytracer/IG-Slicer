import streamlit as st
import streamlit.components.v1 as components
import time

class RedirectApp:
    def __init__(self):
        # Set page config
        st.set_page_config(
            page_title="IG-Slicer - Redirecting",
            layout="centered",
        )
        
        # Initialize session state for tracking redirect status
        if 'redirect_triggered' not in st.session_state:
            st.session_state.redirect_triggered = False
        
    def create_ui(self):
        st.title("IG-Slicer has moved!")
        
        # Display message about the new website
        st.markdown("""
        ## We've moved to a new home!
        
        **Our new website is now available at:**
        
        ## [www.igslicer.site](https://www.igslicer.site)
        
        You will be automatically redirected in 4 seconds...
        """)
        
        # Use Streamlit components to inject pure HTML with JavaScript
        # This is more reliable than using st.markdown with unsafe_allow_html
        redirect_html = """
        <html>
        <head>
            <script>
                setTimeout(function() {
                    window.top.location.href = 'https://www.igslicer.site';
                }, 4000);
            </script>
        </head>
        <body></body>
        </html>
        """
        
        # Insert the HTML/JS component
        components.html(redirect_html, height=0)
        
        # Add a manual redirect button 
        st.markdown("---")
        st.markdown("If you are not redirected automatically, please click the button below:")
        
        # Use a button with custom styling to make it prominent
        st.markdown("""
        <style>
        div.stButton > button {
            background-color: #FF4B4B;
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 15px 30px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            width: 100%;
            margin-top: 20px;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Alternative approach for button: when clicked, use iframe to redirect
        if st.button("Go to www.igslicer.site now"):
            # Set redirect flag in session state
            st.session_state.redirect_triggered = True
            st.rerun()
        
        # If redirect was triggered by button click, show an iframe that handles the redirect
        if st.session_state.redirect_triggered:
            redirect_component = """
            <html>
            <head>
                <script>
                    window.top.location.href = 'https://www.igslicer.site';
                </script>
            </head>
            <body>
                <p>Redirecting...</p>
            </body>
            </html>
            """
            components.html(redirect_component, height=0)
            
            # Fallback message if JavaScript is disabled
            st.markdown("### Redirecting to [www.igslicer.site](https://www.igslicer.site)...")
            st.markdown("If you are not redirected, please [click here](https://www.igslicer.site) to visit the new website.")

if __name__ == "__main__":
    app = RedirectApp()
    app.create_ui() 
