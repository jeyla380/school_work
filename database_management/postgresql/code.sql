/*1) Shows the most rented genres to the least --> Use the 3rd query!*/
SELECT category.name AS genre, COUNT(customer.customer_id) AS total_times_rented
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
ORDER BY total_times_rented DESC;


/*2) Shows the average rental duration of each genre (from greatest to least)*/
SELECT category.name AS genre, AVG(film.rental_duration) AS avg_rental_duration
FROM category JOIN film_category
USING(category_id)
JOIN film
USING(film_id)
GROUP BY genre
ORDER BY avg_rental_duration DESC;


/*3) Adds a 'popularity' field to the first query and sets it to true and false; true = high popularity
and false = low popularity*/
SELECT category.name AS genre, COUNT(customer.customer_id) AS total_times_rented,
	CAST(
	CASE
		WHEN COUNT(customer.customer_id) >= 1000 THEN 1
		ELSE 0
	END AS BOOL) AS popularity
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
ORDER BY total_times_rented DESC;


/*Function for changing popularity boolean to a varchar*/
create function HighLowPopularity(x bool)
	returns varchar(50)
	language plpgsql
as
$$
begin
	if x then
		return 'High Popularity';
	else
		return 'Low Popularity';
	end if;
end
$$;


/*4) Add the function into the code so Popularity field will be updated*/
SELECT category.name AS genre, COUNT(customer.customer_id) AS total_times_rented,
	HighLowPopularity(
	CAST(
	CASE
		WHEN COUNT(customer.customer_id) >= 1000 THEN 1
		ELSE 0
	END
	AS BOOL)) AS popularity
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
ORDER BY total_times_rented DESC;



/*detailed table: genre_id, genre, total_times_rented, popularity, avg_rental_duration*/
CREATE TABLE detailed_table (
	genre_id INT PRIMARY KEY,
	genre VARCHAR(50),
	total_times_rented INT,
	popularity BOOL,
	avg_rental_duration FLOAT
);


/*summary table: genre_id genre, total_times_rented, avg_rental_duration*/
CREATE TABLE summary_table (
	genre_id INT PRIMARY KEY,
	genre VARCHAR(50),
	total_times_rented INT,
	avg_rental_duration FLOAT
);



/*SQL query to extract raw data & input into detailed table*/
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



/*Create a trigger using a function to update summary_table*/
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

/*trigger*/
CREATE TRIGGER update_table
	AFTER INSERT OR UPDATE OR DELETE
	ON detailed_table
	FOR EACH ROW
	EXECUTE PROCEDURE update_to_summary();
	


/*Procedure that removes data from both detailed and summary table and extracts data from D each time*/
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
