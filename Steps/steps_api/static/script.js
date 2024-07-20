document.addEventListener('DOMContentLoaded', function () {
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
            document.getElementById('create-result').textContent = data.message || data.error;
        });
    });

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
            document.getElementById('login-result').textContent = data.session_key || data.error;
        });
    });

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
            document.getElementById('token-result').textContent = data.token || data.error;
        });
    });

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
            document.getElementById('logout-result').textContent = data.message || data.error;
        });
    });

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
            document.getElementById('update-result').textContent = data.message || data.error;
        });
    });
});
