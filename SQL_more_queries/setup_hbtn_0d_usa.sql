-- Təmiz hbtn_0d_usa setup script

-- 1. Database yaradılır
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- 2. Database istifadə olunur
USE hbtn_0d_usa;

-- 3. States cədvəli yaradılır
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- 4. States cədvəlinə unikal məlumat əlavə edilir
INSERT INTO states (name)
VALUES ('California'), ('Arizona'), ('Texas'), ('Utah')
ON DUPLICATE KEY UPDATE name = name;

-- 5. Cities cədvəli yaradılır
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

-- 6. Cities cədvəlinə data əlavə edilir
-- Əgər artıq eyni data varsa, yenidən insert etməyəcək
INSERT INTO cities (state_id, name)
VALUES
((SELECT id FROM states WHERE name = 'California'), 'San Francisco'),
((SELECT id FROM states WHERE name = 'California'), 'San Jose'),
((SELECT id FROM states WHERE name = 'Arizona'), 'Page'),
((SELECT id FROM states WHERE name = 'Texas'), 'Paris'),
((SELECT id FROM states WHERE name = 'Texas'), 'Houston'),
((SELECT id FROM states WHERE name = 'Texas'), 'Dallas')
ON DUPLICATE KEY UPDATE name = name;
