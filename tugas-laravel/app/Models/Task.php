<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Task extends Model
{
    use HasFactory;  // This lets you create fake tasks for testing

    protected $table = 'tasks';  // Tells Laravel which table this model manages

    // These fields cannot be mass-assigned (filled all at once)
    // This is a security feature

    // Add this to specify which fields can be mass-assigned
    protected $fillable = [
        'title',
        'desc',
        'status',
        'due_date',
        'user_id'  // Make sure this is included
    ];

    // Define the relationship with User
    public function user()
    {
        return $this->belongsTo(User::class);
    }
}
