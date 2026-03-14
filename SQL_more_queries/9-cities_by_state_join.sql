-- Lists all cities with their state names from hbtn_0d_usa
SELECT cities.id, cities.name AS city, states.name AS state
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
