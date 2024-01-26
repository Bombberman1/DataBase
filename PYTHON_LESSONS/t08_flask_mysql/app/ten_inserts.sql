DELIMITER //

DROP PROCEDURE IF EXISTS insert_noname;
CREATE PROCEDURE insert_noname()
BEGIN
    DECLARE counter INT DEFAULT 1;

    WHILE counter <= 10 DO
		BEGIN
			DECLARE noname_value VARCHAR(255);
			SET noname_value = CONCAT('Noname', counter);

			INSERT INTO iot_db.robopatroldeveloper (name)
			VALUES (noname_value);

			SET counter = counter + 1;
        END;
    END WHILE;
END //

DELIMITER ;

CALL insert_noname();

