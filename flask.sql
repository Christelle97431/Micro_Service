-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : dim. 08 jan. 2023 à 13:39
-- Version du serveur : 5.7.36
-- Version de PHP : 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `flask`
--

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` text NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=MyISAM AUTO_INCREMENT=93 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`, `created_at`, `updated_at`) VALUES
(92, 'hokaketo', 'sivigeg@mailinator.com', 'b2fe8b46929bfa4c65fee9d5d43a2423799b18e360782e9abc27bd420877243e', '2023-01-08 17:31:13', '2023-01-08 17:31:13'),
(90, 'tugowy', 'repovil@mailinator.com', 'b2fe8b46929bfa4c65fee9d5d43a2423799b18e360782e9abc27bd420877243e', '2023-01-08 16:57:22', '2023-01-08 16:57:22'),
(9, 'garec', 'voxytalody@mailinator.com', 'b2fe8b46929bfa4c65fee9d5d43a2423799b18e360782e9abc27bd420877243e', '2022-12-18 22:58:28', '2022-12-18 22:58:28'),
(7, 'nidib', 'dijo@mailinator.com', 'b2fe8b46929bfa4c65fee9d5d43a2423799b18e360782e9abc27bd420877243e', '2022-12-18 22:48:08', '2022-12-18 22:48:08'),
(4, 'kyfixogahi', 'paviw@mailinator.com', 'b2fe8b46929bfa4c65fee9d5d43a2423799b18e360782e9abc27bd420877243e', '2022-12-18 22:47:57', '2022-12-18 22:47:57'),
(5, 'pykid', 'pyhepo@mailinator.com', 'b2fe8b46929bfa4c65fee9d5d43a2423799b18e360782e9abc27bd420877243e', '2022-12-18 22:48:00', '2022-12-18 22:48:00'),
(6, 'detiny', 'witonokef@mailinator.com', 'b2fe8b46929bfa4c65fee9d5d43a2423799b18e360782e9abc27bd420877243e', '2022-12-18 22:48:04', '2022-12-18 22:48:04'),
(2, 'celyrotoqi', 'tylunobi@mailinator.com', 'b2fe8b46929bfa4c65fee9d5d43a2423799b18e360782e9abc27bd420877243e', '2022-12-18 22:47:39', '2022-12-18 22:47:39'),
(3, 'lamufuwo', 'qyvoq@mailinator.com', 'b2fe8b46929bfa4c65fee9d5d43a2423799b18e360782e9abc27bd420877243e', '2022-12-18 22:47:45', '2022-12-18 22:47:45'),
(91, 'lomabix', 'rusoqiluji@mailinator.com', 'b2fe8b46929bfa4c65fee9d5d43a2423799b18e360782e9abc27bd420877243e', '2023-01-08 16:57:55', '2023-01-08 16:57:55'),
(1, 'test', 'test@gmail.com', 'cd7bc9bddc5435bd1c01941bc5c234c14083d092167fe68296f5d91c81e42106', '2023-01-08 14:55:03', '2023-01-08 14:55:03'),
(8, 'zzz', 'zzz@gmail.com', 'cd7bc9bddc5435bd1c01941bc5c234c14083d092167fe68296f5d91c81e42106', '2022-12-18 22:58:24', '2022-12-18 22:58:24');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
