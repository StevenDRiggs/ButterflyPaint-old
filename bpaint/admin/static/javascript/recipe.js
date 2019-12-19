let pure = document.querySelector('#pure');
let visible_pure = document.querySelector('#visible-pure');
let recipe = document.querySelectorAll('.recipe');

document.querySelector('label[for="pure"]').hidden = true;
pure.hidden = true;


function ifChecked() {
	pure.checked = visible_pure.checked;
	pure.value = pure.checked
	
	if (recipe.length > 0) {
		for (let i = 0; i < recipe.length; i++) {
			if (pure.checked) {
				recipe[i].hidden = true;
				document.querySelector('label[for="submit2"]').hidden = true;
				document.querySelector('#submit2').hidden = true;
			} else {
				recipe[i].hidden = false;
				document.querySelector('label[for="submit2"]').hidden = false;
				document.querySelector('#submit2').hidden = false;
			}
		}
	} else {
		visible_pure.checked = true;
		visible_pure.disabled = true;
	}
}

visible_pure.onclick = function() {ifChecked()};
ifChecked();
ifChecked();