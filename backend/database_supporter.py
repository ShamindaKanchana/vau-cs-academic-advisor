"""
Database Retriever for Academic Chatbot using Gemini
"""
from typing import Dict, Any, Optional, List
import logging
import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine, text
from llama_index.core import SQLDatabase
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from llama_index.core import Settings



# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

class DatabaseRetriever:
    """Database retriever for academic chatbot using Gemini."""

    def __init__(self, tables: Optional[List[str]] = None):
        """
        Initialize database retriever.
        
        Args:
            tables: List of table names to use for querying (default: ["subjects"])
        """
        self.tables = tables or ["subjects"]  # Focus on your subjects table
        self.engine = None
        self.sql_database = None
        self.query_engine = None

        # Initialize connection
        self._initialize_connection()

    def _initialize_connection(self):
        """Initialize database connection using your existing setup."""
        try:
            logger.info("Initializing database connection...")

            # Create engine with your preferred settings
            from services.database import engine
            self.engine = engine

            # Test connection
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))

            logger.info("✅ Database connection successful!")

            # Initialize SQLDatabase with specified tables
            self.sql_database = SQLDatabase(self.engine, include_tables=self.tables)
            print("✅ SQLDatabase initialized with tables: {self.tables}")
            self.query_engine = self._initialize_query_engine()
            print("✅ Query engine initialized with tables: {self.tables}")

        except Exception as e:
            logger.error(f"❌ Database connection failed: {str(e)}")
            raise

    def _initialize_query_engine(self):
        """Initialize the natural language query engine with Gemini."""
        try:
            # Get Gemini API key from environment variables
            gemini_api_key = os.getenv('GEMINI_API_KEY')
            if not gemini_api_key:
                raise ValueError("GEMINI_API_KEY environment variable is required")
            
            llm = Gemini(
                model_name="models/gemini-2.5-pro",  # Using gemini-pro instead of flash
                
                api_key=gemini_api_key ,
                temperature=0.1,
                max_tokens=1024,
            )
            embedding = GeminiEmbedding(
                model_name="models/embedding-001",  # Using gemini-pro instead of flash
                api_key=gemini_api_key,
                max_tokens=1024,
            )
            Settings.embed_model = embedding
            
            return NLSQLTableQueryEngine(
                sql_database=self.sql_database,
                llm=llm,
                embedding=embedding,
                verbose=True,  # Set to True for debugging
            )
        except Exception as e:
            logger.error(f"❌ Query engine initialization failed: {str(e)}")
            raise

    def query(self, query_text: str) -> Dict[str, Any]:
        """Execute a natural language query against the database."""
        if not self.query_engine:
            raise ValueError("Query engine not initialized")

        try:
            response = self.query_engine.query(query_text)
            
            # Extract SQL query and result
            sql_query = ""
            if hasattr(response, 'metadata') and response.metadata:
                sql_query = str(response.metadata.get("sql_query", ""))
            
            return {
                "success": True,
                "sql_query": sql_query,
                "result": str(response),
                "error": None,
            }
        except Exception as e:
            logger.error(f"❌ Query execution failed: {str(e)}")
            return {
                "success": False, 
                "sql_query": "", 
                "result": None, 
                "error": str(e)
            }

    def get_available_tables(self) -> List[str]:
        """Get list of all available tables in the database."""
        if not self.engine:
            return []
        
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text("SHOW TABLES"))
                return [row[0] for row in result.fetchall()]
        except Exception as e:
            logger.error(f"Error fetching tables: {str(e)}")
            return []

    def close(self):
        """Clean up resources and close database connection."""
        try:
            if self.engine:
                self.engine.dispose()
                logger.info("Database connection closed.")
        except Exception as e:
            logger.warning(f"⚠️ Cleanup error: {str(e)}")

    def is_initialized(self) -> bool:
        """Check if retriever is properly initialized."""
        return self.query_engine is not None and self.engine is not None


# Simple usage example
if __name__ == "__main__":
    # Initialize retriever
    retriever = DatabaseRetriever(tables=["modules"])
    
    try:
        # Test some queries
        test_queries = [
          
            "List the basic topics will be learn with differential equation module"
        ]
        
        for query in test_queries:
            print(f"\n🔍 Query: {query}")
            result = retriever.query(query)
            
            if result["success"]:
                print(f"✅ SQL Generated: {result['sql_query']}")
                print(f"📋 Result: {result['result']}")
            else:
                print(f"❌ Error: {result['error']}")
                
    finally:
        # Clean up
        retriever.close()