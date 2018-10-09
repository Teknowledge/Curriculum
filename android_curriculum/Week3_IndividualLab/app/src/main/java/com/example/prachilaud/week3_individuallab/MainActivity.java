package com.example.prachilaud.week3_individuallab;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.View;
import android.widget.EditText;
import java.util.ArrayList;

/**
 * This is To-do app which keeps track of a list of to-do items and allows a user to
 * add new items. The key takeaway from this lab is the use of RecyclerView.
 */
public class MainActivity extends AppCompatActivity {

    TodoItemsAdapter aTodoAdapter;
    RecyclerView rvItems;
    EditText etNewItem;
    ArrayList<TodoItem> todoItems;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etNewItem = (EditText) findViewById(R.id.etNewItem);
        rvItems = (RecyclerView) findViewById(R.id.rvItems);

        // 1. Initialize the adapter with an empty to-do items list
        // 2. Attach the adapter to the recycler view
        // 3. Set a LayoutManager for positioning the items
        aTodoAdapter = new TodoItemsAdapter(this, todoItems);
        rvItems.setAdapter(aTodoAdapter);
        rvItems.setLayoutManager(new LinearLayoutManager(this));

    }

    /*
    When the 'Add' button is clicked, add a new to-do item to the adapter and reset the edit text
    to be blank. We use the second method to set onClick behavior for a button by defining the
    button's onClick attribute in the XML.
     */
    public void onAddItem(View view) {
        todoItems.add(new TodoItem(etNewItem.getText().toString()));
        aTodoAdapter.notifyDataSetChanged();
        etNewItem.setText("");
    }

}