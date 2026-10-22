
# Dictionary Application using Hash Tables
# Collision Resolution: Separate Chaining

class Dictionary:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, word):
        return sum(ord(char) for char in word.lower()) % self.size

    # Add a word and its meaning
    def insert(self, word, meaning):
        index = self.hash_function(word)

        for item in self.table[index]:
            if item[0] == word.lower():
                item[1] = meaning
                print("Meaning updated successfully!")
                return

        self.table[index].append([word.lower(), meaning])
        print("Word added successfully!")

    # Search for a word
    def search(self, word):
        index = self.hash_function(word)

        for item in self.table[index]:
            if item[0] == word.lower():
                print(f"Meaning of {word}: {item[1]}")
                return

        print("Word not found in dictionary.")

    # Delete a word
    def delete(self, word):
        index = self.hash_function(word)

        for item in self.table[index]:
            if item[0] == word.lower():
                self.table[index].remove(item)
                print("Word deleted successfully!")
                return

        print("Word not found in dictionary.")

    # Display all words
    def display(self):
        print("\n--- Dictionary Words ---")
        found = False

        for index, chain in enumerate(self.table):
            for word, meaning in chain:
                print(f"{word}: {meaning}")
                found = True

        if not found:
            print("Dictionary is empty.")


# Main program
dictionary = Dictionary()

while True:
    print("\n===== Dictionary Application =====")
    print("1. Add Word")
    print("2. Search Word")
    print("3. Delete Word")
    print("4. Display Dictionary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("Enter word: ").strip()
        meaning = input("Enter meaning: ").strip()

        if word and meaning:
            dictionary.insert(word, meaning)
        else:
            print("Word and meaning cannot be empty.")

    elif choice == "2":
        word = input("Enter word to search: ").strip()
        dictionary.search(word)

    elif choice == "3":
        word = input("Enter word to delete: ").strip()
        dictionary.delete(word)

    elif choice == "4":
        dictionary.display()

    elif choice == "5":
        print("Thank you for using the Dictionary Application!")
        break

    else:
        print("Invalid choice. Please try again.")
