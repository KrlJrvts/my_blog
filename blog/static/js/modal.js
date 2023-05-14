function closeModalAndRedirect() {
    const city = document.getElementById("city");
    city.value = "";

    window.location.href = 'http://127.0.0.1:8000/';
}

document.addEventListener('DOMContentLoaded', function () {
    const closeButtonModal = document.getElementById('btn-close-footer');
    closeButtonModal.addEventListener('click', function () {
        closeModalAndRedirect();
    });
    const closeButtonFooter = document.getElementById('btn-close-modal');
    closeButtonFooter.addEventListener('click', function () {
        closeModalAndRedirect();
    });
});
