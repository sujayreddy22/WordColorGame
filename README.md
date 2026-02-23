🎮 Word Color Game (Python + Tkinter + SQLite)
📌 Project Overview

The Word Color Game is a GUI-based desktop application developed using Python’s Tkinter library.

The objective of the game is to type the color of the displayed word, not the word text itself. The game runs on a 30-second timer and tracks player scores in real-time.

The project integrates SQLite database functionality to store high scores and display a leaderboard of top players.

🚀 Key Features

Real-time color recognition game

30-second countdown timer

Live score tracking

High score storage using SQLite

Top 5 leaderboard display

Dark mode toggle feature

Reset high scores functionality

Interactive Tkinter GUI

🛠 Technologies Used

Python

Tkinter (GUI Development)

SQLite (Database Management)

Event-Driven Programming

Randomization Logic

🧠 Concepts Implemented

GUI design using Tkinter

Event handling with key bindings

Countdown timer using after() method

SQLite database integration

Persistent data storage

SQL queries (INSERT, SELECT, DELETE)

Dynamic theme switching (Dark/Light mode)

🗄 Database Design

Database: highscores.db

Table: scores

Column	Type
id	INTEGER (Primary Key)
name	TEXT
score	INTEGER
▶️ How to Run the Project

Install Python (3.x recommended)

Navigate to project folder

Run the following command:

python word_color_game.py

Enter your name and press Enter to start the game

🎯 Game Objective

Type the color of the word, not the text itself.
For example, if the word says “Red” but appears in blue color, type:

blue

Score as many correct answers as possible within 30 seconds.

🔮 Future Enhancements

Difficulty levels

Sound effects

Online leaderboard integration

User login system

Game analytics dashboard

👨‍💻 Developer

Developed as part of a GUI-based Python application project demonstrating real-time interaction and database integration.