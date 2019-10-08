const update_form = document.querySelector('form');
update = update_form.elements['update'];
update.onclick = () => formPreLoad(update.value);

function formPreLoad(val) {
	document.location = document.location.href.split('?')[0] + '?rec_id=' + val;
}
