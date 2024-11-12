-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema pesagem_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema pesagem_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pesagem_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `pesagem_db` ;

-- -----------------------------------------------------
-- Table `pesagem_db`.`veiculos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pesagem_db`.`veiculos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `placa` VARCHAR(10) NOT NULL,
  `modelo` VARCHAR(50) NOT NULL,
  `tipo` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `pesagem_db`.`pesagens`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pesagem_db`.`pesagens` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `veiculo_id` INT NOT NULL,
  `peso_bruto` DECIMAL(10,2) NOT NULL,
  `peso_tara` DECIMAL(10,2) NOT NULL,
  `peso_liquido` DECIMAL(10,2) GENERATED ALWAYS AS ((`peso_bruto` - `peso_tara`)) STORED,
  `data_pesagem` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `veiculo_id` (`veiculo_id` ASC) VISIBLE,
  CONSTRAINT `pesagens_ibfk_1`
    FOREIGN KEY (`veiculo_id`)
    REFERENCES `pesagem_db`.`veiculos` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
