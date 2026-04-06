import streamlit as st
import time
import base64 
from pathlib import Path
from streamlit_navigation_bar import st_navbar
from utils import _display_detected_frame, detect_camera, detect_image, detect_video, detect_webcam, load_onnx_model, load_model

st.set_page_config(
    page_title="FoodDetector",
    page_icon=":microscope:"
    
)

# import streamlit as st
# from PIL import Image

# image = Image.open('./pages/bg-about-cuisine.jpg')

# st.image(image)
# st.markdown(f"""
# <style>
#     .stImage  {{
#         position: relative;
#         overflow: hidden;
#     }}
# """, unsafe_allow_html=True)

# st.markdown(f"""
# <h1 class="header-title">📑 About FoodDetector</h1>
#             """, unsafe_allow_html=True)         

st.markdown('''
    <div id="top-section"></div>
    ''', unsafe_allow_html=True)
def img_to_base64(img_path):
    with open(img_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Convert your image to base64
img_path = './assets/img/bg-about-cuisine.png'
img_base64 = img_to_base64(img_path)

# Convert your image to base64
img_path_nutrition = './assets/img/nutrition-table.png'
img_base64_nutrition = img_to_base64(img_path_nutrition)

st.markdown(f"""
<div class="header-container">
    <img src="data:image/jpg;base64,{img_base64}" class="header-image">
    <div class="header-overlay">
        <div class="header-title">Welcome to FoodDetector</div>
        <div class="header-subtitle">An easy way to detect Vietnamese dishes!</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Import img
# def img_bg_cover(img_path):
#     with open(img_path, 'rb') as img_file:
#         return base64.b64encode(img_file.read()).decode('utf-8')

# current_path = Path(__file__).parent
# img_path = current_path / 'pages' / 'img' / 'bg-about-cuisine.jpg'
# img_cover = img_bg_cover(img_path)

# # Cover
# st.markdown(f"""
# <style>
#     .header-container {{
#         position: relative;
#         width: 100%;
#         height: calc(100px + 7vw);
#         overflow: hidden;
#     }}
#     .header-image {{
#         position: absolute;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 100%;
#         background-image: url(data:image/jpg;base64,{img_cover});
#         background-size: cover;
#         background-position: center top;
#     }}
    
#     .header-title {{
#     position: absolute;
#     bottom: 0;
#     /* left: 50%;
#     transform: translateX(-50%); */
#     width: 100%;
#     color: white;
#     background-color: rgba(0, 0, 0, 0.6);
#     padding: 5px 10px;
#     letter-spacing: 1px;
#     font-weight: 800;
#     }}
# </style>

# <div class="header-container">
#     <div class="header-image"></div>
#     <h1 class="header-title">📑 About FoodDetector</h1>
# </div>
# """, unsafe_allow_html=True)
# End Cover

model1 = load_model()
load_onnx_model()

def render_content():
    with st.container():
        # st.title("Welcome to _:green[FoodDetector]_ :male-detective:")
        st.divider()

    #     st.markdown('''
    # FoodDetector uses the _YOLOv10m_ pretrained models for fine-tuning with `VietFood57`, a new custom-made Vietnamese food dataset created for detecting local dishes and achieved a `mAP50` of `0.934`.  
    # It can be used to detect <a href="/Dataset" target="_blank" style="color: #4CAF50; font-weight: bold; font-style: italic; text-decoration: none;">`57`</a> Vietnamese dishes from a picture, video, webcam, and an IP camera through RTSP.
    # ''', unsafe_allow_html=True)

        st.markdown(f'''
    <ul class="define introduction" style="margin-top: 0; margin-bottom: 0;">
        <li class="define-li home-page">FoodDetector uses the <strong>YOLOv10m</strong> pretrained models for fine-tuning with <code>VietFood67</code>, 
        an enhanced custom-made Vietnamese food dataset created for detecting local dishes and achieved a <code>mAP50</code> of <code>0.934</code>.</li>
        <li class="define-li home-page">It can be used to detect <a href="/dataset" target="_self">67</a> Vietnamese dishes from a picture, video, webcam, and an IP camera through RTSP.</li>
    </ul>
                    ''', unsafe_allow_html=True)


        st.divider()

        st.markdown(f'''
                    <h4>Adjust the confident score</h4>
                    ''', unsafe_allow_html=True)
        confidence = float(st.slider(
            label="Confidence score",
            label_visibility="collapsed",
            min_value=10,
            max_value=100,
            value=50,
        )) / 100
        
        st.markdown(f'''
    <style>
        #quick-note {{
        margin-left: 0;
        margin-bottom: 0.5rem;
    }}
    
    p#quick-note.define {{
        margin-top: 0;
    }}

    .title-text-score {{
        font-weight: 700;
        border-radius: 5px;
        background-color: var(--grey);
        padding: 0.5rem;
        display: inline;
    }}

    p.define.subtitle-text-score {{
        margin-top: 0.8rem;
        margin-bottom: 1rem;
    }}
    
    </style>
    <p class="define" id="quick-note"><strong>Quick note</strong>: consideration for selecting the best suited confident score:</p>
    <div class="adjust-section">
        <p class="define title-text-score">High confident score (>= 50%):</p>
        <p class="define subtitle-text-score">Set a higher threshold will make the model to predict with a higher accuracy detection but it will have a low recall as fewer object will 
        be detected because of the high precision constraint.</p>
        <p class="define title-text-score">Low confident score (< 50%):</p>        
        <p class="define subtitle-text-score">Set a lower threshold will enable the model to detect more object - 
    high recall because of the low precision constraint.</p>
    </div>     
                ''', unsafe_allow_html=True)

        st.divider()
        st.markdown(f'''
                    <h4>Nutrition value score</h4>
                    ''', unsafe_allow_html=True)

        st.markdown(f'''
    <ul class="define nutrition" style="margin-top: 0; margin-bottom: 0;">
        <li class="define-li home-page">Our nutrition values are based on the <strong>Traffic Light system</strong>.</li>
        <li class="define-li home-page">All nutrition information provided is approximate.</li>
    </ul>
                    ''', unsafe_allow_html=True)
        
        # Initialize session state for nutrition details toggle
        if "show_nutrition_details" not in st.session_state:
            st.session_state.show_nutrition_details = False
        
        # Toggle button
        if st.button("See more", key="nutrition_toggle", use_container_width=False):
            st.session_state.show_nutrition_details = not st.session_state.show_nutrition_details
        
        # Show nutrition details if toggle is on
        if st.session_state.show_nutrition_details:
            st.markdown(f'''
<div class="nutrition-container">
    <img src="data:image/jpg;base64,{img_base64_nutrition}" class="nutrition-img">
    <ul class="nutrition-explain">
        <li class="nutrition-explain-details"><strong class="color-section" id="green">Green (Low)</strong>: Very healthy. Enjoy without worry.</li>
        <li class="nutrition-explain-details"><strong class="color-section" id="yellow">Yellow (Medium)</strong>: Consume in moderation or combine with healthier options.</li>
        <li class="nutrition-explain-details"><strong class="color-section" id="red">Red (High)</strong>: Limit consumption and look for healthier alternatives.</li>
    </ul>
    <p class="nutrition-explain-details">For more information, please refer to the <a href="https://www.nutricalc.co.uk/case-study/case-study-uk-traffic-light-front-of-pack-colour-thresholds/">NutriCalc</a>,
    <a href="https://heas.health.vic.gov.au/resources/government-guidelines/traffic-light-system/">Healthy Eating Advisory Service</a></p>

<style>
    li.nutrition-explain-details {{
        margin-bottom: 0.5rem !important;
        margin-top: 0.5rem !important;
    }}
    
    p.nutrition-explain-details {{
        font-weight: 400 !important;
        margin: 1rem 0 !important;
    }}
    
    img.nutrition-img {{
        margin-top: 1rem;
        margin-bottom: 1rem;
        width: 90%;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }} 
    
    .color-section {{
        padding: 3px 6px;
        border-radius: 5px;
    }}
    
    #green {{
        background-color: var(--green-nu);
    }}
    
    #yellow {{
        background-color: var(--yellow-nu);
    }}
    
    #red {{
        background-color: var(--red-nu);
    }}
</style>
''', unsafe_allow_html=True)
        
        st.markdown(f'''<br><br>''', unsafe_allow_html=True)        

        st.markdown("""
    <style>
    /* Style the tab labels */
    button[data-baseweb="tab"] {
        padding: calc(8px + 0.2vw) calc(8px + 0.5vw);
        gap: 0;

    }
    button[data-baseweb="tab"] p {
        font-size: calc(9px + 0.3vw) !important;
        font-weight: 500 !important;        
    }
    
    div[data-baseweb="tab-list"] {
        gap: 0;
    }
    /* Style the active tab */
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: var(--button-color-yellow); /* Active tab color */
        border-radius: 8px 7px 0 0;
        color: black;
    }

    /* Style the inactive tabs */
    button[data-baseweb="tab"][aria-selected="false"] {
        color: var(--grey-code-expander);
    }
    
    div[data-baseweb="tab-border"] {
    }
    </style>
""", unsafe_allow_html=True)
        
        st.subheader("Image Upload")

        st.markdown("""
- Uploading image files from the user’s local machine or using an image URL is supported.
- After the prediction process, two buttons will appear to download the results as an image file with bounding boxes or a CSV file.
- The results are generated when the user clicks the button and are named in the format: \`"%date-%month-%year".jpg/csv\`.
        """, unsafe_allow_html=True)

        if "last_uploaded_file_id" not in st.session_state:
            st.session_state.last_uploaded_file_id = None

        camera_photo = st.camera_input("Take a photo", label_visibility="hidden")
        uploaded_file = st.file_uploader("Or upload from library", accept_multiple_files=False, type=["png", "jpg", "jpeg"])

        # Reset detect_image states when a new file is selected
        current_file = camera_photo or uploaded_file
        if current_file is not None:
            file_id = getattr(current_file, "file_id", getattr(current_file, "name", id(current_file)))
            if file_id != st.session_state.last_uploaded_file_id:
                st.session_state.last_uploaded_file_id = file_id
                st.session_state.button_clicked = False
                st.session_state.show_image = True

        if camera_photo:
            detect_image(confidence, model=model1, uploaded_file=camera_photo)
        elif uploaded_file:
            detect_image(confidence, model=model1, uploaded_file=uploaded_file)

    st.markdown('''
    <div>
        <a href="#top-section" class="top-button" onclick="smoothScroll(event, 'top-section')">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="16" height="16">
            <path d="M240.971 130.524l194.343 194.343c9.373 9.373 9.373 24.569 0 33.941l-22.667 22.667c-9.357 9.357-24.522 9.375-33.901.04L224 227.495 69.255 381.516c-9.379 9.335-24.544 9.317-33.901-.04l-22.667-22.667c-9.373-9.373-9.373-24.569 0-33.941L207.03 130.525c9.372-9.373 24.568-9.373 33.941-.001z"/>
        </svg>
        </a>                
    </div>
    
    <script>
    function smoothScroll(event, targetId) {
        event.preventDefault();
        const targetElement = document.getElementById(targetId);
        if (targetElement) {
            targetElement.scrollIntoView({ behavior: 'smooth' });
        }
    }
    </script>
                ''', unsafe_allow_html=True)

def navbar(active_page):
    return ""

def styling_css():
    with open('./assets/css/general-style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    st.markdown("""
    <style>
/* Hide material icon wrapper in expander */
    [data-testid="stExpander"] span:has([data-testid="stIconMaterial"]) {
        display: none !important;
    }
    /* Hide file uploader button, prepend UPLOAD: to instructions text */
    [data-testid="stFileUploaderDropzone"] span:has([data-testid="stIconMaterial"]),
    [data-testid="stFileUploaderDropzone"] button {
        display: none !important;
    }
    [data-testid="stFileUploaderDropzoneInstructions"] span::before {
        content: "UPLOAD: ";
        font-weight: 600;
    }
    /* Yellow buttons: all st.button() calls */
    [data-testid="stButton"] button {
        background-color: #FEC51C !important;
        color: black !important;
        border-color: #FEC51C !important;
    }
    [data-testid="stButton"] button:hover {
        background-color: #fcd96b !important;
        border-color: #fcd96b !important;
    }
    </style>
    """, unsafe_allow_html=True)
 
        
def home_page():
    st.markdown(navbar('Home'), unsafe_allow_html=True)
    

def about_page():
    st.markdown(navbar('About'), unsafe_allow_html=True)
    

# Main app logic
def main():
        # Get the current page from the URL
    styling_css()
    query_params = st.query_params
    path = query_params.get("page", ["home"])[0].lower()
    
    # Always render the navbar
    st.markdown(navbar('Home' if path == 'home' else 'About'), unsafe_allow_html=True)
    
    if path == "about":
        st.markdown('<h1 style="color: white; font-size: 40px;">About Section</h1>', unsafe_allow_html=True)
        st.write("This is the About section. Here you can add information about your project or organization.")
    else:
        render_content()

if __name__ == "__main__":
    main()