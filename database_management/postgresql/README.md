# Advanced Data Management (Data Analysis)
This assignment is based off the data from the DVD Rental Database on the [PostgreSQL Sample Database](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/) webpage.

<br>

## A. Business Report

<b>Business Problem:</b> Which genres of film are the most and least popular, and what is the average rental duration for each one?

### A1.

<b>Detailed Table Fields:</b>
- genre_id
- genre
- total_times_rented
- popularity
- avg_rental_duration (Average Rental Duration)


<b> Summary Table Fields: </b>
- genre_id
- genre
- total_times_rented
- avg_rental_duration

### A2.

<b> Types of Data Fields in Detailed Table:</b>
- genre_id: INT
- genre: VARCHAR(50)
- total_times_rented: INT
- popularity: VARCHAR(50)
- avg_rental_duration: FLOAT

<b>Types of Data Fields in Summary Table:</b>
- genre_id: INT
- genre: VARCHAR(50)
- total_times_rented: INT
- avg_rental_duration: FLOAT

### A3.
<b>Specific Tables Needed:</b>
- category
- film_category
- film
- rental
- inventory
- customer

### A4.
The Popularity field (in the detailed table) is indicating a high and low popularity with ‘true’ and ‘false’. However, it would make the calculation more readable by transforming ‘true’ with “High Popularity”, and ‘false’ with “Low Popularity”.

### A5.
<b>Detailed Table: </b>
- Adjust pricing on DVD rentals based on popularity, duration, etc.
- Determine which genre(s) of film should be acquired.
- Tailor marketing towards different genres based on popularity.

<b>Summary Table:</b>
- Provide overview of performance and trends of DVD rental company.
- Provide performance and demographic information for stakeholders.
- Plan out strategies, budget, etc. based on the overall information.

### A6.
The report should be refreshed every quarter as it’ll allow the stakeholders to respond to the changing market effectively and efficiently.

<br>

## B. Popularity Function
```sql
CREATE FUNCTION HighLowPopularity(x BOOL)
	RETURNS VARCHAR(50)
	LANGUAGE plpgsql
AS
$$
BEGIN
	IF x THEN
		RETURN  'High Popularity';
	ELSE
		RETURN  'Low Popularity';
	END IF;
END
$$;

```

| Before Function | After Function |
| --- | --- |
| ![](https://github.com/jeyla380/school_work/blob/main/database_management/postgresql/images/before_function.png) | ![](https://github.com/jeyla380/school_work/blob/main/database_management/postgresql/images/after_function.png) |

<br>

## C. Detailed Table and Summary Table
<b>Detailed Table:</b>
```sql
CREATE TABLE detailed_table (
	genre_id INT PRIMARY KEY,
	genre VARCHAR(50),
	total_times_rented INT,
	popularity VARCHAR(50),
	avg_rental_duration FLOAT
);

```

<b>Summary Table:</b>
```sql
CREATE TABLE summary_table (
	genre_id INT PRIMARY KEY,
	genre VARCHAR(50),
	total_times_rented INT,
	avg_rental_duration FLOAT
);

```

<br>

## D. Extract Data from Detailed Table
```sql
WITH total_rented_genre AS (
		SELECT category.name AS genre, COUNT(customer.customer_id) AS total_times_rented,
			HighLowPopularity(
			CAST(
				CASE
					WHEN COUNT(customer.customer_id) >= 1000 THEN 1
					ELSE 0
				END
			AS BOOL))AS popularity
		FROM category JOIN film_category
		USING(category_id)
		JOIN film
		USING(film_id)
		JOIN inventory
		USING(film_id)
		JOIN rental
		USING(inventory_id)
		JOIN customer
		USING(customer_id)
		GROUP BY genre
		ORDER BY total_times_rented DESC),
	rental_duration_genre AS (
		SELECT category.name AS genre, AVG(film.rental_duration) AS avg_rental_duration
		FROM category JOIN film_category
		USING(category_id)
		JOIN film
		USING(film_id)
		GROUP BY genre
		ORDER BY avg_rental_duration DESC)
INSERT INTO detailed_table(genre_id, genre, total_times_rented, popularity, avg_rental_duration)
SELECT RANK() OVER (ORDER BY total_rented_genre.total_times_rented DESC) AS genre_id, total_rented_genre.genre, total_rented_genre.total_times_rented, total_rented_genre.popularity, rental_duration_genre.avg_rental_duration
FROM total_rented_genre JOIN rental_duration_genre
ON total_rented_genre.genre = rental_duration_genre.genre;

```

<br>

## E. Trigger
The purpose of this trigger is to update the Summary Table every time there is a change from the Detailed Table.
```sql
/*Function*/
CREATE FUNCTION update_to_summary()
	RETURNS TRIGGER
	LANGUAGE plpgsql
AS
$$
BEGIN
	INSERT INTO summary_table(genre_id, genre, total_times_rented, avg_rental_duration)
	VALUES(NEW.genre_id, NEW.genre, NEW.total_times_rented, NEW.avg_rental_duration);
	RETURN NEW;
END;
$$

/*Trigger*/
CREATE TRIGGER update_table
	AFTER INSERT OR UPDATE OR DELETE
	ON detailed_table
	FOR EACH ROW
	EXECUTE PROCEDURE update_to_summary();

```

<br>

## Procedure
Refreshes the data in both Detailed Table and Summary Table as the data comes from the DVD Rentals Database.
```sql
CREATE PROCEDURE update_detailed_summary()
LANGUAGE plpgsql
AS
$$
BEGIN
	TRUNCATE TABLE summary_table;
	TRUNCATE TABLE detailed_table;
	WITH total_rented_genre AS (
		SELECT category.name AS genre, COUNT(customer.customer_id) AS total_times_rented,
			HighLowPopularity(
			CAST(
			CASE
				WHEN COUNT(customer.customer_id) >= 1000 THEN 1
				ELSE 0
			END
			AS BOOL))AS popularity
		FROM category JOIN film_category
		USING(category_id)
		JOIN film
		USING(film_id)
		JOIN inventory
		USING(film_id)
		JOIN rental
		USING(inventory_id)
		JOIN customer
		USING(customer_id)
		GROUP BY genre
		ORDER BY total_times_rented DESC),
	rental_duration_genre AS (
		SELECT category.name AS genre, AVG(film.rental_duration) AS avg_rental_duration
		FROM category JOIN film_category
		USING(category_id)
		JOIN film
		USING(film_id)
		GROUP BY genre
		ORDER BY avg_rental_duration DESC)
	INSERT INTO detailed_table(genre_id, genre, total_times_rented, popularity, avg_rental_duration)
	SELECT RANK() OVER (ORDER BY total_rented_genre.total_times_rented DESC) AS rank, total_rented_genre.genre, total_rented_genre.total_times_rented, total_rented_genre.popularity, rental_duration_genre.avg_rental_duration
	FROM total_rented_genre JOIN rental_duration_genre
	ON total_rented_genre.genre = rental_duration_genre.genre;
END;
$$;

```
