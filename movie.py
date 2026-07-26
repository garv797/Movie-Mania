import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(
    groq_api_key=os.getenv("Groq_Api_key"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)
def get_movie_suggestions(genre,Subgenre,Mood,Rp,Language,Country,IMDbRating,Runtime,ViolenceLevel,sp,Avoid):
   prompt = PromptTemplate.from_template("""
You are an expert movie recommendation system.
Recommend 5 movies based on the user's preferences.
Preferences:
Genre: {genre}
Subgenre: {subgenre}
Mood: {mood}
Release Preference: {Rp}
Language: {language}
Country: {country}
Minimum IMDb Rating: {imdbrating}
Runtime: {runtime}
Violence Level: {violence_level}
Streaming Platform: {sp}
Avoid: {avoid}

For every movie provide:
- Title
- Release Year
- IMDb Rating
- Genres
- Runtime
- Why it matches
- Where it can be streamed
Avoid recommending movies that violate the user's preferences.

    """)
   parser = StrOutputParser()
   chain = prompt | llm | parser
   response = chain.invoke({
        "genre": genre,
        "subgenre": Subgenre,
        "mood": Mood,
        "Rp": Rp,
        "language": Language,
        "country": Country,
        "imdbrating": IMDbRating,
        "runtime": Runtime,
        "violence_level": ViolenceLevel,
        "sp": sp,
        "avoid": Avoid
    })
   return response



