CREATE SCHEMA movie_info;
-- Specify the database to use
USE movie_info;

-- Create the companies table
CREATE TABLE companies (
    company_id INT PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL
);

-- Create the genres table
CREATE TABLE genres (
    genre_id INT PRIMARY KEY,
    genre_name VARCHAR(255) NOT NULL
);

-- Create the directors table
CREATE TABLE directors (
    director_id INT PRIMARY KEY,
    director_name VARCHAR(255) NOT NULL
);

-- Create the movies table
CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    debut_year INT NOT NULL,
    company_id INT,
    genre_id INT,
    director_id INT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id),
    FOREIGN KEY (director_id) REFERENCES directors(director_id)
);

-- Insert sample data into companies table
INSERT INTO companies (company_id, company_name) VALUES
(1, 'Warner Bros.'),
(2, 'Universal Pictures'),
(3, '20th Century Fox'),
(4, 'Paramount Pictures'),
(5, 'Columbia Pictures');

-- Insert sample data into genres table
INSERT INTO genres (genre_id, genre_name) VALUES
(1, 'Action'),
(2, 'Adventure'),
(3, 'Drama'),
(4, 'Comedy'),
(5, 'Sci-Fi');

-- Insert sample data into directors table
INSERT INTO directors (director_id, director_name) VALUES
(1, 'Christopher Nolan'),
(2, 'Steven Spielberg'),
(3, 'James Cameron'),
(4, 'Quentin Tarantino'),
(5, 'Martin Scorsese');

-- Insert sample data into movies table
INSERT INTO movies (movie_id, title, debut_year, company_id, genre_id, director_id) VALUES
(1, 'Inception', 2010, 1, 5, 1),
(2, 'Jurassic Park', 1993, 2, 2, 2),
(3, 'Avatar', 2009, 3, 5, 3),
(4, 'Titanic', 1997, 4, 3, 3),
(5, 'Pulp Fiction', 1994, 5, 3, 4),
(6, 'The Dark Knight', 2008, 1, 1, 1),
(7, 'Goodfellas', 1990, 4, 3, 5),
(8, 'Django Unchained', 2012, 5, 2, 4),
(9, 'Interstellar', 2014, 1, 5, 1),
(10, 'Schindler\'s List', 1993, 2, 3, 2);

-- Query to list movies with their debut year, genre, director, and publishing company
SELECT
    m.title AS movie_title,
    m.debut_year,
    g.genre_name,
    d.director_name,
    c.company_name
FROM
    movies m
JOIN
    companies c ON m.company_id = c.company_id
JOIN
    genres g ON m.genre_id = g.genre_id
JOIN
    directors d ON m.director_id = d.director_id;

-- Additional query to count movies per company
SELECT
    c.company_name,
    COUNT(m.movie_id) AS movie_count
FROM
    movies m
JOIN
    companies c ON m.company_id = c.company_id
GROUP BY
    c.company_name;

-- Additional query to count movies per genre
SELECT
    g.genre_name,
    COUNT(m.movie_id) AS movie_count
FROM
    movies m
JOIN
    genres g ON m.genre_id = g.genre_id
GROUP BY
    g.genre_name;

-- Additional query to count movies per director
SELECT
    d.director_name,
    COUNT(m.movie_id) AS movie_count
FROM
    movies m
JOIN
    directors d ON m.director_id = d.director_id
GROUP BY
    d.director_name;
