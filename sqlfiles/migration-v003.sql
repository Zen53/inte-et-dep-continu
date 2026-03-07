-- Migration v003
-- Insert initial user in ynov_ci database

USE ynov_ci;

INSERT INTO users (username, email, password) VALUES 
('admin', 'admin@ynov.fr', '$2y$10$N9qo8uLOickgx2ZMRZoMye4ufVHYVpOT610ABc5PH'); 
