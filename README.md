# vau-cs-academic-advisor

## Project Overview
vau-cs-academic-advisor is an academic advisory chatbot system that leverages advanced AI models, including Google's Gemini generative AI, to provide subject content-based and result-based information retrieval and extraction.

## Features
- Handles user input to identify academic advising needs.
- Provides subject content-based advice and information retrieval.
- Extracts result-based information for academic queries.
- Utilizes a state graph to manage conversation flow.
- Integrates with a database for academic subject data.

## Technologies Used
- Python
- LangGraph for state management
- LangChain Google Gemini AI for natural language processing
- SQLAlchemy for database interaction
- LlamaIndex for query engine

## Installation
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies from `requirements.txt`.
4. Set up environment variables in `.env` (e.g., GEMINI_API_KEY).

## Usage
Run the main application:
```
python main.py
```

## Project Structure
- `main.py`: Entry point, sets up the state graph and nodes.
- `agents.py`: Contains AI agent functions handling different user inputs.
- `database_supporter.py`: Manages database connections and queries.
- `prompts.py`: Contains prompt templates for AI models.
- `states.py`: Defines data structures for state management.
- `models/`: Contains data models.
- `services/`: Additional service modules.
- `scripts/`: Utility scripts.

## License
Specify your license here.

---

Feel free to contribute or raise issues for improvements.