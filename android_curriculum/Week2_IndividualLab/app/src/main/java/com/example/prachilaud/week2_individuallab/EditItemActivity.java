package com.example.prachilaud.week2_individuallab;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;

public class EditItemActivity extends AppCompatActivity {

    EditText etEditedItem;
    Integer pos;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_edit_item);

        // Set the edit text's text to be the current to-do item description. Set it to be
        // highlighted.
        etEditedItem = (EditText) findViewById(R.id.etEditedItem);
        etEditedItem.setText(getIntent().getStringExtra("text"));
        etEditedItem.setSelection(getIntent().getStringExtra("text").length());

        pos = getIntent().getIntExtra("pos",0);
    }

    /*
    This method will be called when the 'Save' button is clicked. At this time, we want to
    return to the to-do list (MainActivity) so we finish this activity. However, we need to return
    a result (the new to-do item's text), so we use an Intent to add the parameters (the new
    text and the item's position in the list), and set that to be the result of this activity
    before it finishes.
     */
    public void onSave(View view) {
        EditText etEditedItem = (EditText) findViewById(R.id.etEditedItem);
        Intent data = new Intent();
        data.putExtra("newText", etEditedItem.getText().toString());
        data.putExtra("pos", pos);
        setResult(RESULT_OK, data);
        finish();
    }

}