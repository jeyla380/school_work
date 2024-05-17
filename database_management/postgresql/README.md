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


