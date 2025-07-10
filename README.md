# Netflix Data Transformation Project

This project demonstrates downloading a public dataset from Kaggle, performing data transformations using Python and pandas, and managing the code and data with Git and GitHub.

---

## Dataset

The dataset used is the [Netflix Shows Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows) from Kaggle. It contains metadata about Netflix movies and TV shows, including titles, directors, release years, genres, and more.

---

## Project Structure

- `netflix_titles.csv`: The original raw dataset downloaded from Kaggle.
- `transform_netflix.py`: Python script that performs the data transformations.
- `netflix_transformed.csv`: The resulting CSV file after applying transformations.

## Data Transformations

The script performs the following transformations:

1. Drops rows with missing values in the `director` column.
2. Adds a new column `content_age` calculating the age of the content (current year minus release year).
3. Converts the `date_added` column to datetime format, handling irregularities.
4. Extracts the year from the `date_added` column into a new `added_year` column.
5. Filters the dataset to include only TV Shows.

---

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/Saidhanekula31/netflix-data-transform.git
   cd netflix-data-transform# netflix-data-transform

