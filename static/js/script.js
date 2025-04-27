// TOAST
document.addEventListener('DOMContentLoaded', function () {
    const toastElList = document.querySelectorAll('.toast');
    const toastList = [...toastElList].map(toastEl => new bootstrap.Toast(toastEl));
    toastList.forEach(toast => toast.show());
});

// Delete modal
document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('open_modal') === '1') {
        const deleteModalButton = document.getElementById('deleteModalButton');
        deleteModalButton.click();
    }
    if (urlParams.get('open_modal') === '2') {
        const backButton = document.getElementById('backButtonModal');
        backButton.click();
    }
});