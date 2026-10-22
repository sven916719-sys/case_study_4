
# Dictionary Application Using Hash Tables

## 1. Introduction
This project implements a simple dictionary application using a hash table in Python. It stores words and their meanings and allows users to add, search, delete, and display words.

## 2. Objectives
- To understand the concept of hash tables.
- To store words and meanings efficiently.
- To perform insertion, searching, and deletion operations.
- To handle collisions using separate chaining.

## 3. Description
The Dictionary Application uses a hash function to calculate the index for each word in a hash table. Words with the same index are stored in a list at that position.

This collision resolution technique is called **Separate Chaining**.

## 4. Features
- Add new words with meanings.
- Search for a word and display its meaning.
- Update the meaning of an existing word.
- Delete a word from the dictionary.
- Display all stored words and meanings.
- Handle hash collisions using separate chaining.

## 5. Technologies Used
- Programming Language: Python
- Data Structure: Hash Table
- Collision Resolution: Separate Chaining
- IDE: Visual Studio Code

## 6. How to Run the Project

1. Install Python on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

```bash
python dictionary.py
```

## 7. Operations and Time Complexity

Let n be the number of stored words and m be the size of the hash table.

| Operation | Average Time Complexity |
|---|---|
| Insert | O(1) |
| Search | O(1) |
| Delete | O(1) |
| Display | O(n + m) |

In the worst case, insertion, searching, and deletion can take O(n) time if many words map to the same index.

## 8. Sample Output

===== Dictionary Application =====
1. Add Word
2. Search Word
3. Delete Word
4. Display Dictionary
5. Exit

Enter your choice: 1
Enter word: apple
Enter meaning: A fruit
Word added successfully!

Enter your choice: 2
Enter word to search: apple
Meaning of apple: A fruit

## 9. Advantages
- Fast searching and insertion on average.
- Efficient storage of word-meaning pairs.
- Collision handling prevents words from being lost.
- Simple and easy-to-use menu-driven application.

## 10. Conclusion
This project demonstrates how hash tables can be used to build a dictionary application. It provides efficient insertion, searching, updating, and deletion of words using hashing and separate chaining.
