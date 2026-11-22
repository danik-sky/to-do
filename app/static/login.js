async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const response = await fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: username, password: password })
    });
    const data = await response.json();
    if (response.ok) {
        window.location.href = "/";
    } else {
        document.getElementById("message").textContent = data.error;
    }
}

async function register() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const response = await fetch("/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: username, password: password })
    });
    const data = await response.json();
    if (response.ok) {
        document.getElementById("message").textContent = "Регистрация успешна, войдите";
    } else {
        document.getElementById("message").textContent = data.error;
    }
}

const login_btn = document.getElementById("login-btn");
login_btn.addEventListener("click", login);
const register_btn = document.getElementById("register-btn");
register_btn.addEventListener("click", register);