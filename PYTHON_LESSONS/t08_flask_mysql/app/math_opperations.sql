DELIMITER //

DROP FUNCTION IF EXISTS calculate_math_opp;
CREATE FUNCTION calculate_math_opp(math_type VARCHAR(255))
RETURNS DECIMAL(18,2)
DETERMINISTIC
BEGIN
    DECLARE result DECIMAL(18,2);

    IF math_type = 'MAX' THEN
        SELECT MAX(price) INTO result FROM robopatrol;
    ELSEIF math_type = 'MIN' THEN
        SELECT MIN(price) INTO result FROM robopatrol;
    ELSEIF math_type = 'SUM' THEN
        SELECT SUM(price) INTO result FROM robopatrol;
    ELSEIF math_type = 'AVG' THEN
        SELECT AVG(price) INTO result FROM robopatrol;
    ELSE
        SET result = NULL;
    END IF;

    RETURN result;
END //

DELIMITER ;


DELIMITER //

DROP PROCEDURE IF EXISTS get_math_opp_result;
CREATE PROCEDURE get_math_opp_result()
BEGIN
    DECLARE max_value DECIMAL(18,2);
    DECLARE min_value DECIMAL(18,2);
    DECLARE sum_value DECIMAL(18,2);
    DECLARE avg_value DECIMAL(18,2);

    SET max_value = calculate_math_opp('MAX');
    SET min_value = calculate_math_opp('MIN');
    SET sum_value = calculate_math_opp('SUM');
    SET avg_value = calculate_math_opp('AVG');

    SELECT max_value, min_value, sum_value, avg_value;
END //

DELIMITER ;

CALL get_math_opp_result();
