-- List all records with non-empty name in second_table, ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
