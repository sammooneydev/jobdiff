import sqlite3
from datetime import datetime
from pathlib import Path

from platformdirs import user_data_dir

#declaring db path using platform dirs lib (this means it will place in correct path depending on the os)
DB_PATH = Path(user_data_dir("jobdiff")) / "jobdiff.db"

"""
function that when called, establishes a connection with the sqlite3 database stored at the location pointed to by DB_PATH
"""
def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row #this allows for the reading of columns by name: row["title"]
    
    return conn

"""
function that when called, initialises the database tables "sources", and "jobs"
"""
def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS sources (
           id INTEGER PRIMARY KEY,
           url TEXT NOT NULL UNIQUE
        )          
    """)
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY,
            url TEXT NOT NULL UNIQUE,
            title TEXT NOT NULL,
            company TEXT,
            location TEXT,
            first_seen TEXT NOT NULL,
            is_new INTEGER NOT NULL DEFAULT 1
        )                 
    """)
    
    conn.commit()
    conn.close()