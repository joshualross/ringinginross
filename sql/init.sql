DROP TABLE IF EXISTS guest;
CREATE TABLE guest (
  uuid VARCHAR(36) NOT NULL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(256) DEFAULT NULL,
  is_allowed_guest TINYINT DEFAULT 0,
  guest_uuid VARCHAR(36) DEFAULT NULL,
  message TEXT DEFAULT NULL,
  created INT NOT NULL,
  updated INT NOT NULL
);

INSERT INTO guest
  (uuid, first_name, last_name, email, is_allowed_guest, created, updated)
VALUES
  ('8ccb8bfd-aed2-4a73-8f68-a621e2c4aa8b', 'Joshua', 'Ross', 'joshualross@gmail.com', 1, 1453588796, 1453588796)