package com.example.thread_m13;

public interface TaskCallback {
    void onTaskStarted();
    void onTaskProgress(Integer progress);
    void onTaskFinished(String result);
}
