package com.example.prachilaud.week2_grouplab;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.Collection;

public class MainActivity extends AppCompatActivity {

    ListView lvItems;
    ArrayList<String> foodItems = new ArrayList<String>();
    ArrayAdapter<String> adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Set up our list of food items (data).
        foodItems.add("pizza");
        foodItems.add("chocoloate cake");
        foodItems.add("pasta");
        foodItems.add("ice cream");

        lvItems = (ListView) findViewById(R.id.lvItems);

        // Set up an adapter. The ArrayAdapter takes in 3 arguments: context (we pass in
        // the current Activity instance), layout for the list items (we use the built-in
        // simple list item for just text), and the data source (list of food items).
        adapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, foodItems);
        lvItems.setAdapter(adapter);

        // We can set an onItemClickListener to control the behavior of our listView when
        // an item on the list is clicked.
        lvItems.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                // To start a new Activity, we need to create an Intent that takes in the
                // current instance of this Activity, and the child Activity's class.
                // We use putExtra to add parameters to this intent before starting the new
                // activity.
                Intent intent = new Intent(MainActivity.this, ItemActivity.class);
                intent.putExtra("foodItem", ((TextView) view).getText());
                startActivity(intent);
            }
        });
    }
}
