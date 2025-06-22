<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>To Do List</title>
  <style>
    table {
      width: 100%;
      border-collapse: collapse;
    }
    table, th, td {
      border: 1px solid black;
    }
    th, td {
      padding: 10px;
      text-align: left;
    }
    th {
      background-color: #f2f2f2;
    }
  </style>
</head>
<body>
  <h1>User To-Do List</h1>
  <table>
    <thead>
      <tr>
        <th>Title</th>
        <th>Description</th>
        <th>Due Date</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      @foreach($allUserTasks as $task)
        <tr>
          <td>{{ $task->title }}</td> <!-- Task title -->
          <td>{{ $task->desc }}</td> <!-- Task description -->
          <td>{{ $task->due_date }}</td> <!-- Task due date -->
          <td>
            <!-- Edit link -->
            <a href="{{ route('tasks.edit', $task->id) }}">Edit</a>

            <!-- Delete link with a form -->
            <form action="{{ route('tasks.destroy', $task->id) }}" method="POST" style="display:inline;">
              @csrf
              @method('DELETE')
              <button type="submit" onclick="return confirm('Are you sure you want to delete this task?')">Delete</button>
            </form>
          </td>
        </tr>
      @endforeach
    </tbody>
  </table>
</body>
</html>
