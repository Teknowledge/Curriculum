package com.example.prachilaud.week3_individuallab;

import android.content.Context;
import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.List;

/**
 * Here, we create an adapter for our to-do list that extends from the basic
 * RecyclerView.Adapter. The adapter's role is to convert an object at a position into a
 * list row item to be inserted into the list.
 * The adapter requires the existence of the "ViewHolder" class. A ViewHolder object
 * describes and provides access to all the views within each item row.
 */
public class TodoItemsAdapter extends
        RecyclerView.Adapter<TodoItemsAdapter.ViewHolder> {

    // Member variables for this class - we use the prefix 'm' for all of them.
    List<TodoItem> mTodoItems;

    // Pass in the to-do items array into the constructor
    public TodoItemsAdapter(Context context, List<TodoItem> items) {
        mTodoItems = items;
    }

    // Usually involves inflating a layout from XML and returning the view holder
    @Override
    public TodoItemsAdapter.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        Context context = parent.getContext();
        LayoutInflater inflater = LayoutInflater.from(context);

        // Inflate the custom layout
        View contactView = inflater.inflate(R.layout.todo_item, parent, false);

        // Return a new holder instance
        ViewHolder viewHolder = new ViewHolder(contactView);
        return viewHolder;
    }

    // Involves using the holder to set the view attributes of the item based on the data
    @Override
    public void onBindViewHolder(TodoItemsAdapter.ViewHolder viewHolder, int position) {
        // Get the data model based on position
        TodoItem item = mTodoItems.get(position);

        // Set item views based on your views and data model
        TextView textView = viewHolder.tvItemDesc;
        textView.setText(item.getItem());
    }

    // Returns the total count of items in the list
    @Override
    public int getItemCount() {
        return mTodoItems.size();
    }

    /*
    Provide a direct reference to each of the views within a data item
    Used to cache the views within the item layout for fast access.
     */
    public class ViewHolder extends RecyclerView.ViewHolder {
        // Your holder should contain a member variable
        // for any view that will be set as you render a row
        public TextView tvItemDesc;

        // We also create a constructor that accepts the entire item row
        // and does the view lookups to find each subview
        public ViewHolder(View itemView) {
            // Stores the itemView in a public final member variable that can be used
            // to access the context from any ViewHolder instance.
            super(itemView);
            tvItemDesc = (TextView) itemView.findViewById(R.id.tvItemDesc);
        }
    }
}

