import time

st.title("IG-Slicer has moved! 🚀")

# Display a message with the new URL
st.markdown("""
### 🚀 We've moved to a better web app!
[Click here to visit IG Slicer](https://www.igslicer.site)

If you are not redirected automatically, please click the link above.
""")

# Use JavaScript to redirect in the same tab
redirect_script = """
<script>
    setTimeout(function() {
        window.location.href = "https://www.igslicer.site";
    }, 3000);  // Redirect after 3 seconds
</script>
"""
st.components.v1.html(redirect_script, height=0)
