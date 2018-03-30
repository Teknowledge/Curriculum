package com.example.prachilaud.week3_individuallab;

/**
 * The TodoItem class is used to define a data model for the items in the to-do list.
 * To-do items in this project only contain a description.
 * We also create a corresponding XML layout file that describes the layout for each to-do item
 * in the list.
 */
public class TodoItem {

    // The naming convention is to name class variables with an 'm' prefix.
    private String mItemDesc;

    public TodoItem(String itemDesc) {
        mItemDesc = itemDesc;
    }

    public String getItem(){
        return mItemDesc;
    }

}