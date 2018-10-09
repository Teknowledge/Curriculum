package com.example.prachilaud.week4_grouplab;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ListView;

import com.loopj.android.http.AsyncHttpClient;
import com.loopj.android.http.JsonHttpResponseHandler;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

import cz.msebera.android.httpclient.Header;

/**
 * This app displays a list of upcoming movies along with information about them. The movies &
 * information are pulled from the Flixster database using the Flixster API.
 */
public class MoviesActivity extends AppCompatActivity {

    ListView lvMovies;
    MoviesAdapter moviesAdapter;
    ArrayList<Movie> movies = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_movies);

        // Set up list view and attach adapter
        lvMovies = (ListView) findViewById(R.id.lvMovies);
        moviesAdapter = new MoviesAdapter(this, movies);
        lvMovies.setAdapter(moviesAdapter);

        // Setting up response handler
        String url = "https://api.themoviedb.org/3/movie/now_playing?api_key=a07e22bc18f5cb106bfe4cc1f83ad8ed";
        AsyncHttpClient client = new AsyncHttpClient();
        client.get(url, new JsonHttpResponseHandler(){
            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONObject response) {
                JSONArray movieJsonResults = null;
                try {
                    // Load the results from the JSON response into a JSON array, and then use the
                    // convert method fromJSONArray that we defined in the Movie class to
                    // turn it into a list of Movie objects. Update the adapter as usual.
                    movieJsonResults = response.getJSONArray("results");
                    movies.addAll(Movie.fromJsonArray(movieJsonResults));
                    moviesAdapter.notifyDataSetChanged();
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }

            @Override
            public void onFailure(int statusCode, Header[] headers, Throwable throwable, JSONObject errorResponse) {
                super.onFailure(statusCode, headers, throwable, errorResponse);
            }
        });
    }
}
