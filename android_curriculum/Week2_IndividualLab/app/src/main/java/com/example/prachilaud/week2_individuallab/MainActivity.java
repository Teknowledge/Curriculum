package com.example.prachilaud.week2_individuallab;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {
    // By convention, declare all final static values at the top.
    private final int REQUEST_CODE = 20;

    ArrayList<String> todoItems;
    ArrayAdapter<String> aTodoAdapter;
    ListView lvItems;
    EditText etNewItem;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        /*
         Recall that to set up the array adapter for our list of to-do items, we need to
         pass in 3 things: context, item layout template, and data source.
         */
        todoItems = new ArrayList<String>();
        aTodoAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_list_item_1, todoItems);

        lvItems = (ListView) findViewById(R.id.lvItems);
        lvItems.setAdapter(aTodoAdapter);
        etNewItem = (EditText) findViewById(R.id.etNewItem);

        /*
         Whenever an item is long clicked, delete it from the to-do list by deleting it from
         the data source and notifying the adapter that the data has changed.
         */
        lvItems.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {
            @Override
            public boolean onItemLongClick(AdapterView<?> adapterView, View view, int i, long l) {
                todoItems.remove(i);
                aTodoAdapter.notifyDataSetChanged();
                return true;
            }
        });

        // Whenever an item is clicked, go to an edit activity for that item.
        lvItems.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                // We need to pass in the selected item's current text and position in the list
                // to the edit activity.
                Intent i = new Intent(MainActivity.this, EditItemActivity.class);
                i.putExtra("text", todoItems.get(position));
                i.putExtra("pos" , position);
                startActivityForResult(i, REQUEST_CODE);
            }
        });

    }

    /*
    Since we are starting an activity for result, we must have this method to deal with the
    result that comes back to the parent (current activity).
    Change the data source to reflect the given item's new text, and notify the adapter.
    */
    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        if (resultCode == RESULT_OK && requestCode == REQUEST_CODE) {
            todoItems.set(data.getExtras().getInt("pos"), data.getExtras().getString("newText"));
            aTodoAdapter.notifyDataSetChanged();
        }
    }

    /*
    When the 'Add' button is clicked, add a new to-do item to the adapter and reset the edit text
    to be blank. We use the second method to set onClick behavior for a button by defining the
    button's onClick attribute in the XML.
     */
    public void onAddItem(View view) {
        aTodoAdapter.add(etNewItem.getText().toString());
        etNewItem.setText("");
    }

}