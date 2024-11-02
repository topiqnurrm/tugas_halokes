package com.example.thread_m13;
import android.os.AsyncTask;

public class DownloadTask extends AsyncTask<String, Integer, String> {
    private TaskCallback callback;

    public DownloadTask(TaskCallback callback) {
        this.callback = callback;
    }

    @Override
    protected void onPreExecute() {
        callback.onTaskStarted();
    }

    @Override
    protected String doInBackground(String... params) {
        String url = params[0];
        // Simulasi proses download
        try {
            for (int i = 0; i <= 100; i += 10) {
                Thread.sleep(500); // Simulasi waktu untuk tiap 10% progress
                publishProgress(i);
            }
            return "File berhasil diunduh dari " + url;
        } catch (InterruptedException e) {
            return "Download gagal: " + e.getMessage();
        }
    }

    @Override
    protected void onProgressUpdate(Integer... values) {
        callback.onTaskProgress(values[0]);
    }

    @Override
    protected void onPostExecute(String result) {
        callback.onTaskFinished(result);
    }
}
