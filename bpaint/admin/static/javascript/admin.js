let pure = document.getElementById("pure");
let recipe = document.getElementById("recipe");
let name = document.getElementById("name");
let hidden_recipe = document.createElement("select")
hidden_recipe.hidden = true;
hidden_recipe.name = "recipe";
hidden_recipe.id = "recipe";
hidden_recipe.disabled = true;

if (recipe) {
	recipe.parentElement.insertBefore(hidden_recipe, recipe);
	pure.onclick = function() {ifChecked()};
} else {
	let hidden_pure = document.createElement("select")
	hidden_pure.hidden = true;
	hidden_pure.name = "pure";
	hidden_pure.id = "pure";
	hidden_pure.checked = true;
	pure.checked = true;
	pure.disabled = true;
	pure.parentElement.insertBefore(hidden_pure, pure);
	ifChecked();
}

function ifChecked() {
	if (pure.checked) {
		recipe.disabled = true;
		hidden_recipe.disabled = false;
	} else {
		recipe.disabled = false;
		hidden_recipe.disabled = true;
	}
}