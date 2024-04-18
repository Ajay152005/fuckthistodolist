function addTask() {
    var input = document.getElementById("taskInput");
    var task = input.value.trim();

    if (task === ""){
        alert("Please enter a task!");
        return;
    }

    var ul = document.getElementById("taskList");
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(task));

    var completeButton = document.createElement("button");
    completeButton.appendChild(document.createTextNode("Complete"));
    completeButton.onclick = function() {
        this.parentElement.classList.toggle("completed");
    };
    li.appendChild(completeButton);

    var deleteButton = document.createElement("button");
    deleteButton.appendChild(document.createTextNode("Delete"));
    deleteButton.onclick = function() {
        this.parentElement.remove();
    };
    li.appendChild(deleteButton);

    ul.appendChild(li);
    input.value = "";
}