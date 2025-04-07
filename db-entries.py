import pymongo
import requests
from dotenv import load_dotenv
import os
from generate_embedding import generate_embedding
load_dotenv()

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

db = client.genaiDB

collection = db.movies



def create_movie_entries():
    movies = [
        {
            "title": "Avengers: Endgame",
            "description": "After the devastating events of Avengers: Infinity War, the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",
            "year": 2019,
            "genre": ["Action", "Adventure", "Sci-Fi"],
            "rating": 8.4
        },
        {
            "title": "Black Panther",
            "description": "T'Challa, heir to the hidden but advanced kingdom of Wakanda, must step forward to lead his people into a new future and must confront a challenger from his country's past.",
            "year": 2018,
            "genre": ["Action", "Adventure", "Sci-Fi"],
            "rating": 7.3
        },
        {
            "title": "Spider-Man: No Way Home",
            "description": "With Spider-Man's identity now revealed, Peter asks Doctor Strange for help. When a spell goes wrong, dangerous foes from other worlds start to appear, forcing Peter to discover what it truly means to be Spider-Man.",
            "year": 2021,
            "genre": ["Action", "Adventure", "Fantasy"],
            "rating": 8.2
        },
        {
            "title": "Guardians of the Galaxy",
            "description": "A group of intergalactic criminals must pull together to stop a fanatical warrior with plans to purge the universe.",
            "year": 2014,
            "genre": ["Action", "Adventure", "Comedy"],
            "rating": 8.0
        },
        {
            "title": "Iron Man",
            "description": "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.",
            "year": 2008,
            "genre": ["Action", "Adventure", "Sci-Fi"],
            "rating": 7.9
        }
    ]

    for movie in movies:
        # Only generate embedding for the title and description
        text_to_embed = f"{movie['title']} {movie['description']}"
        movie['embedding'] = generate_embedding(text_to_embed)
        
        # Insert the movie into the database
        collection.insert_one(movie)
        print(f"Inserted movie: {movie['title']}")

# Create the movie entries
create_movie_entries()
