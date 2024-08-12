import streamlit as st
from PIL import Image
from base64 import b64encode
from constants import *


def realtime_customer_counting():
    st.subheader('Realtime Customer Counting With Deep Learning Techniques')
    st.write('The application utilizes footage from in-store security cameras to provide store managers with valuable insights into customer behavior. It offers key functionalities such as customer identification, demographic categorization, and customer counting.')
    st.write('The customer detection feature tracks the number of people entering and exiting the store, while the classification feature groups customers by age, gender, and other demographic characteristics. Additionally, the application monitors customer density during specific time periods.')
    st.write('All this data is analyzed through a user-friendly web interface, enabling store managers to monitor and enhance store performance and customer behavior. This data-driven approach allows for more informed and detailed operational decisions.')
    st.write('Our application is built on cutting-edge computer vision and machine learning techniques, offering both real-time and historical data analysis. As a result, it makes store management more efficient and effective.')
    for image_path in IMAGE_REALTIME_COUNTING_PATHS.keys():
        st.image(ASSETS_PATH+image_path)
        st.markdown(f"<p style='text-align: center;'><i>{IMAGE_REALTIME_COUNTING_PATHS[image_path]}</i></p>", unsafe_allow_html=True)
    st.write("For more details about the project please click: ")
    st.write('[GitHub Repository](https://github.com/BeytullahYayla/Realtime-Customer-Counting-With-Deep-Learning-Techniques-And-Web-UI)')
    
def dentai():
    st.subheader('DentAI')
    st.write('DentAI is a mobile application designed to provide users with valuable information about their oral health. It serves as a preliminary diagnostic tool that can be used by both physicians and patients.')
    st.write('With the user-friendly mobile interface we developed, users can easily access the application. By uploading a photograph of their teeth, they can receive insights into potential oral diseases and the likelihood of these conditions. Additionally, the app offers advice on preventive measures to maintain oral health.')
    st.write('Instead of waiting for a lengthy appointment to learn about your dental health, you can use the DentAI application to gain preliminary information about your teeth and actively monitor your oral health with personalized features.')
    st.write('The application is developed using Python for the backend, React Native for the mobile interface, and MySQL for the database. We also utilized Ngrok as an API tunneling tool.')
    
    for image_path in IMAGE_DENTAI_PATHS.keys():
        image = Image.open(ASSETS_PATH+image_path)
        resized_image = image.resize((360, 800))
        st.image(resized_image, use_column_width=False)
        st.markdown(f"<p style='text-align: center;'><i>{IMAGE_DENTAI_PATHS[image_path]}</i></p>", unsafe_allow_html=True)
    st.write("For more details about the project please click: ")
    st.write('[GitHub Repository](https://github.com/BeytullahYayla/DentAI)')
def semantic_segmentation():
    st.subheader('Semantic Segmentation of Drivable Areas In Highways')
    st.markdown("In this project my aim is to detect drivable areas in highways using state of the art deep learning techniques and present a repository to autonomous vehicle engineers.")
    st.markdown("""
    ## 🚩 Contents
- Topics
- Getting Started
  *  Json2Mask
  *  Mask On Image
-   Preprocessing
      *   torchlike_data
      *   one_hot_encoder
      *   tensorize_image
      *   tensorize_mask
 -  Training
      *   Splitting Data
      *   Optimizer
      *   Loss Function
      *   Segmentation Model Selection
      *   Training Loop
  - Evaluation
  - Inference
    """)
    st.markdown("### Outputs from The Project")
    for image_path in IMAGE_DRIVABLE_AREA_SEGMENTATION_PATHS.keys():
        image = Image.open(ASSETS_PATH+image_path)
        image=image.resize((840,240))
        st.image(image, use_column_width=False)
        st.markdown(f"<p style='text-align: center;'><i>{IMAGE_DRIVABLE_AREA_SEGMENTATION_PATHS[image_path]}</i></p>", unsafe_allow_html=True)
    st.markdown("Developed ***segformer segmentation model*** and reached ***%98 intersection over unit(iou)*** score")
    st.write("For more detailed explanation about the project please click the link below")
    st.write('[GitHub Repository](https://github.com/BeytullahYayla/Drivable-Area-Segmentation-Using-Transformer-and-Unet-Architectures)')
def turtlebot3_object_detection():
    st.subheader('Turtlebot3 Object Detectıon Task in ROS')
    st.markdown("This project showcases the integration of TurtleBot3 with ROS (Robot Operating System) to perform object detection and basic navigation tasks. The primary goal of this project is to demonstrate how a TurtleBot3 robot can autonomously detect objects in its environment and navigate based on predefined patterns, such as drawing an equilateral triangle.")
    st.markdown("""
   # 🚩 Contents

- Getting Started
  *  Draw Equilateral Triangle
      * Message Files
      * Algorithm
  *  Laser Scanning
      * Laser Scanning Message Files
      * Laser Scanning Algorithm

  *  Object Detection and Finding Geometry Center
      * Object Detection Message Filese
      * Class Definition
   
  *  Final Project
    """)
    
    st.markdown("### Outputs from the Project")
    st.markdown("### Drawing Equilateral Triangle With Turtlebot Robot")    
    st.video(ASSETS_PATH+"turtlebot1.mp4")
    st.write("")
    st.write("### Laser Scanning")
    st.video(ASSETS_PATH+"turtlebot2.mp4")
    st.write("")
    st.write("### Object Detection with Turtlebot3")
    st.video(ASSETS_PATH+"turtlebot3.mp4")
    st.write("For more detailed explanation about the project please click the link below")
    st.write('[GitHub Repository](https://github.com/BeytullahYayla/Ros-Object-Detection-With-Turtlebot3)')
    
