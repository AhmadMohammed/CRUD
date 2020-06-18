-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql12.freemysqlhosting.net
-- Generation Time: Jun 18, 2020 at 08:03 PM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sql12348567`
--
CREATE DATABASE IF NOT EXISTS `sql12348567` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `sql12348567`;

-- --------------------------------------------------------

--
-- Table structure for table `content`
--

CREATE TABLE `content` (
  `id` int(11) NOT NULL,
  `contributor` varchar(255) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `article` longblob NOT NULL,
  `picture` longblob NOT NULL,
  `sound` longblob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `groups`
--

CREATE TABLE `groups` (
  `id` int(11) NOT NULL,
  `groups` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `groups`
--

INSERT INTO `groups` (`id`, `groups`) VALUES
(1, 'A'),
(3, 'Z');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `group` varchar(255) NOT NULL,
  `Reporter` varchar(255) NOT NULL,
  `subject` varchar(255) NOT NULL,
  `tag` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`group`, `Reporter`, `subject`, `tag`) VALUES
('', 'Ahmad', 'CAD', 'Software'),
('', 'Parwiz', 'Gears', 'Mechanics'),
('', 'Ahmad', 'Nuclear Energy', 'Energy');

-- --------------------------------------------------------

--
-- Table structure for table `reporters`
--

CREATE TABLE `reporters` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `groups` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reporters`
--

INSERT INTO `reporters` (`id`, `name`, `groups`, `email`, `password`) VALUES
(3, 'Parwiz', 'A', 'parwiz.f@gmail.com', '1'),
(5, 'Karimja', 'B', 'ka@gmail.com', '1'),
(6, 'Jamal', 'B', 'ja@gmail.com', '1'),
(7, 'Nawid', 'B', 'na@gmail.com', '1'),
(12, 'Tom Logan', 'B', 'tom@gmail.com', '1'),
(13, 'Fawad', 'B', 'fa@gmail.com', '1'),
(14, 'Ahmad', 'Z', 'A@gmail.com', '1'),
(22, 'Turki', 'Z', 'Tu@gmail.com', '1'),
(23, 'Raad', 'Z', 'R@gmail.com', '1'),
(24, 'Shehab', 'A', 'Shehab@gmail.com', '1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `content`
--
ALTER TABLE `content`
  ADD KEY `subject` (`subject`),
  ADD KEY `contributor` (`contributor`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `groups`
--
ALTER TABLE `groups`
  ADD KEY `groups` (`groups`),
  ADD KEY `id` (`id`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD KEY `Reporter` (`Reporter`),
  ADD KEY `subject` (`subject`),
  ADD KEY `group` (`group`);

--
-- Indexes for table `reporters`
--
ALTER TABLE `reporters`
  ADD PRIMARY KEY (`id`),
  ADD KEY `groups` (`groups`),
  ADD KEY `name` (`name`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `content`
--
ALTER TABLE `content`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `groups`
--
ALTER TABLE `groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `reporters`
--
ALTER TABLE `reporters`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `groups`
--
ALTER TABLE `groups`
  ADD CONSTRAINT `groups_ibfk_1` FOREIGN KEY (`groups`) REFERENCES `reporters` (`groups`);

--
-- Constraints for table `post`
--
ALTER TABLE `post`
  ADD CONSTRAINT `post_ibfk_1` FOREIGN KEY (`Reporter`) REFERENCES `reporters` (`name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
