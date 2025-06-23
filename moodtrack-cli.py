import json
import os
from datetime import datetime

DATA_FILE = "mood_log.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_entry():
    mood = input("How are you feeling today? (e.g., happy, sad, anxious): ").strip()
    entry = input("Write a short journal entry about your day: ").strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_data()
    data.append({"timestamp": timestamp, "mood": mood, "entry": entry})
    save_data(data)
    print("\n✅ Entry saved!")

def view_entries():
    data = load_data()
    if not data:
        print("📭 No entries found.")
        return

    for entry in data:
        print("\n🗓️", entry["timestamp"])
        print("Mood:", entry["mood"])
        print("Entry:", entry["entry"])
        print("-" * 40)

def show_menu():
    while True:
        print("\n📓 MoodTrack Menu")
        print("1. Add a new entry")
        print("2. View mood history")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("👋 Goodbye. Take care!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    show_menu()
