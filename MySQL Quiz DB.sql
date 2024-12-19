CREATE DATABASE quiz_db;

USE quiz_db;

CREATE TABLE quiz (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    answer CHAR(1) NOT NULL
);

-- Insert the quiz data
INSERT INTO quiz (question, option_a, option_b, option_c, option_d, answer) VALUES
("What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", "C"),
("Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", "B"),
("Who wrote 'To Kill a Mockingbird'?", "Harper Lee", "J.K. Rowling", "Ernest Hemingway", "Mark Twain", "A"),
("What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "D"),
("What is the smallest prime number?", "1", "2", "3", "5", "B");
