-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 20 Jul 2024 pada 17.06
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpustakaan`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `buku`
--

CREATE TABLE `buku` (
  `id` int(11) NOT NULL,
  `judul` varchar(255) NOT NULL,
  `penulis` varchar(255) NOT NULL,
  `penerbit` varchar(255) DEFAULT NULL,
  `tahun_terbit` int(11) DEFAULT NULL,
  `konten` text NOT NULL,
  `iktisar` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `buku`
--

INSERT INTO `buku` (`id`, `judul`, `penulis`, `penerbit`, `tahun_terbit`, `konten`, `iktisar`) VALUES
(1, 'Belajar Python', 'John Doe', 'Teknologi Press', 2021, 'Bab 1: Pengantar Python;Bab 2: Struktur Data;Bab 3: Pemrograman OOP', 'Buku ini menjelaskan dasar-dasar pemrograman Python secara komprehensif.'),
(2, 'Data Science dengan Python', 'Jane Smith', 'Insight Publishers', 2022, 'Bab 1: Statistik;Bab 2: Pembelajaran Mesin;Bab 3: Visualisasi Data', 'Panduan praktis untuk analisis data dan machine learning dengan Python.'),
(3, 'Web Development 101', 'Alex Johnson', 'Web Creators', 2023, 'Bab 1: HTML;Bab 2: CSS;Bab 3: JavaScript', 'Panduan dasar untuk memulai pengembangan web dari HTML hingga JavaScript.'),
(4, 'Machine Learning Basics', 'Emily Davis', 'AI Publishers', 2024, 'Bab 1: Pembelajaran Supervised;Bab 2: Pembelajaran Tidak Terawasi;Bab 3: Pembelajaran Mendalam', 'Pengantar konsep dan teknik dasar dalam machine learning.'),
(5, 'Pengantar Statistik', 'Michael Brown', 'Statistics World', 2020, 'Bab 1: Statistik Deskriptif;Bab 2: Inferensi Statistik;Bab 3: Analisis Regresi', 'Buku ini memberikan panduan komprehensif tentang metode statistik dasar dan lanjutan.');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `buku`
--
ALTER TABLE `buku`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
