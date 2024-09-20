-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Mag 31, 2023 alle 21:20
-- Versione del server: 10.4.27-MariaDB
-- Versione PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rzm`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `carrello`
--

CREATE TABLE `carrello` (
  `idCompratore` varchar(30) NOT NULL,
  `id` int(11) NOT NULL,
  `Nome` varchar(30) NOT NULL,
  `Descrizione` varchar(255) NOT NULL,
  `Taglia` varchar(30) NOT NULL,
  `Prezzo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `carrello`
--

INSERT INTO `carrello` (`idCompratore`, `id`, `Nome`, `Descrizione`, `Taglia`, `Prezzo`) VALUES
('demetriuszaiat@gmail.com', 46, 'palm angels', 'nuova', 'L', 800);

-- --------------------------------------------------------

--
-- Struttura della tabella `compra`
--

CREATE TABLE `compra` (
  `emailUtente` varchar(30) NOT NULL,
  `idMerce` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `merce`
--

CREATE TABLE `merce` (
  `id` int(11) NOT NULL,
  `Nome` varchar(30) DEFAULT NULL,
  `Descrizione` varchar(255) DEFAULT NULL,
  `Categoria` varchar(30) DEFAULT NULL,
  `Taglia` varchar(10) NOT NULL,
  `prezzo` int(10) DEFAULT NULL,
  `immagine` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `merce`
--

INSERT INTO `merce` (`id`, `Nome`, `Descrizione`, `Categoria`, `Taglia`, `prezzo`, `immagine`) VALUES
(39, 'MOCHA', 'indossate dal leggendario alessandro ramos', 'scarpe', '42', 30000, 'mocha.png'),
(40, 'aj4 navy', 'indossate solo una volta', 'scarpe', '42', 400, 'aj4.png'),
(41, 'air force rainbow', 'REGALO POCO APREZZATO (NUOVE)', 'scarpe', '42', 110, 'airforce.png'),
(42, 'vans x off-white', 'distrutte', 'scarpe', '42', 100, 'off.png'),
(43, 'fear hoodie', 'quasi nuova', 'felpe', 'L', 670, 'fear.png'),
(44, 'stone island hoodie', 'molto affezzionato ', 'felpe', 'L', 300, 'stone.png'),
(45, 'represent', 'indossata da cr7', 'felpe', 'L', 50, 'represent.png'),
(47, 'artt.', 'trovata per terra', 'felpe', 'XS', 10000, 'kenzo.png'),
(48, 'stone island', 'quasi nuova', 'maglie', 'M', 160, 'island.png'),
(49, 'burlon', 'regalata da burlon', 'maglie', 'M', 2000, 'burlon.png'),
(50, 'dima', 'indossata da dima la pula', 'maglie', 'M', 1, 'otto.png');

-- --------------------------------------------------------

--
-- Struttura della tabella `recensione`
--

CREATE TABLE `recensione` (
  `id` int(11) NOT NULL,
  `descrizione` varchar(255) NOT NULL,
  `valutazione` int(2) DEFAULT NULL,
  `emailAcquirente` varchar(255) NOT NULL,
  `emailVenditore` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `utenti`
--

CREATE TABLE `utenti` (
  `email` varchar(30) NOT NULL,
  `Nome` varchar(30) NOT NULL,
  `Cognome` varchar(30) NOT NULL,
  `Password` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `utenti`
--

INSERT INTO `utenti` (`email`, `Nome`, `Cognome`, `Password`) VALUES
('alessandroramos@gmail.com', 'Alessandro', 'Ramos Garay', '1234'),
('demetriuszaiat@gmail.com', 'Demetrius', 'Zaiat', '1234'),
('massimilianostercho@gmail.com', 'Massimiliano', 'Stercho', '1234');

-- --------------------------------------------------------

--
-- Struttura della tabella `vende`
--

CREATE TABLE `vende` (
  `emailUtente` varchar(30) NOT NULL,
  `idMerce` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struttura della tabella `venduto`
--

CREATE TABLE `venduto` (
  `idVenditore` varchar(30) NOT NULL,
  `id` int(11) NOT NULL,
  `Nome` varchar(30) NOT NULL,
  `Descrizione` varchar(255) NOT NULL,
  `Taglia` varchar(30) NOT NULL,
  `Prezzo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `compra`
--
ALTER TABLE `compra`
  ADD PRIMARY KEY (`emailUtente`,`idMerce`),
  ADD KEY `idMerce` (`idMerce`);

--
-- Indici per le tabelle `merce`
--
ALTER TABLE `merce`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `recensione`
--
ALTER TABLE `recensione`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `emailAcquirente` (`emailAcquirente`,`emailVenditore`),
  ADD KEY `emailVenditore` (`emailVenditore`);

--
-- Indici per le tabelle `utenti`
--
ALTER TABLE `utenti`
  ADD PRIMARY KEY (`email`);

--
-- Indici per le tabelle `vende`
--
ALTER TABLE `vende`
  ADD PRIMARY KEY (`emailUtente`,`idMerce`),
  ADD KEY `idMerce` (`idMerce`);

--
-- Indici per le tabelle `venduto`
--
ALTER TABLE `venduto`
  ADD PRIMARY KEY (`idVenditore`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `merce`
--
ALTER TABLE `merce`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `compra`
--
ALTER TABLE `compra`
  ADD CONSTRAINT `compra_ibfk_1` FOREIGN KEY (`emailUtente`) REFERENCES `utenti` (`email`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `compra_ibfk_2` FOREIGN KEY (`idMerce`) REFERENCES `merce` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limiti per la tabella `recensione`
--
ALTER TABLE `recensione`
  ADD CONSTRAINT `recensione_ibfk_1` FOREIGN KEY (`emailAcquirente`) REFERENCES `utenti` (`email`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `recensione_ibfk_2` FOREIGN KEY (`emailVenditore`) REFERENCES `utenti` (`email`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Limiti per la tabella `vende`
--
ALTER TABLE `vende`
  ADD CONSTRAINT `vende_ibfk_1` FOREIGN KEY (`emailUtente`) REFERENCES `utenti` (`email`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `vende_ibfk_2` FOREIGN KEY (`idMerce`) REFERENCES `merce` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
