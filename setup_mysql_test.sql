--   Creates a MySQL server with:
--   Database hbnb_test_db.
--   User hbnb_test with password hbnb_test_pwd in localhost.
--   Grants all privileges for hbnb_test on hbnb_test_db.
--   Grants SELECT privilege for hbnb_test on performance.

-- Create or ensure the existence of the 'hbnb_test_db' database
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or ensure the existence of the 'hbnb_test' user with the specified password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the 'hbnb_test_db' to the 'hbnb_test' user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on the 'performance_schema' database to the 'hbnb_test' user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
