/*
a)In actor table column information is on actor_id, first_name, last_name, last_update
b) film_id, title, description, release_year, language_id, original_language_id, rental_duration, rental_rate, length,
 replacement_cost rating, special_features, last_update
c)  film_actor
d)rental table has 1 primary key and 3 foreign keys as well as time specifics, which makes it easier to understand with references to other tables
e)inventory table also inludes 2 foreign keys and last_update, help us to understand what we have as of now
f)We can look at 'film' and 'rental' tables to have a better grasp of movies were rented that specific day and see which movies were they.
*/

--a
SELECT * FROM actor
--b
SELECT * FROM film
--c
SELECT * FROM film_actor
--d
SELECT * FROM rental
--e
SELECT * FROM inventory
--f
SELECT * FROM film, rental
