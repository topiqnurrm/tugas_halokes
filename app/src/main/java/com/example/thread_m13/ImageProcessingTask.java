package com.example.thread_m13;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.widget.ImageView;
import android.view.View;

public class ImageProcessingTask extends AsyncTask<Bitmap, Void, Bitmap> {
    private TaskCallback callback;
    private ImageView imageView; // Tambahkan variabel ImageView

    public ImageProcessingTask(TaskCallback callback, ImageView imageView) {
        this.callback = callback;
        this.imageView = imageView; // Inisialisasi ImageView
    }

    @Override
    protected void onPreExecute() {
        callback.onTaskStarted();
    }

    @Override
    protected Bitmap doInBackground(Bitmap... params) {
        Bitmap bitmap = params[0];
        if (bitmap != null) {
            return Bitmap.createScaledBitmap(bitmap, 100, 100, false);
        } else {
            return null;
        }
    }

    @Override
    protected void onPostExecute(Bitmap result) {
        if (result != null) {
            imageView.setImageBitmap(result); // Tampilkan gambar yang sudah diproses
            imageView.setVisibility(View.VISIBLE); // Pastikan ImageView terlihat
            callback.onTaskFinished("Image processed successfully");
        } else {
            callback.onTaskFinished("Failed to process image"); // Jika gagal
        }
    }
}
