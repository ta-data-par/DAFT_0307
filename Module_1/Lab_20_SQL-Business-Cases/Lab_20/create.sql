CREATE DATABASE lab_mysql;
USE lab_mysql;

CREATE TABLE Cars (
VIN varchar(30), 
Manufacturer varchar(30), 
Model varchar (30), 
Year integer, 
Color varchar (30) );

CREATE TABLE Customers (
Customer_ID integer,
Name varchar (30),
Phone varchar(30),
Email varchar(30),
Address varchar(50),
City varchar(30),
StateProvince varchar(30),
Country varchar(30),
Postal_Code integer );

CREATE TABLE Salespersos (
Staff_ID integer,
Name varchar(30),
Store varchar(30));

CREATE TABLE Invoices (
Invoice_Number integer,
Date date,
Car varchar(30),
Customer_ID integer,
Salesperson varchar(30));





