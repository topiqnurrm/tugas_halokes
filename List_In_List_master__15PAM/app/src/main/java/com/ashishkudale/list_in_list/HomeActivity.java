package com.ashishkudale.list_in_list;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.widget.Switch;
import android.widget.CompoundButton;

import com.ashishkudale.list_in_list.adapters.SubjectAdapter;
import com.ashishkudale.list_in_list.models.Chapter;
import com.ashishkudale.list_in_list.models.Subject;

import java.util.ArrayList;

public class HomeActivity extends AppCompatActivity {

    private RecyclerView rvSubject;
    private SubjectAdapter subjectAdapter;
    private ArrayList<Subject> subjects;
    private Switch switchLayout;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Initialize views
        rvSubject = findViewById(R.id.rvSubject);
        switchLayout = findViewById(R.id.switchLayout);

        // Prepare data and set up adapter
        subjects = prepareData();
        subjectAdapter = new SubjectAdapter(subjects, HomeActivity.this);

        // Set up default RecyclerView layout manager (vertical)
        LinearLayoutManager manager = new LinearLayoutManager(this);
        manager.setOrientation(LinearLayoutManager.VERTICAL);
        rvSubject.setLayoutManager(manager);
        rvSubject.setAdapter(subjectAdapter);

        // Set up a listener for the Switch to toggle between vertical and horizontal layout
        switchLayout.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                // Change the RecyclerView layout based on Switch state
                if (isChecked) {
                    // Switch to horizontal layout
                    LinearLayoutManager horizontalManager = new LinearLayoutManager(HomeActivity.this);
                    horizontalManager.setOrientation(LinearLayoutManager.HORIZONTAL);
                    rvSubject.setLayoutManager(horizontalManager);
                } else {
                    // Switch to vertical layout
                    LinearLayoutManager verticalManager = new LinearLayoutManager(HomeActivity.this);
                    verticalManager.setOrientation(LinearLayoutManager.VERTICAL);
                    rvSubject.setLayoutManager(verticalManager);
                }
            }
        });
    }

    private void initComponents() {
        rvSubject = findViewById(R.id.rvSubject);
    }

    private ArrayList<Subject> prepareData() {
        ArrayList<Subject> subjects = new ArrayList<Subject>();

        Subject physics = new Subject();
        physics.id = 1;
        physics.subjectName = "Bahasa Pemrograman";
        physics.chapters = new ArrayList<Chapter>();

        Chapter chapter1 = new Chapter();
        chapter1.id = 1;
        chapter1.chapterName = "Java";
        chapter1.imageUrl = "https://miro.medium.com/v2/resize:fit:1400/1*iIXOmGDzrtTJmdwbn7cGMw.png";

        Chapter chapter2 = new Chapter();
        chapter2.id = 2;
        chapter2.chapterName = "Python";
        chapter2.imageUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/640px-Python.svg.png";

        Chapter chapter3 = new Chapter();
        chapter3.id = 3;
        chapter3.chapterName = "PHP";
        chapter3.imageUrl = "https://raw.githubusercontent.com/github/explore/ccc16358ac4530c6a69b1b80c7223cd2744dea83/topics/php/php.png";

        Chapter chapter4 = new Chapter();
        chapter4.id = 4;
        chapter4.chapterName = "HTML";
        chapter4.imageUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/800px-HTML5_logo_and_wordmark.svg.png";

        physics.chapters.add(chapter1);
        physics.chapters.add(chapter2);
        physics.chapters.add(chapter3);
        physics.chapters.add(chapter4);

        Subject chem = new Subject();
        chem.id = 2;
        chem.subjectName = "Desain Grafis";
        chem.chapters = new ArrayList<Chapter>();

        Chapter chapter6 = new Chapter();
        chapter6.id = 6;
        chapter6.chapterName = "Canva";
        chapter6.imageUrl = "https://firebearstudio.com/blog/wp-content/uploads/2022/11/1A6kkoOVJVpXPWewg8axc5w.png";

        Chapter chapter7 = new Chapter();
        chapter7.id = 7;
        chapter7.chapterName = "Figma";
        chapter7.imageUrl = "https://spin.atomicobject.com/wp-content/uploads/Figma-Image.jpg";

        Chapter chapter8 = new Chapter();
        chapter8.id = 8;
        chapter8.chapterName = "Adobe";
        chapter8.imageUrl = "https://upload.wikimedia.org/wikipedia/commons/1/1c/Adobe_Express_logo_RGB_1024px.png";

        Chapter chapter9 = new Chapter();
        chapter9.id = 9;
        chapter9.chapterName = "Corel Draw";
        chapter9.imageUrl = "https://img.utdstc.com/icon/62f/136/62f1369d2e49fdcdf4989596eefad984413b9f39a8edcb775ceda2ad736e686c:200";

        chem.chapters.add(chapter6);
        chem.chapters.add(chapter7);
        chem.chapters.add(chapter8);
        chem.chapters.add(chapter9);


        subjects.add(physics);
        subjects.add(chem);

        return subjects;
    }
}
