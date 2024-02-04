--   Creates a MySQL server with:
--   Database hbnb_dev_db.
--   User hbnb_dev with password hbnb_dev_pwd in localhost.
--   Grants all privileges for hbnb_dev on hbnb_dev_db.
--   Grants SELECT privilege for hbnb_dev on performance.

-- Create or ensure the existence of the 'hbnb_dev_db' database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Set the password policy to LOW for simplicity (may be changed based on security requirements)
SET GLOBAL validate_password.policy = LOW;

-- Create or ensure the existence of the 'hbnb_dev' user with the specified password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the 'hbnb_dev_db' to the 'hbnb_dev' user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the 'performance_schema' database to the 'hbnb_dev' user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Refresh MySQL privileges to apply the changes
FLUSH PRIVILEGES;
