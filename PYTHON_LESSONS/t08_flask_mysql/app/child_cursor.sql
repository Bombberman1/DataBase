DELIMITER //

DROP PROCEDURE IF EXISTS copy_data_to_random_tables;
CREATE PROCEDURE copy_data_to_random_tables()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE original_table_name VARCHAR(255);
    DECLARE new_table_name1 VARCHAR(255);
    DECLARE new_table_name2 VARCHAR(255);
    DECLARE cur CURSOR FOR SELECT table_name FROM information_schema.tables WHERE table_schema = 'iot_db' AND table_name = 'child';
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;

    read_loop: LOOP
        FETCH cur INTO original_table_name;
        IF done THEN
            LEAVE read_loop;
        END IF;

        SET new_table_name1 = CONCAT(original_table_name, '_', DATE_FORMAT(NOW(), '%H_%i_%s'), '_1');
        SET new_table_name2 = CONCAT(original_table_name, '_', DATE_FORMAT(NOW(), '%H_%i_%s'), '_2');

        SET @create_table1_sql = CONCAT('CREATE TABLE iot_db.', new_table_name1, ' AS SELECT * FROM iot_db.', original_table_name, ' ORDER BY RAND()');
        PREPARE stmt1 FROM @create_table1_sql;
        EXECUTE stmt1;
        DEALLOCATE PREPARE stmt1;

        SET @create_table2_sql = CONCAT('CREATE TABLE iot_db.', new_table_name2, ' AS SELECT * FROM iot_db.', original_table_name, ' ORDER BY RAND()');
        PREPARE stmt2 FROM @create_table2_sql;
        EXECUTE stmt2;
        DEALLOCATE PREPARE stmt2;
    END LOOP;

    CLOSE cur;
END //

DELIMITER ;

CALL copy_data_to_random_tables();
