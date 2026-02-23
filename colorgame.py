import tkinter
import random
import sqlite3
from tkinter import messagebox

# Setup SQLite
conn = sqlite3.connect('highscores.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS scores (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)")
conn.commit()

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 30
dark_mode = False

def get_high_score():
    cursor.execute("SELECT MAX(score) FROM scores")
    result = cursor.fetchone()[0]
    return result if result else 0

def get_top_scores():
    cursor.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 5")
    return cursor.fetchall()

def startGame(event):
    global timeleft, score
    if timeleft == 30:
        score = 0
        scoreLabel.config(text="Score: 0")
        updateHighScoreDisplay()
        countdown()
    nextColour()

def nextColour():
    global score, timeleft
    if timeleft > 0:
        e.focus_set()
        typed = e.get().lower()
        correct = label.cget("fg").lower()
        if typed == correct:
            score += 1
            scoreLabel.config(text="Score: " + str(score))
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        updateHighScoreDisplay()

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
    else:
        name = nameEntry.get().strip()
        prev_high = get_high_score()
        if name:
            cursor.execute("INSERT INTO scores (name, score) VALUES (?, ?)", (name, score))
            conn.commit()
        if score > prev_high:
            messagebox.showinfo("🏆 New High Score!", f"🎉 Congrats {name}!\nYou set a new high score: {score}!")
        else:
            messagebox.showinfo("Game Over", f"Time's up!\nYour score: {score}\nHigh Score: {prev_high}")
        showLeaderboard()
        updateHighScoreDisplay()

def updateHighScoreDisplay():
    high = get_high_score()
    highScoreLabel.config(text=f"High Score: {high}")

def resetHighScore():
    if messagebox.askyesno("Confirm Reset", "Are you sure you want to reset the high scores?"):
        cursor.execute("DELETE FROM scores")
        conn.commit()
        updateHighScoreDisplay()
        messagebox.showinfo("Reset Done", "High scores have been reset to 0.")

def showLeaderboard():
    top_scores = get_top_scores()
    msg = "🏅 Top 5 Players:\n\n"
    for idx, (name, sc) in enumerate(top_scores, 1):
        msg += f"{idx}. {name} - {sc}\n"
    messagebox.showinfo("Leaderboard", msg)

def toggleTheme():
    global dark_mode
    dark_mode = not dark_mode
    bg = "#121212" if dark_mode else "#f0f0f0"
    fg = "white" if dark_mode else "black"
    highlight = "cyan" if dark_mode else "blue"

    root.configure(bg=bg)
    for widget in root.winfo_children():
        if isinstance(widget, (tkinter.Label, tkinter.Button)):
            widget.configure(bg=bg, fg=fg)
        if isinstance(widget, tkinter.Entry):
            widget.configure(bg="gray20" if dark_mode else "white", fg=fg, insertbackground=fg)
    highScoreLabel.configure(fg=highlight)
    themeBtn.configure(bg=bg, fg=fg)

# GUI Setup
root = tkinter.Tk()
root.title("🎮 WORD COLOR GAME")
root.geometry("430x400")
root.configure(bg="#f0f0f0")

tkinter.Label(root, text="Enter your name:", font=('Helvetica', 10), bg="#f0f0f0").pack()
nameEntry = tkinter.Entry(root)
nameEntry.pack()

tkinter.Label(root, text="Type the *COLOR* of the word, not the word itself!",
              font=('Helvetica', 12, 'italic'), bg="#f0f0f0", fg="darkgreen").pack(pady=5)

scoreLabel = tkinter.Label(root, text="Press Enter to start", font=('Helvetica', 12), bg="#f0f0f0")
scoreLabel.pack()

highScoreLabel = tkinter.Label(root, text=f"High Score: {get_high_score()}",
                               font=('Helvetica', 12, 'bold'), fg='blue', bg="#f0f0f0")
highScoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12), bg="#f0f0f0")
timeLabel.pack(pady=5)

label = tkinter.Label(root, font=('Helvetica', 60), bg="#f0f0f0")
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack(pady=5)
e.focus_set()

tkinter.Button(root, text="Reset High Score", fg="red", command=resetHighScore).pack(pady=10)

themeBtn = tkinter.Button(root, text="🌙 Toggle Theme", command=toggleTheme)
themeBtn.pack()

root.mainloop()
conn.close()
