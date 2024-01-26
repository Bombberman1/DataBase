USE iot_db;
DELIMITER //

DROP TRIGGER IF EXISTS enforce_buyer_relation;
CREATE TRIGGER enforce_buyer_relation
BEFORE INSERT ON child
FOR EACH ROW
BEGIN
    DECLARE buyer_count INT;

    -- Check if there is a corresponding buyer record with the specified buyerId
    SELECT COUNT(*) INTO buyer_count
    FROM buyer
    WHERE userId = NEW.buyerId;

    -- If the buyer record does not exist, raise an error
    IF buyer_count = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Buyer with specified buyerId does not exist.';
    END IF;
END;
//
DELIMITER ;
