
-- DROP TABLE IF EXISTS product;
-- DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS productMovement;

CREATE TABLE IF NOT EXISTS product (
  product_id TEXT PRIMARY KEY ,
  product_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS location (
  location_id TEXT PRIMARY KEY ,
  location_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS productMovement (
    movement_id TEXT PRIMARY KEY ,
    time_stamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    from_location TEXT, 
    to_location TEXT, 
    product_id TEXT,    
    qty INTEGER,
    FOREIGN KEY (from_location) REFERENCES location (location_id),
    FOREIGN KEY (to_location) REFERENCES location (location_id),
    FOREIGN KEY (product_id) REFERENCES product (product_id)
);