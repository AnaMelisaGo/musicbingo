// Delete modal
document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('open_modal') === '1') {
        /* const deleteModal = document.getElementById('deleteModal');
        const modal = new bootstrap.Modal(deleteModal, {
            backdrop: 'static',
            keyboard: false
        });
        modal.show(); */
        const deleteModalButton = document.getElementById('deleteModalButton');
        deleteModalButton.click();
        /* alert('Hello!'); */
    }
});