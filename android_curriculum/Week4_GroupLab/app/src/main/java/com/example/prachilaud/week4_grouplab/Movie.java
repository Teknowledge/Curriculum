package com.example.prachilaud.week4_grouplab;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.Serializable;
import java.util.ArrayList;

/**
 * The Movie class defines the objects that are going to be displayed in the list in
 * MoviesActivity. Each Movie object keeps track of the information about a particular movie.
 */

public class Movie implements Serializable {

    // Attributes of the movie we want
    public String originalTitle;
    public String posterPath;
    public String overview;
    public String backdropPath;
    public float rating;
    public double popularity;

    /*
    When we create a movie object, we pass it the JSONObject that is returned from our API call.
    We then populate our class variables with the information in that object.
      */
    public Movie(JSONObject jsonObject) throws JSONException {
        posterPath = jsonObject.getString("poster_path");
        originalTitle = jsonObject.getString("original_title");
        overview = jsonObject.getString("overview");
        backdropPath = jsonObject.getString("backdrop_path");
        rating = (float) jsonObject.getDouble("vote_average");
        popularity = jsonObject.getDouble("popularity");
    }

    /*
    Takes array of JSON responses from API call, and returns array of Movies created.
    We need this method to convert our JSON responses into an easier object from which we can
    extract information.
     */

    public static ArrayList<Movie> fromJsonArray(JSONArray jsonArray) {
        ArrayList<Movie> results = new ArrayList<>();
        for(int i=0; i< jsonArray.length(); i++) {
            try {
                results.add(new Movie(jsonArray.getJSONObject(i)));
            } catch (JSONException e) {
                e.printStackTrace();
            }
        }
        return results;
    }

    /*
    Getters for all movie attributes
     */

    public String getOriginalTitle() {
        return originalTitle;
    }

    public String getPosterPath() {
        return posterPath;
    }

    public String getOverview() {
        return overview;
    }

    public String getBackdropPath() {
        return backdropPath;
    }

    public float getRating() {
        return rating;
    }

    public double getPopularity() {
        return popularity;
    }
}
