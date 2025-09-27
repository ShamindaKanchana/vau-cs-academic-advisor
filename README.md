# VAU-CS Academic Advisor 🤖📚

## Project Overview
VAU-CS Academic Advisor is an intelligent chatbot system designed to assist students with academic inquiries. It leverages Google's Gemini AI to provide personalized academic guidance, course information, and study advice through a user-friendly chat interface.

## ✨ Features
- **Interactive Chat Interface**: Modern, responsive UI with markdown support
- **Intelligent Query Handling**: Understands and processes various academic queries
- **State Management**: Uses LangGraph for sophisticated conversation flow control
- **Database Integration**: Fetches course and module information from a MySQL database
- **Multi-modal Support**: Handles different types of academic inquiries:
  - Course content queries
  - Module information
  - Academic advice
  - General university information

## 🏗️ Architecture

### Frontend (React)
- Built with React 18 and Vite
- Modern UI with Material Icons
- Responsive design for all devices
- Real-time message rendering with markdown support

### Backend (Python/Flask)
- **API Layer**: RESTful endpoints for chat functionality
- **State Management**: LangGraph for managing complex conversation flows and state transitions
- **AI Integration**: 
  - Google Gemini for natural language understanding and generation
  - LangChain framework for building and chaining AI components
- **Database**: 
  - MySQL with SQLAlchemy ORM for structured data storage
  - LlamaIndex for efficient vector-based querying and retrieval
- **Key Technologies**:
  - **LangGraph**: Manages the conversation state machine, handling different conversation paths and maintaining context
  - **LlamaIndex**: Powers the semantic search and retrieval of academic content with vector embeddings
  - **SQLAlchemy**: ORM for database interactions and schema management

### Data Flow
1. User sends message → Frontend → Backend API
2. Backend processes message through LangGraph state machine
3. Appropriate agent handles the query
4. Response is generated and formatted with markdown
5. Frontend renders the markdown response

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js 16+
- MySQL 8.0+
- Google Gemini API key

### Backend Setup
1. Clone the repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
4. Set up environment variables in `.env`:
   ```
   GEMINI_API_KEY=your_gemini_api_key
   DB_HOST=your_db_host
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_NAME=academic_advisor
   DB_PORT=3306
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

### Database Setup
1. Create a new MySQL database:
   ```sql
   CREATE DATABASE academic_advisor;
   ```
2. Run the initialization script:
   ```bash
   python backend/models/init_database.py
   ```

## 🏃‍♂️ Running the Application

### Start Backend Server
```bash
cd backend
python main.py
```

### Start Frontend Development Server
```bash
cd frontend
npm run dev
```

Visit `http://localhost:5173` in your browser to access the application.

## 📂 Project Structure

### Backend
```
backend/
├── agents.py           # AI agent implementations
├── main.py            # Main application and API endpoints
├── database_supporter.py  # Database connection and queries
├── prompts.py         # AI prompt templates
├── states.py          # State definitions for LangGraph
├── models/            # Database models
├── services/          # Additional services
└── scripts/           # Utility scripts
```

### Frontend
```
frontend/
├── public/            # Static files
└── src/
    ├── components/    # React components
    ├── styles/        # CSS files
    └── App.jsx        # Main application component
```

## 🤖 How It Works

1. **User Input Processing**:
   - User messages are sent to the backend API
   - The system classifies the query type (subject content, results, general info)

2. **State Management with LangGraph**:
   - LangGraph orchestrates the conversation flow through a state machine
   - Different nodes in the graph handle specific query types:
     - `user_input_handler`: Routes queries to appropriate handlers
     - `subject_content_based`: Handles course content inquiries
     - `result_based_infor_extraction`: Processes result-related queries
     - `academic_advice_ready`: Manages academic guidance requests
   - State is maintained and transformed through the conversation
   - Conditional edges determine the flow based on query analysis

3. **Information Retrieval with LlamaIndex**:
   - Converts academic content into vector embeddings for semantic search
   - Enables efficient similarity-based retrieval of course materials
   - Handles complex queries by understanding the semantic meaning
   - Caches frequently accessed data for improved performance

3. **Response Generation**:
   - Relevant information is retrieved from the database
   - AI generates a natural language response
   - Response is formatted with markdown for rich display


## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact
shamindakanchana@gmail.com

---

Built with ❤️ by Shaminda Kanchana