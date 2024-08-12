import streamlit as st
from PIL import Image
from base64 import b64encode
from pages import *
from constants import *

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
    selection = st.sidebar.radio('Projects', 
                                 ['Portfolio', 'Realtime Customer Counting', 'DentAI', 'Drivable Area Segmentation', 'Turtlebot3 Ros Object Detection', 'Behavioral Clonning Model'])

    if selection == 'Portfolio':
        web_portfolio()
    elif selection == 'Realtime Customer Counting':
        realtime_customer_counting()
    elif selection == 'DentAI':
        dentai()
    elif selection == 'Drivable Area Segmentation':
        semantic_segmentation()
    elif selection == 'Turtlebot3 Ros Object Detection':
        turtlebot3_object_detection()
    elif selection == 'Behavioral Clonning Model':
        self_driving_car_behavioral_clonning()

def main():
    st.set_page_config(page_title="Beytullah Yayla's Portfolio", page_icon="⭐")
    inject_custom_css()  # Inject the custom CSS
    sidebar()

if __name__ == '__main__':
    main()
