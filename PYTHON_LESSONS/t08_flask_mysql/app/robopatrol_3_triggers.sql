USE iot_db;
DELIMITER //

DROP TRIGGER IF EXISTS prevent_update;
CREATE TRIGGER prevent_update
BEFORE UPDATE ON robopatrol
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Update is not allowed';
END;

//
DELIMITER ;

DELIMITER //

DROP TRIGGER IF EXISTS prevent_delete;
CREATE TRIGGER prevent_delete
BEFORE DELETE ON robopatrol
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Delete is not allowed';
END;

//
DELIMITER ;

DELIMITER //

DROP TRIGGER IF EXISTS prevent_insert_price;
CREATE TRIGGER prevent_insert_price
BEFORE INSERT ON robopatrol
FOR EACH ROW
BEGIN
    IF NEW.price > 10000 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Price is too high';
    END IF;
END;

//
DELIMITER ;
