document.addEventListener('DOMContentLoaded', () => {
    const openbutton = document.querySelector('#logout');
    const modal = document.querySelector("[data-modal]");
    const closebutton = document.querySelector("[data-close-modal]");
    openbutton.addEventListener('click', () => {
        modal.style.display = 'block';
        modal.showModal();
    })
    closebutton.addEventListener('click', () => {
        modal.style.display = 'none';
        modal.close();
    })
})
$(document).ready(function() {
    $(".dropdown-toggle").dropdown();
});

