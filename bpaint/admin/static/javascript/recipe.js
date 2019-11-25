let pure = document.getElementById("pure");
let recipe = document.getElementById("recipe");

function ifChecked() {
	if (recipe) {
		if (pure.checked) {
			recipe.hidden = true;
		} else {
			recipe.hidden = false;
		}
	}
}

pure.onclick = function() {ifChecked()};

if (!recipe) {
	let hidden_pure = document.createElement("select");
	hidden_pure.hidden = true;
	hidden_pure.name = "pure";
	hidden_pure.id = "pure";
	hidden_pure.checked = true;
	pure.checked = true;
	pure.disabled = true;
	pure.parentElement.insertBefore(hidden_pure, pure);
	ifChecked();
}
