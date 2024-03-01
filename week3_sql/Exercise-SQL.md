
  

# SQL: Structured Query Language Exercise

  

### Getting Started

1. Go to BigQuery UI https://console.cloud.google.com/bigquery

2. Add in the public data sets.

3. Click the Add Data icon

4. Add any dataset

5.  `bigquery-public-data` should become visible and populate in the BigQuery UI.

3. Add your queries where it says [YOUR QUERY HERE].

4. Make sure you add your query in between the triple tick marks.

---

  

# SQL: Structured Query Language Exercise

  
  

For this section of the exercise we will be using the `bigquery-public-data.new_york_311.311_service_requests` table.

  

1. Write a query that tells us how many rows are in the table.

```sql

SELECT
  COUNT(*)
FROM
  `bigquery-public-data.new_york_311.311_service_requests`

```

  

2. Write a query that counts all of the records for just **your** zip code. (zipcode column is `incident_zip`) 

```sql

SELECT
  COUNT(`incident_zip`)
FROM
  `bigquery-public-data.new_york_311.311_service_requests`
WHERE
  `incident_zip` = "11209"

```  

2.2. Lets find out what the most common complaint_type there is in NYC. Write a query that counts all the records for each complaint_type. Hint.. you are going to have to do a group by.  Order them from highest to lowest. 

```sql

SELECT 
  complaint_type,
  COUNT(complaint_type) as type_count
FROM 
  `bigquery-public-data.new_york_311.311_service_requests` 
GROUP BY
  complaint_type
ORDER BY
  type_count DESC

```

3. For every agency, count how many _DISTINCT_ agency_names each one has. Hint you must use a group by for this as well. 

```sql

SELECT
  `agency`,
  COUNT(DISTINCT `agency_name`) as `count_agency_names`
FROM
  `bigquery-public-data.new_york_311.311_service_requests`
GROUP BY
  `agency`

```

4. What are the 5 agency_names with the most complaints? (Small Hint: LIMIT)

```sql

SELECT
  `agency_name`,
  COUNT(*) as `count_complaints`
FROM
  `bigquery-public-data.new_york_311.311_service_requests`
GROUP BY
  `agency_name`
ORDER BY
  `count_complaints` DESC
LIMIT
  5
```

  
  

5. Lets inspect which complaint_type has the most open cases. Write a query that counts all the records for each complaint_type, just for the where the stats is 'Open' and order the results from highest to lowest.

```sql

SELECT
  `complaint_type`,
  COUNT(*) as `count_open`
FROM
  `bigquery-public-data.new_york_311.311_service_requests`
GROUP BY
  `complaint_type`, `status`
HAVING
  `status` = "Open"
ORDER BY
  `count_open` DESC
LIMIT
  1

```

  
  

6. Write a query to check if there are any duplicate values in the unique_key column. (hint.. There are two was to do this, one is to use a temporary table for the groupby, then filter for values that have more than one count, or, using just one table but including the `having` function).

```sql

SELECT
  `unique_key`,
  COUNT(`unique_key`) as `n_keys`
FROM
  `bigquery-public-data.new_york_311.311_service_requests`
GROUP BY
  `unique_key`
HAVING 
  `n_keys` > 1  

```

  
  

## For this next section, use the `new_york_citibike` datasets.

  

1. Using the `bigquery-public-data.new_york_citibike.citibike_trips` table, who went on more bike trips, self-identified Males or Females?

```sql

SELECT
  `gender`, 
  COUNT(*) as `count_trips`
FROM
  `bigquery-public-data.new_york_citibike.citibike_trips`
GROUP BY
  `gender`
ORDER BY
  `count_trips` DESC

```

2. What was the average, shortest, and longest bike trip taken in minutes?
[Super extra credit: Also tell me MEDIAN trip time]
```sql

SELECT
  AVG(`tripduration`/60) AS `avg_duration`,
  MIN(`tripduration`/60) AS `min_duration`, 
  MAX(`tripduration`/60) AS `max_duration`, 
FROM
  `bigquery-public-data.new_york_citibike.citibike_trips`

```

  

3. Write a query that, for every station_name, has the amount of trips that started there and the amount of trips that ended there. (Hint, use two temporary tables, one that counts the amount of starts, the other that counts the number of ends, and then join the two and displays each station name, total starts, total ends and the sum total starts and total ends.)

