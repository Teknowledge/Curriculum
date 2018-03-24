package com.example.prachilaud.lab1;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    // We declare all the views that we want to interact with at the top.
    Button btnHelloWord;
    Button btnEnterText;
    EditText etUserText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // We "inflate the layout", which means that we set up this activity
        // with the views defined in the "activity_main" XML layout file.
        setContentView(R.layout.activity_main);

        // To get the view objects in our activity, we use findViewById, and then
        // cast the view that is returned to the appropriate type so that we can
        // access all of the specific methods we need.
        btnHelloWord = (Button) findViewById(R.id.btnHelloWorld);
        btnEnterText = (Button) findViewById(R.id.btnEnterText);
        etUserText = (EditText) findViewById(R.id.etUserText);

        // One way to set up onClick behavior for a button is to set up an
        // onClickListener.
        btnHelloWord.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // When this button is clicked, make a toast that says Hello World.
                Toast.makeText(getApplicationContext(), "Hello World!", Toast.LENGTH_LONG).show();
            }
        });

        btnEnterText.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // When this button is clicked, make a toast that displays the text entered
                // into the editText box.
                Toast.makeText(getApplicationContext(), etUserText.getText(), Toast.LENGTH_LONG).show();
            }
        });
    }
}
