import json
import os

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteManager:
    def __init__(self, notes_file):
        self.notes_file = notes_file
        self.notes = self.load_notes()

    def load_notes(self):
        if os.path.exists(self.notes_file):
            with open(self.notes_file, 'r') as f:
                return json.load(f)
        return []

    def save_notes(self):
        with open(self.notes_file, 'w') as f:
            json.dump([note.__dict__ for note in self.notes], f)

    def create_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)
        self.save_notes()

    def list_notes(self):
        for i, note in enumerate(self.notes):
            print(f"{i+1}. {note.title}")

    def view_note(self, index):
        if 1 <= index <= len(self.notes):
            note = self.notes[index - 1]
            print(f"Title: {note.title}")
            print(f"Content: {note.content}")
        else:
            print("Invalid note index")

    def edit_note(self, index, new_title, new_content):
        if 1 <= index <= len(self.notes):
            self.notes[index - 1].title = new_title
            self.notes[index - 1].content = new_content
            self.save_notes()
            print("Note edited successfully")
        else:
            print("Invalid note index")

    def delete_note(self, index):
        if 1 <= index <= len(self.notes):
            del self.notes[index - 1]
            self.save_notes()
            print("Note deleted successfully")
        else:
            print("Invalid note index")

def main():
    notes_manager = NoteManager('notes.json')

    while True:
        print("\n1. Create a note")
        print("2. List all notes")
        print("3. View a note")
        print("4. Edit a note")
        print("5. Delete a note")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            notes_manager.create_note(title, content)
        elif choice == '2':
            notes_manager.list_notes()
        elif choice == '3':
            index = int(input("Enter note index: "))
            notes_manager.view_note(index)
        elif choice == '4':
            index = int(input("Enter note index: "))
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            notes_manager.edit_note(index, new_title, new_content)
        elif choice == '5':
            index = int(input("Enter note index: "))
            notes_manager.delete_note(index)
        elif choice == '6':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()