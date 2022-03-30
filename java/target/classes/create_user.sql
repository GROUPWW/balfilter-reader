CREATE TABLE `user` (
                        `id` INT PRIMARY KEY AUTO_INCREMENT,
                        `userName` VARCHAR(30) NOT NULL,
                        `password` VARCHAR(200) NOT NULL,
                        `email` VARCHAR(30) NOT NULL,
                        `phone` VARCHAR(30) NOT NULL
);