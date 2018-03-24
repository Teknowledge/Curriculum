package com.example.prachilaud.week2_grouplab;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class ItemActivity extends AppCompatActivity {

    TextView tvItem;
    Button btnBack;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_item);

        tvItem = (TextView) findViewById(R.id.tvItem);
        btnBack = (Button) findViewById(R.id.btnBack);

        // Access the extra params passed through an Intent in this way.
        String item = getIntent().getStringExtra("foodItem");
        tvItem.setText(item);


        btnBack.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                onSubmit(view);
            }
        });
    }

    // Closes the activity and returns to first screen
    public void onSubmit(View v) {
        this.finish();
    }
}
