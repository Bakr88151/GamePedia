document.addEventListener('DOMContentLoaded', ()=>{
    showlogin();
});
function showcreate(){
    const login = document.querySelector("#login");
    const create = document.querySelector('#create');
    create.style.display = 'block';
    login.style.display = 'none'; 
}
function showlogin(){
    const login = document.querySelector("#login");
    const create = document.querySelector('#create');
    create.style.display = "none";
    login.style.display = "block";
}