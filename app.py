import streamlit as st
import pandas as pd
import base64
import ast

def set_video_background(video_file):
    with open(video_file, "rb") as video:
        video_bytes = video.read()
    video_base64 = base64.b64encode(video_bytes).decode()

    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto:wght@400;700&display=swap');

        /* --- General Setup & Background --- */
        .stApp {{
            background-color: transparent;
        }}
        #bg-video {{
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            object-fit: cover; z-index: -1; filter: blur(4px); opacity: 0.5;
        }}

        /* --- Main Content Container --- */
        .main .block-container {{
            background-color: rgba(10, 10, 20, 0.9); /* Darker overlay for better text contrast */
            border-radius: 15px;
            padding: 2rem;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}

        /* --- Themed Elements & Typography --- */
        h1 {{
            font-family: 'Playfair Display', serif; /* Newspaper font */
            color: #FFFFFF;
            font-size: 3.2em !important;
            text-align: center;
            padding-bottom: 1.5rem;
        }}
        h3.subtitle {{
            text-align: center;
            color: #CCCCCC;
            font-family: 'Roboto', sans-serif;
            margin-top: -2rem; /* Pull subtitle closer to title */
            margin-bottom: 2rem;
        }}
        h2, h3, h4, h5 {{
            color: #E62429; /* Spider-Man Red */
            font-family: 'Roboto', sans-serif;
            font-weight: bold;
        }}
        p, .stMarkdown, .stMetric {{
            font-family: 'Roboto', sans-serif;
            font-size: 1.1em !important; /* Slightly adjusted text size for balance */
        }}

        /* --- Dropdown Selector (Half-width, right-aligned) --- */
        .stSelectbox div[data-baseweb="select"] > div {{
            border: 2px solid #0056b3; /* Spider-Man Blue */
        }}

        /* --- Professional Detail Cards --- */
        .detail-card {{
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 6px;
            padding: 0.5rem 0.8rem; /* Compact padding */
            margin-bottom: 0.4rem;
            border-left: 4px solid #0056b3;
        }}
        .detail-card strong {{
            color: #E62429; /* Red for emphasis */
        }}

        /* --- High-Contrast Synopsis & Comments Box --- */
        .content-box {{
            background-color: rgba(0, 0, 0, 0.25);
            border-radius: 8px;
            padding: 1rem;
            margin-top: 1rem;
        }}
        .content-box p {{
            color: #f0f2f6;
            line-height: 1.5;
            font-size: 1.2em !important;
        }}
        .comments-container {{
            height: 180px; /* Reduced height to prevent scrolling */
            overflow-y: auto;
            border-radius: 5px;
            padding-right: 10px; /* Space for scrollbar */
        }}
        .comment-box {{
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding: 0.5rem 0;
            margin-bottom: 0.5rem;
            font-size: 1em;
        }}

        /* --- Default Welcome View Styling --- */
        .welcome-container img {{
            border-radius: 10px;
        }}
        .welcome-container p {{
            font-size: 1.2em;
            line-height: 1.5;
        }}
                
        /* --- GitHub Social Links --- */
        .social-links {{
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            margin-top: 2rem;
        }}
        .social-links a {{
            display: flex;
            align-items: center;
            text-decoration: none;
            color: #CCCCCC;
            font-weight: bold;
            transition: color 0.3s;
        }}
        .social-links a:hover {{
            color: #E62429; /* Spider-Man Red on hover */
        }}
        .social-links img {{
            width: 24px;
            height: 24px;
            margin-right: 0.5rem;
        }}

        </style>

        <video autoplay muted loop id="bg-video">
            <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
        </video>
        """,
        unsafe_allow_html=True
    )

# --- Load Your Data ---
try:
    df = pd.read_csv('spiderman_sentiment_data.csv')
except FileNotFoundError:
    st.error("Error: 'spiderman_sentiment_data.csv' not found. Please run the data collection notebook first.")
    st.stop()

st.set_page_config(page_title="The Daily Bugle Report", layout="wide")
set_video_background('Bg.mp4')

# --- App Header ---
st.title("THE DAILY BUGLE REPORT")

# --- Interactive Selector (Right-Aligned) ---
_, col2 = st.columns([1, 1])
with col2:
    storyline_options = ["-- Select an Arc to Analyze --"] + df['Storyline'].tolist()
    selected_arc = st.selectbox("", storyline_options, label_visibility="collapsed")

# --- Display Area ---
if selected_arc != "-- Select an Arc to Analyze --":
    arc_data = df[df['Storyline'] == selected_arc].iloc[0]

    col1, col2 = st.columns([1, 2]) # Ratio for a smaller image

    with col1:
        placeholder_image = "https://placehold.co/400x600/0a0a14/E62429?text=COVER+ART%0ANOT+AVAILABLE"
        image_to_display = arc_data['image_url'] if pd.notna(arc_data['image_url']) else placeholder_image
        st.image(image_to_display, use_container_width=True) # <-- FIX APPLIED

    with col2:
        st.header(f"{arc_data['Storyline']}")

        # Display details in styled "cards"
        st.markdown(f'<div class="detail-card"><strong>Publication Date:</strong> {arc_data["Publication_Date"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-card"><strong>Issue(s):</strong> {arc_data["Issues"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-card"><strong>Writer(s):</strong> {arc_data["Writers"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-card"><strong>Penciller(s):</strong> {arc_data["Pencillers"]}</div>', unsafe_allow_html=True)

        # Synopsis (now in the right column)
        st.markdown("<h5>SYNOPSIS</h5>", unsafe_allow_html=True)
        st.markdown(f'<div class="content-box"><p>{arc_data["synopsis"]}</p></div>', unsafe_allow_html=True)

        sub_col1, sub_col2 = st.columns(2)

        with sub_col1:
            st.markdown("<h5>THE PEOPLE'S VERDICT</h5>", unsafe_allow_html=True)
            st.metric(label="Average Fan Sentiment", value=f"{arc_data['fan_sentiment_score']:.2f}")
            st.progress((arc_data['fan_sentiment_score'] + 1) / 2)

        with sub_col2:
            st.markdown("<h5>TOP FAN COMMENTS</h5>", unsafe_allow_html=True)
            try:
                if pd.notna(arc_data['fan_comments']):
                    fan_comments = ast.literal_eval(arc_data['fan_comments'])
                    if fan_comments:
                        comment_html = ""
                        for comment in fan_comments:
                            comment_html += f'<div class="comment-box">{comment}</div>'
                        st.markdown(f'<div class="comments-container">{comment_html}</div>', unsafe_allow_html=True)
                    else:
                        st.info("No fan comments were found.")
                else:
                     st.info("No fan comments were found.")
            except (ValueError, SyntaxError):
                st.error("Could not parse comments.")

else:
    # --- Default Welcome View ---
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("default.jpg", use_container_width=True) # <-- FIX APPLIED
    with col2:
        st.markdown("""
<div class="welcome-container">
    <h2>Welcome to The Daily Bugle Report!</h2>
    <p><strong>An interactive data science project that quantifies fan sentiment across Spider-Man's most iconic comic book storylines.</strong></p>
    <p>This dashboard goes beyond subjective reviews to deliver a data-driven verdict on the web-slinger's history. It employs a full data pipeline to automatically scrape, process, and analyze thousands of fan discussions, revealing the true consensus on celebrated sagas and controversial moments alike.</p>
    <h4>Dashboard Features:</h4>
    <ul>
    <li><b>Explore Decades of History:</b> Navigate a comprehensive, scraped list of major story arcs, from the Silver Age to modern classics.</li>
    <li><b>Access In-Depth Story Details:</b> Instantly view official synopses, creative teams, and publication data for every arc.</li>
    <li><b>Discover the Fan-Approved Verdict:</b> See a quantitative sentiment score, calculated using Natural Language Processing on real-world fan comments.</li>
    </ul>
    <h4>Technology Spotlight:</h4>
    <p>This project was built with <strong>Python</strong>, featuring a data pipeline powered by <strong>Pandas</strong>, <strong>Beautiful Soup</strong>, and <strong>PRAW</strong> (Reddit API). Sentiment analysis is handled by <strong>NLTK</strong>, and the interactive frontend is delivered by <strong>Streamlit</strong> with custom <strong>HTML/CSS</strong>.</p>
    <p><strong>Ready to explore? Select a story arc from the dropdown menu above to begin.</strong></p>
    <div class="social-links">
      <a href="https://github.com/Pratap-Samar/Daily-Bugle-Sentiment-Dashboard" target="_blank">
      <img src="https://raw.githubusercontent.com/Pratap-Samar/Daily-Bugle-Sentiment-Dashboard/main/github.png" alt="GitHub Logo">
      View Repository
      </a>
      <a href="https://github.com/Pratap-Samar" target="_blank">
      <img src="https://raw.githubusercontent.com/Pratap-Samar/Daily-Bugle-Sentiment-Dashboard/main/github.png" alt="GitHub Logo">
      My Profile
      </a>
    </div>
</div>
""", unsafe_allow_html=True)
