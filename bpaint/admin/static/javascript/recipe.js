let pure = document.getElementById("pure-display");
let recipe = document.getElementsByClassName("recipe");

let hidden_pure = document.createElement("select");
hidden_pure.hidden = true;
hidden_pure.name = "pure";
hidden_pure.id = "pure";


function ifChecked() {
	if (recipe.length > 0) {
		for (let i = 0; i < recipe.length; i++) {
			if (pure.checked) {
				recipe[i].hidden = true;
				document.querySelector("label[for='submit2']").hidden = true;
				document.getElementById('submit2').hidden = true;
			} else {
				recipe[i].hidden = false;
				document.querySelector("label[for='submit2']").hidden = false;
				document.getElementById('submit2').hidden = false;
			}
		}
	} else {
		hidden_pure.checked = true;
		pure.checked = true;
		pure.disabled = true;
		pure.parentElement.insertBefore(hidden_pure, pure);
	}
}

pure.onclick = function() {ifChecked()};
ifChecked();
