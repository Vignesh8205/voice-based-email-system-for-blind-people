-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 07, 2022 at 08:55 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `voice_email`
--

-- --------------------------------------------------------

--
-- Table structure for table `compose`
--

CREATE TABLE `compose` (
  `id` int(10) NOT NULL,
  `fromid` varchar(20) NOT NULL,
  `subject` varchar(200) NOT NULL,
  `toid` varchar(20) NOT NULL,
  `readmsg` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `compose`
--

INSERT INTO `compose` (`id`, `fromid`, `subject`, `toid`, `readmsg`) VALUES
(1, '1001', 'welcome ko vi bhej di maine', '1003', '1'),
(2, '1003', 'welcome to voice busy meaning', '1001', '1'),
(3, '1003', 'where are you from', '1001 1001', '1'),
(4, '2003', '1001', '1001', '1'),
(5, '1003', 'hi how are you', '1001', '1'),
(6, '1003', 'projects working successfully', '1001', '1'),
(7, '1003', 'hi how are you', '1004', '1'),
(8, '1005', 'hi how are you where are you from', '1004', '1');

-- --------------------------------------------------------

--
-- Table structure for table `register_user`
--

CREATE TABLE `register_user` (
  `id` int(10) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `DOB` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register_user`
--

INSERT INTO `register_user` (`id`, `name`, `email`, `DOB`) VALUES
(1001, 'df', 'df', 'df'),
(1002, 'df', 'df', 'df'),
(1003, 'shaikh', 'sha@gmail.com', '10/10/10'),
(1004, 'divya', 'divyakavya2829@gmail.com', '11/28/98'),
(1005, 'ddd', 'ddd', '5/7/22');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `compose`
--
ALTER TABLE `compose`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `register_user`
--
ALTER TABLE `register_user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `compose`
--
ALTER TABLE `compose`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `register_user`
--
ALTER TABLE `register_user`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1006;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
