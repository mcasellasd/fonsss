document.addEventListener("DOMContentLoaded", function () {
    const fundList = document.getElementById("fundList");

    // Carrega la llista de fons
    function loadFunds() {
        fetch("backend/fetch_data.php")
            .then(response => response.json())
            .then(data => {
                fundList.innerHTML = "";
                data.forEach(fund => {
                    const row = document.createElement("tr");

                    row.innerHTML = `
                        <td><input type="checkbox" class="fund-checkbox" data-id="${fund.FundID}"></td>
                        <td>${fund.FundID}</td>
                        <td>${fund.ISIN}</td>
                        <td>${fund.Nom}</td>
                        <td>${fund.Tipus}</td>
                    `;

                    fundList.appendChild(row);
                });
            });
    }

    // Gestiona la selecció
    fundList.addEventListener("change", function (e) {
        if (e.target.classList.contains("fund-checkbox")) {
            const fundID = e.target.dataset.id;
            if (e.target.checked) {
                console.log(`Fons seleccionat: ${fundID}`);
            } else {
                console.log(`Fons deseleccionat: ${fundID}`);
            }
        }
    });

    // Carrega els fons inicialment
    loadFunds();
});