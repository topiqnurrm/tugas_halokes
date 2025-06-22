<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Task</title>
</head>
<body>
    <h2>Create New Task</h2>
    
    <form action="{{ url('/tasks') }}" method="POST">
        <!-- CSRF Token -->
        @csrf

        <!-- Title Input -->
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br><br>

        <!-- Description Input -->
        <label for="desc">Description:</label>
        <textarea id="desc" name="desc"></textarea>
        <br><br>

        <!-- Status Input -->
        <label for="status">Status:</label>
        <input type="text" id="status" name="status" required>
        <br><br>

        <!-- Due Date Input -->
        <label for="due_date">Due Date:</label>
        <input type="date" id="due_date" name="due_date">
        <br><br>

        <!-- Submit Button -->
        <button type="submit">Create Task</button>
    </form>
</body>
</html>
