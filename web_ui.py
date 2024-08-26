import streamlit as st
from PIL import Image
from base64 import b64encode
from pages import *
from constants import *
import os 
def inject_custom_css():
    st.markdown(
        """
        <style>
        .css-1v3fvcr edgvbvh9 { /* Sidebar radio button text */
            font-size: 20px !important; /* Adjust the size as needed */
        }
        .css-1v3fvcr { /* Sidebar radio button */
            min-height: 50px !important; /* Adjust the size as needed */
        }
        </style>
        """,
        unsafe_allow_html=True
    )



def sidebar():
    # Display your name
    st.sidebar.markdown(
        "<p style='text-align: center;'><b>Beytullah Yayla</b></p>", 
        unsafe_allow_html=True
    )
    
    # Get Profile Image
    try:
        with open(os.path.join(ASSETS_PATH, "beytullah_yayla_photo.png"), "rb") as img_file:
            img = "data:image/png;base64," + b64encode(img_file.read()).decode()
    except FileNotFoundError:
        img = ""  # You can add a fallback image or a placeholder here
    
    try:
        with open(os.path.join(ASSETS_PATH, "Beytullah Yayla Resume EN.pdf"), "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
    except FileNotFoundError:
        pdf_bytes = None  # Handle this appropriately if the file is missing
    
    # Display Profile Image with animation
    st.sidebar.write(f"""
    <style>
    @keyframes slowTilt {{
        0%, 100% {{
            transform: rotate(0deg);
        }}
        50% {{
            transform: rotate(5deg);
        }}
    }}
    .box img {{
        width: 150px;
        height: 150px;
        border-radius: 25%;
        animation: slowTilt 2s ease-in-out infinite;
    }}
    </style>
    <div style="display: flex; justify-content: center;">
        <div class="box">
            <img src="{img}" alt="Profile Image">
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add Social Icons
    social_icons_data = {
        "GitHub": ["https://github.com/BeytullahYayla", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
        "LinkedIn": ["https://www.linkedin.com/in/beytullahyayla/", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
        "Kaggle": ["https://www.kaggle.com/beytullahyayla", "https://www.kaggle.com/static/images/site-logo.svg"],
    }

    social_icons_html = [
        f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 10px;'>"
        f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'"
        f" style='width: 25px; height: 25px;'></a>"
        for platform in social_icons_data
    ]
    
    st.sidebar.write("Junior Data Scientist And AI Enthusiast")
    st.sidebar.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)
    
    st.sidebar.divider()
    
    # Download CV button
    if pdf_bytes:
        st.sidebar.download_button(label="📄 Download my CV", data=pdf_bytes, file_name="Beytullah Yayla CV.pdf", mime="application/pdf",)
    else:
        st.sidebar.write("CV is currently unavailable.")
    
    
def tabs():
    
        # Create tabs
        tabs = st.tabs(['Realtime Customer Counting', 'DentAI', 'Drivable Area Segmentation', 'Turtlebot3 ROS Object Detection', 'Behavioral Cloning Model'])

        # Assign each tab to a variable
        customer_counting_tab, dentai_tab, segmentation_tab, turtlebot3_tab, cloning_tab = tabs

        # Realtime Customer Counting Tab
        with customer_counting_tab:
            realtime_customer_counting()

        # DentAI Tab
        with dentai_tab:
            dentai()

        # Drivable Area Segmentation Tab
        with segmentation_tab:
            semantic_segmentation()

        # Turtlebot3 ROS Object Detection Tab
        with turtlebot3_tab:
            turtlebot3_object_detection()

        # Behavioral Cloning Model Tab
        with cloning_tab:
            self_driving_car_behavioral_clonning()

def main():
    st.set_page_config(page_title="Beytullah Yayla's Portfolio", page_icon="⭐")
    
    sidebar()
    # Render the tabs or the portfolio based on the query parameter
    tabs()

if __name__ == '__main__':
    main()
