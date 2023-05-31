# create db
CREATE DATABASE todolist_flask;

-- todolist_flask.todos definition

CREATE TABLE `todos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    
# library
pip3 install pymysql
pip3 install flask_cors
pip3 install flask-mysql

# run
python3 main.py