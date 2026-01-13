





function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Make a POST request to your Flask login endpoint with username and password
    // Example using Fetch API:
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
    })
    .then(response => {
        if (response.ok) {
            // window.location.href = '/protected'; // Redirect to the protected resource
            window.location.href = '/dashboard'; 
        } else {
            // Handle login error
            console.error('Login failed');
        }
    })
    .catch(error => {
        console.error('Error during login:', error);
    });
}

function register() {
    const regUsername = document.getElementById('regUsername').value;
    const regPassword = document.getElementById('regPassword').value;
    const regFullname = document.getElementById('regFullName').value;
    const regEmail = document.getElementById('regEmail').value;

    // Make a POST request to your Flask register endpoint with username and password
    // Example using Fetch API:
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username: regUsername, password: regPassword, email:regEmail, fullname:regFullname}),
    })
    .then(response => {
        if (response.ok) {
            console.log('Registration successful');
            swal("Account Created !", "You can Now Login with your username & Password, Thanks For Registering", "success")
            .then(() => {
                // Redirect to the login page
                window.location.href = "/login";
              });

            // Optionally, you can auto-login the user after registration
            // Call the login() function with the registered credentials
        } else {
            // Handle registration error

            swal("Registeration Failed", "Fill all the Details", "error");
        }
    })
    .catch(error => {
        console.error('Error during registration:', error);
        swal("Contact us", "ankitmishra.letter@gmail.com", "error");
    });
}