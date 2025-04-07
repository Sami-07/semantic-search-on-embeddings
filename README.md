# Semantic Movie Search

This project demonstrates semantic search capabilities using MongoDB's vector search feature and Hugging Face's embedding model. It allows you to search for movies using natural language queries.

## Features

- Vector-based semantic search for movies
- Uses MongoDB's vector search capabilities
- Leverages Hugging Face's sentence-transformers/all-MiniLM-L6-v2 model for embeddings
- Sample movie database with popular titles

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your credentials:
```
MONGO_URI=your_mongodb_connection_string
HUGGING_FACE_TOKEN=your_hugging_face_api_token
```

3. Run the database setup script:
```bash
python db-entries.py
```

4. Go to MongoDB Atlas and create a vector search index with the following settings:
```
{
  "fields": [
    {
      "numDimensions": 384,
      "path": "embedding",
      "similarity": "dotProduct",
      "type": "vector"
    }
  ]
}
```

5. Run the search script:
```bash
python script.py
```

## Usage

The project includes sample queries that demonstrate different types of semantic searches:
- Direct title matches ("Avengers: Endgame")
- Conceptual matches ("movie about a hidden advanced kingdom")
- Thematic matches ("funny space adventure with criminals")

The search results will show the movie title and description for the top 5 most relevant matches.

## Requirements

- Python
- MongoDB Atlas (with vector search enabled)
- Hugging Face API token (for embedding generation)
