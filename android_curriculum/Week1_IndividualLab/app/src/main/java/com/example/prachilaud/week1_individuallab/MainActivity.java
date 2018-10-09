package com.example.prachilaud.week1_individuallab;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import org.w3c.dom.Text;

public class MainActivity extends AppCompatActivity {

    // We declare all the views that we want to interact with at the top.
    Button btnSubmit;
    EditText etUserText;
    TextView tvDisplayText;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        // We "inflate the layout", which means that we set up this activity
        // with the views defined in the "activity_main" XML layout file.
        setContentView(R.layout.activity_main);

        // To get the view objects in our activity, we use findViewById, and then
        // cast the view that is returned to the appropriate type so that we can
        // access all of the specific methods we need.
        btnSubmit = (Button) findViewById(R.id.btnSubmit);
        etUserText = (EditText) findViewById(R.id.etUserText);
        tvDisplayText = (TextView) findViewById(R.id.tvDisplayText);

        // One way to set up onClick behavior for a button is to set up an
        // onClickListener.
        btnSubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // When this button is clicked, set the text view's text to be the user's
                // entered input, and reset the edit text box to be blank.
                tvDisplayText.setText(etUserText.getText());
                etUserText.setText("");
            }
        });
    }
}
