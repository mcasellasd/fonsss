<?php
$servername = "localhost"; // Canvia-ho si el teu servidor no és localhost
$username = "root";        // Introdueix el teu usuari de MySQL
$password = "";            // Introdueix la teva contrasenya de MySQL

// Crear la connexió
$conn = new mysqli($servername, $username, $password);

// Comprovar la connexió
if ($conn->connect_error) {
    die("Connexió fallida: " . $conn->connect_error);
}

// Crear la base de dades si no existeix
$sql = "CREATE DATABASE IF NOT EXISTS InvestmentFundsDB";
if ($conn->query($sql) === TRUE) {
    echo "Base de dades creada o ja existeix.<br>";
} else {
    echo "Error en crear la base de dades: " . $conn->error . "<br>";
}

$conn->close();
?>