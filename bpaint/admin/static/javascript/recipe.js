let pure = document.getElementById("pure");
let recipe = document.getElementById("recipe");

function ifChecked() {
	if (recipe) {
		if (pure.checked) {
			recipe.disabled = true;
		} else {
			recipe.disabled = false;
		}
	}

if (recipe) {
	pure.onclick = function() {ifChecked};
} else {
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
