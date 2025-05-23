from database import SessionLocal
from models import Prompt

# Create a new DB session
session = SessionLocal()

# Fetch all entries from the Prompt table
entries = session.query(Prompt).all()

# Print the entries
if not entries:
    print("❌ No entries found in the database.")
else:
    print(f"✅ Found {len(entries)} entries in the database:\n")
    for entry in entries:
        print(f"📝 Query: {entry.query}\n")
        print(f"🟢 Casual Response:\n{entry.casual_response}\n")
        print(f"🔵 Formal Response:\n{entry.formal_response}\n")
        print(f"🕒 Created At: {entry.created_at}\n")
        print("─" * 50)

# Close the session
session.close()
