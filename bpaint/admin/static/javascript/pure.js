let pure = document.getElementById("pure");
let recipe = document.getElementById("recipe");
let name = document.getElementById("name");

let hidden_recipe = document.createElement("textarea")
hidden_recipe.hidden = true;
hidden_recipe.name = "recipe";
hidden_recipe.id = "recipe";
hidden_recipe.disabled = true;
recipe.parentElement.insertBefore(hidden_recipe, recipe);

pure.onclick = function() {ifChecked()};

function ifChecked() {
	if (pure.checked) {
		recipe.disabled = true;
		recipe.value = name.value;
		hidden_recipe.disabled = false;
		hidden_recipe.value = name.value;
	} else {
		recipe.disabled = false;
		hidden_recipe.disabled = true;
	}
}