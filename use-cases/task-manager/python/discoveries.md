# Task Manager Assessment - Part 1

## Project Structure & Tech Stack
* *Language:* Python 3.11+
* *Requirements:* None (Standard Library only).
* *Main Components:*
  - cli.py: User Interface / Entry Point.
  - models.py: Data structure (The Task class).
  - storage.py: Data persistence (saving tasks).
  - app.py: Core logic for managing tasks.

## My Observations
The project is modular. I initially thought it might be one big file, but it separates the data (models.py) from the commands (cli.py).
## Part 2: Feature Location
* *Feature Found:* "Create a Task"
* *UI Location:* I found the 'create' command in cli.py.
* *Logic Location:* The actual code that builds the task is in app.py on *Line 10* (def create_task).
* *Observation:* The create_task function is responsible for taking the user's input (like title and description) and turning it into a Task object.
## Part 3: Domain Model Discovery
* *The Task Object:* Every task has an ID, Title, Description, Priority, Due Date, and Tags.
* *Statuses:* Tasks can be TODO, IN_PROGRESS, or DONE.
* *Logic Check:* I noticed that tasks are given a unique ID using uuid, which ensures no two tasks have the same number.
