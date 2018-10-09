package com.example.prachilaud.week5_grouplab;

import android.app.DialogFragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.WindowManager;
import android.widget.Button;

/**
 * This class is a Dialog Fragment that pops up when we want to show the user a MadLib. The
 * MadLib string is passed in when the Fragment is instantiated, and is displayed to the user.
 * The user then is expected to select one of two buttons, each of which indicates positive or
 * negative reaction. Based on the user reaction, we then call a MadLibReactionListener method and
 * pass it the string that the user saw. We expect the parent Activity to implement this listener.
 */

public class MadLibDialogFragment extends DialogFragment {

    // Member view fields
    Button btnPos;
    Button btnNeg;

    /**
     * Setting up a listener interface for what to do if the user has a positive reaction or a
     * negative reaction. This listener interface will then be implemented by the parent Activity,
     * so that it can behave based on the information passed to it from this Fragment.
     */
    public interface MadLibReactionListener {
        void onPosReaction(String text);
        void onNegReaction(String text);
    }

    public MadLibDialogFragment() {
        // Empty constructor is required for DialogFragment
        // Make sure not to add arguments to the constructor
        // Use `newInstance` instead as shown below
    }

    /*
    Instantiate a MadLibDialogFragment. This takes in the string that
    we will be showing, and sets it as an argument.
     */
    public static MadLibDialogFragment newInstance(String title) {
        MadLibDialogFragment frag = new MadLibDialogFragment();
        Bundle args = new Bundle();
        args.putString("title", title);
        frag.setArguments(args);
        return frag;
    }

    /*
    Inflate the view, similar to how we do it for other components.
     */
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        return inflater.inflate(R.layout.mad_lib_fragment, container);
    }

    @Override
    public void onViewCreated(View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);

        // Get fields from view
        btnPos = (Button) view.findViewById(R.id.btnPos);
        btnNeg = (Button) view.findViewById(R.id.btnNeg);

        // Fetch arguments from bundle and set title
        final String title = getArguments().getString("title", "Enter Name");
        getDialog().setTitle(title);

        /*
        We set up the listener here; since we are expecting the parent activity to implement this
        listener, we can cast it to the MadLibReactionListener, and then call those listener
        methods when the user selects a button.
         */
        final MadLibReactionListener listener = (MadLibReactionListener) getActivity();
        btnPos.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                listener.onPosReaction(title);
            }
        });
        btnNeg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                listener.onNegReaction(title);
            }
        });

    }


}
