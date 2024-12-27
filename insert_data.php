<?php
include 'db_connect.php';

// Dades dels fons
$funds = [
    [
        'ISIN' => 'LU1295551144',
        'Nom' => 'Capital Group New Perspective Fund',
        'Tipus' => 'SICAV',
        'ObjectiuInversio' => 'Generar un creixement a llarg termini del capital. Inversió en empreses de tot el món inclosos mercats emergents.',
        'ClassificacioESG' => 'Article 8 - ESG',
        'DivisaReferencia' => 'EUR',
        'DataPublicacio' => '2024-11-13',
        'Gestor' => 'Capital International Management Company Sàrl',
        'Domicili' => 'Luxemburg',
        'EnllacFollet' => 'www.capitalgroup.com'
    ],
    [
        'ISIN' => 'LU0232524495',
        'Nom' => 'AB SICAV I – American Growth Portfolio',
        'Tipus' => 'Fons de capital variable',
        'ObjectiuInversio' => 'Revaloritzar la inversió mitjançant el creixement del capital. Inversió en empreses nord-americanes.',
        'ClassificacioESG' => 'Article 8 - ESG',
        'DivisaReferencia' => 'EUR',
        'DataPublicacio' => '2024-02-29',
        'Gestor' => 'AllianceBernstein (Luxembourg) S.à r.l.',
        'Domicili' => 'Luxemburg',
        'EnllacFollet' => 'www.alliancebernstein.com'
    ],
    [
        'ISIN' => 'LU0171307068',
        'Nom' => 'BGF World Healthscience Fund',
        'Tipus' => 'Renda variable',
        'ObjectiuInversio' => 'Maximitzar la rendibilitat invertint en empreses del sector sanitari, farmacèutic, i biotecnologia.',
        'ClassificacioESG' => 'Article 8 - ESG',
        'DivisaReferencia' => 'EUR',
        'DataPublicacio' => '2024-11-30',
        'Gestor' => 'BlackRock (Luxembourg) S.A.',
        'Domicili' => 'Luxemburg',
        'EnllacFollet' => 'www.blackrock.com'
    ]
];

// Inserció dels fons
foreach ($funds as $fund) {
    $sql = "INSERT INTO Funds (ISIN, Nom, Tipus, ObjectiuInversio, ClassificacioESG, DivisaReferencia, DataPublicacio, Gestor, Domicili, EnllacFollet)
            VALUES (
                '{$fund['ISIN']}', 
                '{$fund['Nom']}', 
                '{$fund['Tipus']}', 
                '{$fund['ObjectiuInversio']}', 
                '{$fund['ClassificacioESG']}', 
                '{$fund['DivisaReferencia']}', 
                '{$fund['DataPublicacio']}', 
                '{$fund['Gestor']}', 
                '{$fund['Domicili']}', 
                '{$fund['EnllacFollet']}'
            )";

    if ($conn->query($sql) === TRUE) {
        echo "Fons inserit: " . $fund['Nom'] . "<br>";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error . "<br>";
    }
}

$conn->close();
?>