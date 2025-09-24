from services.database import engine
from models.sql_models import Base
import time

def create_tables_with_retry(max_retries=3):
    """Try to create tables with retry logic for network issues"""
    for attempt in range(max_retries):
        try:
            Base.metadata.create_all(engine)
            print("✅ Tables created successfully in cloud database!")
            return True
        except Exception as e:
            print(f"⚠️ Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print("Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("❌ All attempts failed. Could not create tables.")
                return False

if __name__ == "__main__":
    create_tables_with_retry()