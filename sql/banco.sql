CREATE DATABASE IF NOT EXISTS db_loja;
USE db_loja;

CREATE TABLE IF NOT EXISTS Tb_produto (
    Cd_Produto INT PRIMARY KEY auto_increment,
    Nome_Produto VARCHAR(100) NOT NULL
);