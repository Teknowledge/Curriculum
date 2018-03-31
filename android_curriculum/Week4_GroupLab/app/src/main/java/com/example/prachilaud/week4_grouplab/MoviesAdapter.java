package com.example.prachilaud.week4_grouplab;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

import java.util.ArrayList;

/**
 * MoviesAdapter is the adapter we will be using for the list of Movie objects displayed in
 * Movies Activity.
 */

public class MoviesAdapter extends ArrayAdapter<Movie> {

    public MoviesAdapter(Context context, ArrayList<Movie> movies) {
        super(context, R.layout.item_movie, movies);
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {

        Movie movie = getItem(position);

        ViewHolder viewHolder;

        if (convertView == null) {
            // If the ViewHolder hasn't been set up yet, set it up and fill in all the fields.
            viewHolder = new ViewHolder();
            viewHolder.title = (TextView) convertView.findViewById(R.id.tvTitle);
            viewHolder.overview = (TextView) convertView.findViewById(R.id.tvOverview);
            viewHolder.popularity = (ProgressBar) convertView.findViewById(R.id.pbPopularity);
            viewHolder.image = (ImageView) convertView.findViewById(R.id.ivImage);

            // Inflate the view with the movie item XML layout, and set tag to the ViewHolder object.
            convertView = LayoutInflater.from(getContext()).inflate(R.layout.item_movie, parent, false);
            convertView.setTag(viewHolder);
        } else {
            // If the view is not null, then that means this view is being recycled. That means
            // we don't have to re-inflate the layout, but we need to watch out for this and make
            // sure we replace all the fields below.
            viewHolder = (ViewHolder) convertView.getTag();
        }

        // Populates non-null fields; if the fields are non-null, it is possible that they have
        // old information because of recycling.
        if(viewHolder.title != null) {
            viewHolder.title.setText(movie.getOriginalTitle());
        }
        if(viewHolder.overview != null) {
            viewHolder.overview.setText(movie.getOverview());
        }
        if (viewHolder.popularity != null) {
            viewHolder.popularity.setProgress((int)movie.getPopularity()*2);
        }

        // Using Picasso to load images, keep a placeholder while the actual image loads
        Picasso.with(getContext()).load(movie.getPosterPath()).placeholder(R.drawable.placeholder_img).into(viewHolder.image);

        return convertView;

    }

    /**
     * The ViewHolder class is used to enable direct access to all the views that comprise
     * the movie object. We only need to keep the Vie
     */
    public class ViewHolder {
        TextView title;
        TextView overview;
        ImageView image;
        ProgressBar popularity;

        public ViewHolder(){
            // Empty constructor
        }
    }
}
