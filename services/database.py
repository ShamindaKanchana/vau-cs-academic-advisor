import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration from environment variables - JUST LIKE YOUR NODE.JS SETUP
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': int(os.getenv('DB_PORT', 3306)),  # Default MySQL port is 3306
    'charset': 'utf8mb4',
    'autocommit': True
}

# For SSL configuration (similar to your Node.js setup)
if os.getenv('DB_SSL') == 'true':
    DB_CONFIG['ssl'] = {
        'ssl': {'rejectUnauthorized': os.getenv('DB_SSL_REJECT_UNAUTHORIZED') == 'true'}
    }

# Create SQLAlchemy engine - THIS IS YOUR CONNECTION POOL
connection_string = f"mysql+pymysql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"

engine = create_engine(
    connection_string,
    pool_size=20,  # Similar to your connectionLimit: 20
    max_overflow=0,
    pool_recycle=3600,  # Recycle connections after 1 hour
    echo=False  # Set to True for debugging SQL queries
)

# Create Session factory - THIS IS HOW YOU GET CONNECTIONS
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Test the connection (similar to your pool.getConnection())
def test_connection():
    try:
        with engine.connect() as conn:
            print('✅ Successfully connected to MySQL database at', conn.engine.url)
        return True
    except Exception as e:
        print(f'⚠️ Database connection error: {e}')
        return False

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Test connection when this module is imported
if test_connection():
    print("✅ Database connection test passed")
else:
    print("❌ Database connection test failed")