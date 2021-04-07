-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 07, 2021 at 04:05 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projectsikap`
--

-- --------------------------------------------------------

--
-- Table structure for table `applicant`
--

CREATE TABLE `applicant` (
  `id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `surname` varchar(100) NOT NULL,
  `user_type` int(11) NOT NULL,
  `isVerified` int(11) NOT NULL,
  `industry` varchar(100) NOT NULL,
  `region` varchar(100) NOT NULL,
  `province` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `age` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `applicant`
--

INSERT INTO `applicant` (`id`, `email`, `password`, `name`, `surname`, `user_type`, `isVerified`, `industry`, `region`, `province`, `city`, `age`) VALUES
(4, 'clive01@email.com', 'Thunder321', 'Clive', 'Robinson', 0, 1, 'Tech', 'VII', 'Cebu', 'Cebu', 37),
(5, 'martinD@email.com', 'Duncan007', 'Martin', 'Duncan', 0, 1, 'BPO', 'VII', 'Cebu', 'Lapu-Lapu', 40),
(6, 'preciousring@email.com', 'BilboB@ggins', 'Joey', 'Sutton', 0, 1, 'Commercial', 'VII', 'Cebu', 'Mandaue', 45),
(7, 'treesbegreen@email.com', 'saveLe3s', 'Aubrey', 'Robson', 0, 1, 'Education', 'VII', 'Cebu', 'Cebu', 18),
(8, 'wineLover@email.com', 'AddrianaWines', 'Wynne', 'Lane', 0, 1, 'Finance', 'VII', 'Cebu', 'Danao', 29),
(9, 'brownBear@email.com', 'DwightLight', 'Eileen', 'Meskill', 0, 1, 'Commercial', 'VII', 'Cebu', 'Compostella', 23),
(10, 'beerlover@email.com', 'RedHorse', 'Gina', 'Thornton', 0, 1, 'Tech', 'VII', 'Cebu', 'Bogo', 36),
(11, 'alamatngibon@email.com', 'IbongAdarna', 'Dakila', 'Aguilar', 0, 1, 'Tech', 'VII', 'Cebu', 'Bogo', 35),
(12, 'awitngtanghalan@email.com', 'ArnelTheJudge', 'Arnel', 'Valdez', 0, 1, 'Tech', 'VII', 'Cebu', 'Lapu-Lapu', 38),
(13, 'theAgbayani@email.com', 'Otso8', 'Bayani', 'DeGuzman', 0, 1, 'Education', 'VII', 'Cebu', 'Danao', 20),
(14, 'notEBulaga@email.com', 'OriginalRiza', 'Riza', 'Cook', 0, 1, 'Tourism', 'VII', 'Cebu', 'Mandaue', 37),
(15, 'bballLife@email.com', 'FemaleJovit', 'Jovelyn', 'Ortiz', 0, 1, 'Commercial', 'VII', 'Cebu', 'Cebu', 27),
(16, 'whoframed@email.com', 'RogerRabbit', 'Roger', 'Magallanes', 0, 1, 'BPO', 'VII', 'Cebu', 'Cebu', 23),
(17, 'maroonandgold@email.com', 'HindiAkoProf', 'Elmer', 'Carandang', 0, 1, 'Education', 'VII', 'Cebu', 'Toledo', 37),
(18, 'womanofsteel@email.com', 'GreatPower', 'Layne', 'Dilag', 0, 1, 'Tourism', 'VII', 'Cebu', 'Naga', 39);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `applicant`
--
ALTER TABLE `applicant`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `applicant`
--
ALTER TABLE `applicant`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
