-- phpMyAdmin SQL Dump
-- version 4.5.5.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2016-03-20 23:39:35
-- 服务器版本： 5.5.47-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project-sally`
--

-- --------------------------------------------------------

--
-- 表的结构 `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `for_sale` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `goods`
--

CREATE TABLE `goods` (
  `id` int(11) NOT NULL,
  `barcode` varchar(14) DEFAULT NULL,
  `title` varchar(100) NOT NULL,
  `category_id` int(11) NOT NULL,
  `price` float NOT NULL DEFAULT '0',
  `old_price` float NOT NULL DEFAULT '0',
  `sold_count` int(11) NOT NULL DEFAULT '0',
  `stock_count` int(11) NOT NULL DEFAULT '0',
  `rate` float NOT NULL DEFAULT '0',
  `rate_count` int(11) NOT NULL DEFAULT '0',
  `add_dt` datetime DEFAULT NULL,
  `pic` varchar(255) DEFAULT NULL,
  `for_sale` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `receiver_name` varchar(20) NOT NULL,
  `receiver_addr` varchar(100) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `total_price` float NOT NULL DEFAULT '0',
  `rate` float NOT NULL DEFAULT '0',
  `handled` tinyint(1) NOT NULL DEFAULT '0',
  `completed` tinyint(1) NOT NULL DEFAULT '0',
  `place_dt` datetime NOT NULL,
  `complete_dt` datetime DEFAULT NULL,
  `handle_dt` datetime DEFAULT NULL,
  `closed` tinyint(1) NOT NULL DEFAULT '0',
  `close_dt` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `sold_goods`
--

CREATE TABLE `sold_goods` (
  `id` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `deal_price` float NOT NULL DEFAULT '0',
  `rate` float NOT NULL DEFAULT '0',
  `amount` int(11) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `categories_id_uindex` (`id`),
  ADD UNIQUE KEY `categories_title_uindex` (`title`);

--
-- Indexes for table `goods`
--
ALTER TABLE `goods`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `goods_id_uindex` (`id`),
  ADD UNIQUE KEY `goods_title_uindex` (`title`),
  ADD UNIQUE KEY `goods_barcode_uindex` (`barcode`),
  ADD KEY `goods_categories_id_fk` (`category_id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `orders_id_uindex` (`id`);

--
-- Indexes for table `sold_goods`
--
ALTER TABLE `sold_goods`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `sold_goods_id_uindex` (`id`),
  ADD KEY `sold_goods_goods_id_fk` (`goods_id`),
  ADD KEY `sold_goods_orders_id_fk` (`order_id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- 使用表AUTO_INCREMENT `goods`
--
ALTER TABLE `goods`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
--
-- 使用表AUTO_INCREMENT `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
--
-- 使用表AUTO_INCREMENT `sold_goods`
--
ALTER TABLE `sold_goods`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
--
-- 限制导出的表
--

--
-- 限制表 `goods`
--
ALTER TABLE `goods`
  ADD CONSTRAINT `goods_categories_id_fk` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`);

--
-- 限制表 `sold_goods`
--
ALTER TABLE `sold_goods`
  ADD CONSTRAINT `sold_goods_goods_id_fk` FOREIGN KEY (`goods_id`) REFERENCES `goods` (`id`),
  ADD CONSTRAINT `sold_goods_orders_id_fk` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
