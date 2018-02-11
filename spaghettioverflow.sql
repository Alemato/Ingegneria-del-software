-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Feb 11, 2018 alle 20:29
-- Versione del server: 10.1.28-MariaDB
-- Versione PHP: 7.1.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `spaghettioverflow`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `areas`
--

CREATE TABLE `areas` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `areas`
--

INSERT INTO `areas` (`id`, `name`) VALUES
(1, 'A1');

-- --------------------------------------------------------

--
-- Struttura della tabella `clusters`
--

CREATE TABLE `clusters` (
  `id` int(11) NOT NULL,
  `idA` int(11) NOT NULL,
  `name` text NOT NULL,
  `inef` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `clusters`
--

INSERT INTO `clusters` (`id`, `idA`, `name`, `inef`) VALUES
(1, 1, 'C1', 60),
(2, 1, 'C2', 60);

-- --------------------------------------------------------

--
-- Struttura della tabella `engineers`
--

CREATE TABLE `engineers` (
  `name` text NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `engineers`
--

INSERT INTO `engineers` (`name`, `username`, `password`) VALUES
('admin', 'admin', 'admin');

-- --------------------------------------------------------

--
-- Struttura della tabella `supervisors`
--

CREATE TABLE `supervisors` (
  `name` text NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dump dei dati per la tabella `supervisors`
--

INSERT INTO `supervisors` (`name`, `username`, `password`) VALUES
('admin', 'admin', 'admin');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `areas`
--
ALTER TABLE `areas`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `clusters`
--
ALTER TABLE `clusters`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk` (`idA`);

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `clusters`
--
ALTER TABLE `clusters`
  ADD CONSTRAINT `fk` FOREIGN KEY (`idA`) REFERENCES `areas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
