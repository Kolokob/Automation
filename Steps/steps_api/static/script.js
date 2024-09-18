document.addEventListener('DOMContentLoaded', function () {

    // Create Sender
    document.getElementById('create-sender-form').addEventListener('submit', function (e) {
        e.preventDefault();
        const email = document.getElementById('create-email').value;
        const password = document.getElementById('create-password').value;
        const country = document.getElementById('create-country').value;

        fetch('/create_sender', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password, country })
        })
        .then(response => response.json())
        .then(data => {
            let resultDiv = document.getElementById('create-result');
            resultDiv.textContent = '';
            if (data.message) {
                resultDiv.textContent = data.message;
            } else {
                resultDiv.textContent = 'Error: ' + data.error;
            }
        });
    });

    // Login
    document.getElementById('login-form').addEventListener('submit', function (e) {
        e.preventDefault();
        const email = document.getElementById('login-email').value;
        const password = document.getElementById('login-password').value;
        const country = document.getElementById('login-country').value;

        fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password, country })
        })
        .then(response => response.json())
        .then(data => {
            let resultDiv = document.getElementById('login-result');
            resultDiv.textContent = '';
            if (data.session_key) {
                resultDiv.textContent = 'Session Key: ' + data.session_key;
            } else {
                resultDiv.textContent = 'Error: ' + data.error;
            }
        });
    });

    // Get Token
    document.getElementById('get-token-form').addEventListener('submit', function (e) {
        e.preventDefault();
        const email = document.getElementById('token-email').value;
        const password = document.getElementById('token-password').value;
        const country = document.getElementById('token-country').value;
        const session_key = document.getElementById('token-session').value;

        fetch('/get_token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password, country, session_key })
        })
        .then(response => response.json())
        .then(data => {
            let resultDiv = document.getElementById('token-result');
            resultDiv.textContent = '';
            if (data.token) {
                resultDiv.textContent = 'Token: ' + data.token;
            } else {
                resultDiv.textContent = 'Error: ' + data.error;
            }
        });
    });

    // Logout
    document.getElementById('logout-form').addEventListener('submit', function (e) {
        e.preventDefault();
        const email = document.getElementById('logout-email').value;
        const password = document.getElementById('logout-password').value;
        const country = document.getElementById('logout-country').value;
        const session_key = document.getElementById('logout-session').value;

        fetch('/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password, country, session_key })
        })
        .then(response => response.json())
        .then(data => {
            let resultDiv = document.getElementById('logout-result');
            resultDiv.textContent = '';
            if (data.message) {
                resultDiv.textContent = data.message;
            } else {
                resultDiv.textContent = 'Error: ' + data.error;
            }
        });
    });

    // Update Profile
    document.getElementById('update-profile-form').addEventListener('submit', function (e) {
        e.preventDefault();
        const email = document.getElementById('update-email').value;
        const password = document.getElementById('update-password').value;
        const country = document.getElementById('update-country').value;
        const session_key = document.getElementById('update-session').value;
        const name = document.getElementById('update-name').value;
        const surname = document.getElementById('update-surname').value;
        const cell = document.getElementById('update-cell').value;
        const address_actual = document.getElementById('update-address').value;

        fetch('/update_profile', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password, country, session_key, name, surname, cell, address_actual })
        })
        .then(response => response.json())
        .then(data => {
            let resultDiv = document.getElementById('update-result');
            resultDiv.textContent = '';
            if (data.message) {
                resultDiv.textContent = data.message;
            } else {
                resultDiv.textContent = 'Error: ' + data.error;
            }
        });
    });
});
