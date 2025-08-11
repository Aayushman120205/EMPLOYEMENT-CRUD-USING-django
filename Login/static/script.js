document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector('#login');

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const email = document.getElementById('email').value;
        const pin = document.getElementById('Pin').value;

        if (!email || !pin) {
            alert("❗ Please enter both email and password.");
            return;
        }
        fetch("http://127.0.0.1:8000/api/getall-employees/")
            .then(response => response.json())
            .then(data => {
                const user = data.find(emp =>
                    emp.Email === email && emp.Password === pin
                );
                if (user) {
                    // ✅ Login successful, redirect
                    window.location.href = "/LoggedIn/";
                } else {
                    // ❌ Invalid login
                    alert("Invalid Email or Password");
                }
            })
            .catch(error => console.error("Error fetching employees:", error));
    });
});
