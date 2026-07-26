import streamlit as st
from movie import get_movie_suggestions
st.set_page_config(
    page_title="Movie Mania",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(180deg, #0f0f1a 0%, #1a1a2e 100%);
        }
        h1, h2, h3 { color: #f5f5f5 !important; }
        .hero-subtitle {
            color: #b8b8d1;
            font-size: 1.05rem;
            margin-top: -10px;
            margin-bottom: 1.5rem;
        }
        .stButton>button {
            width: 100%;
            background: linear-gradient(90deg, #e50914, #ff6a00);
            color: white;
            font-weight: 600;
            font-size: 1.2rem;
            padding: 1rem 1.5rem;
            border: none;
            border-radius: 10px;
            transition: transform 0.15s ease;
        }
        .stButton>button:hover {
            transform: scale(1.02);
            box-shadow: 0 4px 18px rgba(229, 9, 20, 0.4);
        }
        .chip {
            display: inline-block;
            background: #2a2a40;
            color: #e0e0f0;
            padding: 4px 12px;
            border-radius: 20px;
            margin: 3px;
            font-size: 0.85rem;
            border: 1px solid #3f3f5c;
        }
        section[data-testid="stSidebar"] {
            background: #14141f;
            border-right: 1px solid #2a2a40;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🎬 Movie Mania")
st.markdown(
    '<p class="hero-subtitle">Tell us your mood, we\'ll tell you what to watch — powered by AI.</p>',
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("## 🎛️ Build Your Filter")

    with st.expander("🎭 Genre & Mood", expanded=True):
        genre = st.selectbox(
            "Genre",
            ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Thriller"],
        )
        subgenre = st.selectbox(
            "Subgenre",
            ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Thriller"],
        )
        mood = st.selectbox(
            "Mood",
            [
                "Happy", "Emotional", "Dark", "Suspenseful", "Mind-blowing",
                "Inspirational", "Relaxing", "Funny", "Feel-good",
                "Heartbreaking", "Creepy", "Adrenaline-filled",
            ],
        )

    with st.expander("🌍 Origin & Language"):
        language = st.selectbox(
            "Language",
            ["English", "Hindi", "Korean", "Japanese", "Spanish", "French", "Any language"],
        )
        country = st.selectbox(
            "Industry / Region",
            ["Hollywood", "Bollywood", "Korean", "Japanese", "European", "International"],
        )
        release_pref = st.selectbox(
            "Release preference",
            ["Latest releases", "2020+", "2010+", "Classics", "Any"],
        )

    with st.expander("⭐ Quality & Format"):
        imdb_rating = st.selectbox(
            "Minimum IMDb rating",
            ["Above 7", "Above 8", "Above 8.5"],
        )
        runtime = st.selectbox(
            "Runtime",
            ["Under 90 minutes", "Around 2 hours", "No preference"],
        )
        streaming_platform = st.selectbox(
            "Streaming platform",
            ["Netflix", "Prime Video", "Disney+", "Any"],
        )

    with st.expander("⚠️ Content Preferences"):
        violence_level = st.selectbox(
            "Violence level",
            ["None", "Mild", "Moderate", "High"],
        )
        avoid = st.selectbox(
            "Avoid",
            [
                "Excessive gore", "Musicals", "Superhero movies", "Sequels",
                "Franchises", "Low-rated movies", "Predictable endings",
            ],
        )

    st.markdown("---")
    
find_clicked = st.button("Get Movie Suggestions")
st.markdown("#### Your picks")
chips = [genre, subgenre, mood, release_pref, language, country,
         imdb_rating, runtime, violence_level, streaming_platform, avoid]
st.markdown(" ".join(f'<span class="chip">{c}</span>' for c in chips), unsafe_allow_html=True)

st.markdown("")  # spacer

if find_clicked:
    try:
        with st.spinner("🍿 Finding the best movies for you..."):
            response = get_movie_suggestions(
                genre,
                subgenre,
                mood,
                release_pref,
                language,
                country,
                imdb_rating,
                runtime,
                violence_level,
                streaming_platform,
                avoid,
            )
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(response)
        st.markdown("</div>", unsafe_allow_html=True)
        st.success("Done! Enjoy your movie night! 🍿")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("👈 Set your preferences in the sidebar, then hit **Get Movie Suggestions**.")
    