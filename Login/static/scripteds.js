document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('Save').addEventListener('click', async function () {
        const firstName = document.getElementById("First_Name").value.trim();
        const lastName = document.getElementById("Last_Name").value.trim();
        const email = document.getElementById("email").value.trim();
        const contact = document.getElementById("contact").value.trim();
        const date = document.getElementById("dateofjoining").value.trim();
        const password = document.getElementById('security').value;
        
        if (!firstName || !lastName || !email || !contact || !date || !password) {
            alert("❗ All fields are required.");
            return;
        }

        const phonePattern = /^(\+91)?\d{10}$/;
        if (!phonePattern.test(contact)) {
            alert("❌ Contact must be 10 digits, optionally starting with +91.");
            return;
        }

        const data = {
            First_Name: firstName,
            Last_Name: lastName,
            Email: email,
            Contact: contact,
            Date_of_Joining: date,
            Password:password,
        };

        try {
            const response = await fetch("http://127.0.0.1:8000/api/create-employees/", {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken()
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (response.ok) {
                alert("✅ Employee created successfully!");
                location.reload();
            } else {
                if (result.Email) {
                    alert("❗ Please enter a valid Email.");
                } else if (result.Contact) {
                    alert("❗ This contact number is invalid or already exists.");
                } else if (result.First_Name || result.Last_Name) {
                    alert("❗ Please enter a valid first and last name.");
                } else if (result.Date_of_Joining) {
                    alert("❗ Please enter a valid date of joining.");
                } else {
                    alert("❌ Something went wrong. Please check your inputs and try again."+ JSON.stringify(result));
                }
            }
        } catch (error) {
            alert("❌ Request failed: " + error);
            location.reload();
        }
    });
});

function getCSRFToken() {
    let name = "csrftoken=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let cookies = decodedCookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      let c = cookies[i].trim();
      if (c.indexOf(name) === 0) return c.substring(name.length, c.length);
    }
    return "";
}