```sql

WITH
  TABLE_START AS (
  SELECT
    start_station_name as station_name,
    COUNT(start_station_name) AS count_start
  FROM
    `bigquery-public-data.new_york_citibike.citibike_trips`
  GROUP BY
    start_station_name ),
  TABLE_END AS (
  SELECT
    end_station_name as station_name,
    COUNT(end_station_name) AS count_end
  FROM
    `bigquery-public-data.new_york_citibike.citibike_trips`
  GROUP BY
    end_station_name )

SELECT
  *
FROM
  TABLE_START AS A
JOIN
  TABLE_END AS B
ON
  A.station_name = B.station_name

```

  
  
  

## Political Ads
1. Who is spending the most money on political ads in the US.  

Using the `bigquery-public-data.google_political_ads.advertiser_weekly_spend` table, write a query that sums all the `spend_usd` for each `advertiser_name`. Order them from most to least. [Who spent the 20th most... Guess which instructor managed that campaigns data...]

```sql

SELECT
  `advertiser_name`, 
  SUM(`spend_usd`) as `spend_sum`
FROM
  `bigquery-public-data.google_political_ads.advertiser_weekly_spend`
GROUP BY
  `advertiser_name`
ORDER BY
  `spend_sum` DESC

```

  

2. Do the same thing, but for only THIS YEAR. [HINT:  look at table schema for which column to use]

```sql

SELECT
  `advertiser_name`, 
  SUM(`spend_usd`) as `spend_sum`, 
  `week_start_date`
FROM
  `bigquery-public-data.google_political_ads.advertiser_weekly_spend`
WHERE
  `week_start_date` >= '2024-01-01'
GROUP BY
  `advertiser_name`, `week_start_date`
ORDER BY
  `spend_sum` DESC

```
 

3. Find what week_start_date had the highest ad spend..?

```sql

SELECT
  SUM(`spend_usd`) as `spend_sum`, 
  `week_start_date`
FROM
  `bigquery-public-data.google_political_ads.advertiser_weekly_spend`
GROUP BY
  `week_start_date`
ORDER BY
  `spend_sum` DESC
LIMIT
  1

```

  

5. THIS ONE QUESTION OPTIONAL Extra credit question, using the same table as above, find out how much each advertiser_name spent on average, min and max for all their ads. This is difficult.  Hint.... Temporary Tables with Joins.

```

[YOUR ANSWER HERE]

```
  
  

### For the next question, use the `census_bureau_usa` tables.

*  `bigquery-public-data.census_bureau_usa.population_by_zip_2000`

*  `bigquery-public-data.census_bureau_usa.population_by_zip_2010`

  

1. Write a query that returns each zipcode and their population for 2000 and 2010. Hint... You are probably going to have to use two temporary tables, then join them.

```sql

WITH
  TABLE_2000 AS (
  SELECT
    zipcode, 
    SUM(population) AS sum_population_2000
  FROM
    `bigquery-public-data.census_bureau_usa.population_by_zip_2000`
  GROUP BY
    zipcode ),
  TABLE_2010 AS (
  SELECT
    zipcode, 
    SUM(population) AS sum_population_2010
  FROM
    `bigquery-public-data.census_bureau_usa.population_by_zip_2010`
  GROUP BY
    zipcode )


SELECT
  *
FROM
  TABLE_2000 AS A
JOIN
  TABLE_2010 AS B
ON
  A.zipcode = B.zipcode

```

1. Building upon the query above, tell me which zipcode had the largest popluation growth and had the least (or negative) growth. 

```sql

WITH
  TABLE_2000 AS (
  SELECT
    zipcode, 
    SUM(population) AS sum_population_2000
  FROM
    `bigquery-public-data.census_bureau_usa.population_by_zip_2000`
  GROUP BY
    zipcode ),
  TABLE_2010 AS (
  SELECT
    zipcode, 
    SUM(population) AS sum_population_2010
  FROM
    `bigquery-public-data.census_bureau_usa.population_by_zip_2010`
  GROUP BY
    zipcode )


SELECT
  *, 
  sum_population_2010-sum_population_2000 as population_growth
FROM
  TABLE_2000 AS A
JOIN
  TABLE_2010 AS B
ON
  A.zipcode = B.zipcode
ORDER BY
  population_growth ASC

```
  

## EXTRA CREDIT, using python for BigQuery


Extra credit: For the next section, answer the following questions in the notebook below. 

1. Open up this [this Colab notebook](https://colab.research.google.com/drive/1kHdTtuHTPEaMH32GotVum41YVdeyzQ74?usp=sharing).

2. Save a copy of it in your drive.

3. Rename your saved version with your initials.

4. Click the 'Share' button on the top right.

5. Change the permissions so anyone with link can view.

6. Copy the link and paste it right below this line.

7. [THE LINK TO YOUR COLAB NOTEBOOK GOES HERE]

8. Begin working on the questions in that file.