function validateForm() {
    let titleInput = document.getElementById('id_title');
    let descriptionInput = document.getElementById('id_description');
    let categoryInput = document.getElementById('id_category');

    if (titleInput.value.trim() === '') {
        highlightField(titleInput);
        return false;
    } else {
        resetField(titleInput);
    }

    if (descriptionInput.value.trim() === '') {
        highlightField(descriptionInput);
        return false;
    } else {
        resetField(descriptionInput);
    }

    if (categoryInput.value.trim() === '') {
        highlightField(categoryInput);
        return false;
    } else {
        resetField(categoryInput);
    }

    return true;
}

function highlightField(field) {
    field.style.backgroundColor = 'pink';
}

function resetField(field) {
    field.style.backgroundColor = '';
}

