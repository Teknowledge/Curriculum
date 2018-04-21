package com.example.prachilaud.week5_grouplab;

import android.app.FragmentManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import java.util.ArrayList;
import java.util.Random;

/**
 * The MainActivity for this app displays a button, which when clicked, opens a
 * MadLibDialogFragment, which displays a randomly generated mad lib.
 * This class also implements two methods defined in the MadLibReactionListener so that it
 * can communicate with its child fragment.
 */
public class MainActivity extends AppCompatActivity
        implements MadLibDialogFragment.MadLibReactionListener{

    Button btnShowLibs;
    String[] nouns = {"bear", "cake", "lamp"};
    String[] verbs = {"ran", "ate", "talked"};
    String[] adj = {"purple", "spiky", "weird"};
    int numPosReactions;
    int numNegReactions;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Set up button to show mad libs.
        btnShowLibs = (Button) findViewById(R.id.btnShowLibs);
        btnShowLibs.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                showLibs();
            }
        });
    }

    /**
     * Generate a random mad lib string. Set up the fragment manager, instantiate the
     * fragment, and show it.
     */
    private void showLibs() {
        Random rand = new Random();
        String text = "The " + nouns[rand.nextInt(nouns.length)] + " " + verbs[rand.nextInt(verbs.length)]
                + " the " + adj[rand.nextInt(adj.length)] + " " + nouns[rand.nextInt(nouns.length)] + ".";
        FragmentManager fm = getFragmentManager();
        MadLibDialogFragment dialog =
                MadLibDialogFragment.newInstance(text);
        dialog.show(fm, "mad_lib_fragment");
    }

    /*
    Implementing the MadLibReactionsListener methods
     */

    @Override
    public void onPosReaction(String text) {
        numPosReactions += 1;
    }

    @Override
    public void onNegReaction(String text) {
        numNegReactions += 1;
    }
}
