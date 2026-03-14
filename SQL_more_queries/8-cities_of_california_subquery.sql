-- List all cities of California using a subquery (no JOIN)
USE hbtn_0d_usa;

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