def self_driving_car_behavioral_clonning():
    st.subheader('Behavioral Clonning Method Implementation')
    st.markdown("Behavioral Clonning is a method by which human subcognitive skills can be captured and reproduced in a computer program. In this project I used behavioral cloning technique in shown below to train a neural network that can drive a car in Udacity Self Driving Car Simulation without hitting obstacles.")
    st.markdown("Data was collected with udacity self-driving car simulator. The Udacity simulator has two modes, training and autonomous, and two tracks. Training mode is to log the data for learning the driving behaviour. To do this I drove the car on track 1 keeping the car at centre of the lane and logged the data for 3 laps.")
    st.markdown("### Behavioral Clonning Method")    
    st.image(ASSETS_PATH+"behavioral_clonning.png")
    st.markdown("### Deep Learning Model Implemented From NVIDIA research paper")    
    st.image(ASSETS_PATH+"behavioral_clonning1.png")
    st.markdown("### Results")    
    st.video(ASSETS_PATH+"behavioral_clonning.mp4")
    
    st.write("For more detailed explanation about the project please click the link below")
    st.write('[GitHub Repository](https://github.com/BeytullahYayla/Self-Driving-Car-Simulation-Behavioral-Cloning)')
    
    
    
def web_portfolio():
   
    # Set the page title
    st.write(f"""
    <div class="title" style="text-align: center;">
    <span style='font-size: 32px;'>Hello! My name is Beytullah Yayla</span>👋
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<style>div.block-container{padding-top:3rem;}</style>',unsafe_allow_html=True)

    # Get Profile Image
    with open(ASSETS_PATH+"beytullah_yayla_photo.png", "rb") as img_file:
        img = "data:image/png;base64," + b64encode(img_file.read()).decode()
    
    # Reading Profile
    with open(ASSETS_PATH+"Beytullah Yayla CV.pdf", "rb") as pdf_file:
       pdf_bytes = pdf_file.read()

    st.write(f"""
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
    width: 300;
    height: 300;
    border-radius: 50%;
    animation: slowTilt 2s ease-in-out infinite;
    }}
    </style>
    <div style="display: flex; justify-content: center;">
    <div class="box">
    <img src="{img}">
    </div>
    </div>
    """, 
    unsafe_allow_html=True)

# Set the title
    st.write(f"""
             <div class=
             "subtitle" style="text-align: center;">Junior Data Scientist and AI Enthusiast</div>""",
              unsafe_allow_html=True)
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
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
    {''.join(social_icons_html)}
    </div>""", 
    unsafe_allow_html=True)

    st.write("##")

    # About Me Section
    st.subheader("About Me")

    st.markdown("""
    - 🧑‍💻 I am a **Junior Data Scientist and AI Enthusiast**.
    - 🚀 Previously, I served as an Artifical Intelligence Project Assistant at [Koçtaş](https://www.koctas.com.tr/) where I worked mostly on computer vision projects
    like **Realtime Customer Counting using IP Cameras** and **Perception part of a warehouse robot**. Additionally, I have 2 years of experience at [Ford Otosan](https://www.fordotosan.com.tr/)
    at a team developing l4 level highway autonomous truck and i took part of a perception team of autonomous truck during my internship.
    - 🛠️ **Tech Stack:** Python, Java, FastAPI, OpenCV, Tensorflow, Docker, Angular, MySQL 
    - ❤️ I am passionate about *Machine Learning/Deep Learning, MLOps, Data Science, Software Engineering, 
    Computer Vision, Data Analytics, Data Engineering*.
    - 🤖 Additionally, I am a Mentor at [Global AI Hub](https://www.linkedin.com/company/globalaihub/?originalSubdomain=ch), where I do mentorship on topics like deep learning, machine learning, and data science to mentees voluntarily.
    - 🏂 In my free time, I enjoy practicing guitar and listening to music.
    - 🪧 You can reach me at beytullahyayla1@gmail.com.
    - 🏠 Based in Turkey.
    """)

    st.write("##")

    # Download CV button
    st.download_button(label="📄 Download my CV", data=pdf_bytes, file_name="Beytullah Yayla CV.pdf", mime="application/pdf",)
    st.write("##")
    st.write(f"""<div class="subtitle" style="text-align: center;">🌟 Have A Wonderful Day!!! 🌟</div>""", unsafe_allow_html=True)
    