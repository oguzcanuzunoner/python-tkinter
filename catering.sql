-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 11 Eyl 2020, 03:35:33
-- Sunucu sürümü: 10.4.14-MariaDB
-- PHP Sürümü: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `catering`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `musteriler`
--

CREATE TABLE `musteriler` (
  `id` int(8) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `sifre` varchar(8) NOT NULL,
  `ad` varchar(11) NOT NULL,
  `soyad` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `musteriler`
--

INSERT INTO `musteriler` (`id`, `mail`, `sifre`, `ad`, `soyad`) VALUES
(1, 'oguzcanuzunoner@icloud.com', '123456', 'Oğuzcan', 'Uzunöner'),
(2, 'deneme2@deneme.com', '123456', 'Canan', 'Arabacı'),
(3, 'deneme@deneme.com', '123456', 'Deneme', 'Hesabı');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `personel`
--

CREATE TABLE `personel` (
  `id` int(2) NOT NULL,
  `mail` varchar(50) NOT NULL,
  `sifre` int(8) NOT NULL,
  `ad` varchar(11) NOT NULL,
  `soyad` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `personel`
--

INSERT INTO `personel` (`id`, `mail`, `sifre`, `ad`, `soyad`) VALUES
(1, 'personel@personel.com', 123456, 'Personel', 'Hesabı');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `siparisler`
--

CREATE TABLE `siparisler` (
  `id` int(11) NOT NULL,
  `ad` varchar(11) NOT NULL,
  `soyad` varchar(11) NOT NULL,
  `menu` varchar(20) NOT NULL,
  `menu_adet` int(2) NOT NULL,
  `icecek` varchar(10) NOT NULL,
  `icecek_adet` varchar(3) NOT NULL,
  `toplam` int(11) NOT NULL,
  `katalog` varchar(5) NOT NULL,
  `adres` varchar(250) NOT NULL,
  `siparis_tarihi` datetime NOT NULL DEFAULT current_timestamp(),
  `musterimail` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `siparisler`
--

INSERT INTO `siparisler` (`id`, `ad`, `soyad`, `menu`, `menu_adet`, `icecek`, `icecek_adet`, `toplam`, `katalog`, `adres`, `siparis_tarihi`, `musterimail`) VALUES
(1, 'Oğuzcan', 'Uzunöner', 'Geleneksel Menü', 10, 'KOLA', '10', 840, 'Evet', 'Üniversite İktisadi ve İdari Bilimler Fakültesi Karadeniz Teknik Üniversitesi, 61080 Ortahisar/Trabzon\n', '2020-05-24 19:12:33', 'oguzcanuzunoner@icloud.com'),
(2, 'Oğuzcan', 'Uzunöner', 'Modern Sofra Menü', 4, 'LIMONATA', '2', 410, 'Hayır', 'Gülbaharhatun Mahallesi Kahramanmaraş Caddesi No:201\nTrabzon Büyükşehir Belediyesi - TRABZON / TÜRKİYE\n', '2020-05-24 19:13:07', 'oguzcanuzunoner@icloud.com'),
(3, 'Oğuzcan', 'Uzunöner', 'Kış Menü', 9, 'İÇECEK YOK', '0', 900, 'Hayır', 'Huzur Mh., Türk Telekom Arena Stadyumu, 34396 Sarıyer, İstanbul, Türkiye\n', '2020-05-24 19:14:11', 'oguzcanuzunoner@icloud.com'),
(4, 'Canan', 'Arabacı', 'Modern Sofra Menü', 4, 'FANTA', '3', 415, 'Hayır', 'Yeni Mahalle Uğur Mumcu Caddesi No:29 Çaycuma Belediyesi 67900 Çaycuma', '2020-05-24 19:15:21', 'deneme2@deneme.com'),
(5, 'Canan', 'Arabacı', 'Kış Menü', 4, 'AYRAN', '6', 430, 'Evet', 'Pazarkapı Mahallesi, Kahramanmaraş Caddesi, No:104\nORTAHİSAR-TRABZON / TÜRKİYE\n', '2020-05-24 19:16:44', 'deneme2@deneme.com'),
(6, 'Deneme', 'Hesabı', 'Kış Menü', 8, 'ICE TEA', '5', 800, 'Hayır', 'Üniversite, Milli Egemenlik Cd., 61080 Trabzon Merkez/Trabzon\n', '2020-05-24 19:17:58', 'deneme@deneme.com');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `musteriler`
--
ALTER TABLE `musteriler`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `mail` (`mail`);

--
-- Tablo için indeksler `personel`
--
ALTER TABLE `personel`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `siparisler`
--
ALTER TABLE `siparisler`
  ADD PRIMARY KEY (`id`),
  ADD KEY `f_key` (`musterimail`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `musteriler`
--
ALTER TABLE `musteriler`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Tablo için AUTO_INCREMENT değeri `personel`
--
ALTER TABLE `personel`
  MODIFY `id` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Tablo için AUTO_INCREMENT değeri `siparisler`
--
ALTER TABLE `siparisler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
