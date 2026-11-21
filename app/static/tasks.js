async function loadTasks() {
    const response = await fetch("/tasks");
    const tasks = await response.json();
    const list = document.getElementById("task-list");
    list.innerHTML = "";
    for (const task of tasks) {
        const li = document.createElement("li");
        let text = task.title + " [" + task.priority + "]";
        if (task.deadline) {
            text = text + " до " + task.deadline;
        }
        if (task.is_done) {
            text = text + " — выполнена";
        }
        li.textContent = text;
        if (!task.is_done) {
            const button = document.createElement("button");
            button.textContent = "Выполнено";
            button.addEventListener("click", () => markDone(task.id));
            li.appendChild(button);
        }
        list.appendChild(li);
    }
}

async function createTask() {
    const title = document.getElementById("title").value;
    const priority = document.getElementById("priority").value;
    const deadline = document.getElementById("deadline").value;
    const body = { title: title, priority: priority };
    if (deadline) {
        body.deadline = deadline;
    }
    const response = await fetch("/create", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body)
    });
    const data = await response.json();
    if (response.ok) {
        document.getElementById("title").value = "";
        document.getElementById("deadline").value = "";
        document.getElementById("message").textContent = "";
        await loadTasks();
    } else {
        document.getElementById("message").textContent = data.error;
    }
}

async function markDone(taskId) {
    const response = await fetch("/tasks/" + taskId + "/done", {
        method: "POST"
    });
    const data = await response.json();
    if (response.ok) {
        await loadTasks();
    } else {
        document.getElementById("message").textContent = data.error;
    }
}

async function logout() {
    const response = await fetch("/logout", {
        method: "POST"
    });
    const data = await response.json();
    if (response.ok) {
        window.location.href = "/login";
    } else {
        document.getElementById("message").textContent = data.error;
    }
}

const create_btn = document.getElementById("create-btn");
create_btn.addEventListener("click", createTask);
const logout_btn = document.getElementById("logout-btn");
logout_btn.addEventListener("click", logout);
loadTasks();