document.addEventListener("DOMContentLoaded", function () {

    console.log("Personal Blog ishlayapti!");

    // Menu linklarini bosganda

    const links = document.querySelectorAll("nav a");

    links.forEach(function (link) {

        link.addEventListener("click", function () {

            console.log("Sahifaga o'tildi:", link.textContent.trim());

        });

    });

});