function verifygame(){
    fetch('/verifyordelete',{
        method: 'POST',
        body: JSON.stringify({
            task:'verify',
            game_id: document.querySelector('#game_id').value,
        })
    })
    window.location.replace("/unverifiedgames");
}
function deletegame(){
    fetch('/verifyordelete',{
        method: 'POST',
        body: JSON.stringify({
            task:'delete',
            game_id: document.querySelector('#game_id').value,
        })
    })
    window.location.replace("/unverifiedgames");
}