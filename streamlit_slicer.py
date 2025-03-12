import streamlit as st

class RedirectApp:
    def __init__(self):
        # Set page config
        st.set_page_config(
            page_title="IG-Slicer - Redirecting",
            layout="centered",
        )
        
    def create_ui(self):
        st.title("IG-Slicer has moved!")
        
        # Display message about the new website
        st.markdown("""
        ## We've moved to a new home!
        
        **Our new website is now available at:**
        
        ## [www.igslicer.site](https://www.igslicer.site)
        
        You will be automatically redirected in 4 seconds...
        """)
        
        # Create a redirect with JavaScript after 4 seconds
        redirect_html = """
        <script type="text/javascript">
            // Function to redirect after 4 seconds
            function redirect() {
                window.location.href = "https://www.igslicer.site";
            }
            
            // Set timeout for 4 seconds
            setTimeout(redirect, 4000);
        </script>
        """
        
        # Inject the HTML/JS for redirect
        st.markdown(redirect_html, unsafe_allow_html=True)
        
        # Add a manual redirect button for users who have JavaScript disabled
        st.markdown("---")
        st.markdown("If you are not redirected automatically, please click the button below:")
        
        # Use a button with custom styling to make it prominent
        button_style = """
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
        """
        st.markdown(button_style, unsafe_allow_html=True)
        
        if st.button("Go to www.igslicer.site now"):
            js = f"""
            <script>
                window.location.href = "https://www.igslicer.site";
            </script>
            """
            st.markdown(js, unsafe_allow_html=True)

if __name__ == "__main__":
    app = RedirectApp()
    app.create_ui() 
