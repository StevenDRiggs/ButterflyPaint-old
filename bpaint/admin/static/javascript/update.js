let name = document.getElementById("name");
let hidden_name = document.createElement("input");

hidden_name.hidden = true;
hidden_name.name = "name";
hidden_name.id = "name";
hidden_name.type = "text";
hidden_name.value = name.value;

name.disabled = true;
name.parentElement.insertBefore(hidden_name, name);
