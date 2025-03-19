package com.example.thread_m13;

import android.os.AsyncTask;

public class CalculationTask extends AsyncTask<Integer, Integer, Long> {
    private TaskCallback callback;

    public CalculationTask(TaskCallback callback) {
        this.callback = callback;
    }

    @Override
    protected void onPreExecute() {
        callback.onTaskStarted();
    }

    @Override
    protected Long doInBackground(Integer... params) {
        int n = params[0];
        long result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
            publishProgress(i * 100 / n);  // Perkiraan progress
            try {
                Thread.sleep(50); // Simulasi proses panjang
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        return result;
    }

    @Override
    protected void onProgressUpdate(Integer... values) {
        callback.onTaskProgress(values[0]);
    }

    @Override
    protected void onPostExecute(Long result) {
        callback.onTaskFinished("Calculation Result: " + result);
    }
}
