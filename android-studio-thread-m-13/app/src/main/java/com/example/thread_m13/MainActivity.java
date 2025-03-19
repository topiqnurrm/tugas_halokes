package com.example.thread_m13;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.TextView;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.view.View;
import android.widget.Button;
import com.example.thread_m13.ImageProcessingTask;

import android.widget.ImageView;

public class MainActivity extends AppCompatActivity implements TaskCallback {
    private TextView statusText;
    private ProgressBar progressBar;
    private Button startButton;
    private ImageView processedImageView; // Tambahkan referensi ke ImageView

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        statusText = findViewById(R.id.statusText);
        progressBar = findViewById(R.id.progressBar);
        startButton = findViewById(R.id.startButton);
        processedImageView = findViewById(R.id.processedImageView); // Ambil referensi ke ImageView

        // Listener untuk tombol Start Download
        startButton.setOnClickListener(v -> {
            hideImageView(); // Sembunyikan gambar saat tombol ini ditekan
            new DownloadTask(this).execute("https://example.com/largefile.zip");
        });

        // Listener untuk tombol Start Network Task
        findViewById(R.id.networkButton).setOnClickListener(v -> {
            hideImageView(); // Sembunyikan gambar saat tombol ini ditekan
            new NetworkTask(this).execute("https://jsonplaceholder.typicode.com/posts/1");
        });

        // Listener untuk tombol Start Calculation Task
        findViewById(R.id.calculationButton).setOnClickListener(v -> {
            hideImageView(); // Sembunyikan gambar saat tombol ini ditekan
            new CalculationTask(this).execute(20);  // Hitung faktorial dari 20
        });

        // Listener untuk tombol Start Image Processing Task
        findViewById(R.id.imageProcessingButton).setOnClickListener(v -> {
            Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.drawable.kunjungan);
            new ImageProcessingTask(this, processedImageView).execute(bitmap);
        });
    }

// Metode untuk menyembunyikan ImageView
private void hideImageView() {
    processedImageView.setVisibility(View.GONE); // Atur ImageView menjadi tidak terlihat
}

//    @Override
//    public void onTaskStarted() {
//        progressBar.setVisibility(View.VISIBLE);
//        statusText.setText("prosess...");
//        startButton.setEnabled(false);
//    }

    @Override
    public void onTaskProgress(Integer progress) {
        progressBar.setProgress(progress);
        statusText.setText("Progress: " + progress + "%");
    }

//    @Override
//    public void onTaskFinished(String result) {
//        progressBar.setVisibility(View.GONE);
////        statusText.setText("Download Complete: " + result);
//        statusText.setText(result);
//        startButton.setEnabled(true);
//    }

    @Override
    public void onTaskStarted() {
        progressBar.setVisibility(View.VISIBLE);
        statusText.setText("prosess...");

        // Sembunyikan semua tombol saat proses loading
        startButton.setVisibility(View.GONE);
        findViewById(R.id.networkButton).setVisibility(View.GONE);
        findViewById(R.id.imageProcessingButton).setVisibility(View.GONE);
        findViewById(R.id.startButton).setVisibility(View.GONE);
        findViewById(R.id.networkButton).setVisibility(View.GONE);
        findViewById(R.id.calculationButton).setVisibility(View.GONE);
        findViewById(R.id.imageProcessingButton).setVisibility(View.GONE);
    }

    @Override
    public void onTaskFinished(String result) {
        progressBar.setVisibility(View.GONE);

        // Tampilkan hasil
        statusText.setText(result);

        // Kembalikan visibilitas tombol setelah selesai
        startButton.setVisibility(View.VISIBLE);
        findViewById(R.id.networkButton).setVisibility(View.VISIBLE);
        findViewById(R.id.imageProcessingButton).setVisibility(View.VISIBLE);
        findViewById(R.id.startButton).setVisibility(View.VISIBLE);
        findViewById(R.id.networkButton).setVisibility(View.VISIBLE);
        findViewById(R.id.calculationButton).setVisibility(View.VISIBLE);
        findViewById(R.id.imageProcessingButton).setVisibility(View.VISIBLE);
    }
}

