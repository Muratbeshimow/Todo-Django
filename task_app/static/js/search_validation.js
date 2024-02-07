function validateSearchForm() {
    let searchInput = document.getElementById('search-area').value;
    if (searchInput.trim() === '') {
        document.getElementById('search-area').style.backgroundColor = 'pink';
        alert('Empty Search');
        return false;
    } else {
        document.getElementById('search-area').style.backgroundColor = '';
        return true;
    }
}
