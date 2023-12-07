document.addEventListener('DOMContentLoaded', () => {
    ratingcolor();
})

function postreview(){
    const ratingfield = document.querySelector('.rating_input');
    const reviewfield = document.querySelector('.rating_review');
    if(ratingfield.value != '' && reviewfield.value != ''){
        fetch('/postrating',{
            method: 'POST',
            body: JSON.stringify({
                task:'post',
                game_id: document.querySelector('#game_id').value,
                rating: ratingfield.value,
                review: reviewfield.value,
            })
        })
        document.querySelector('.userreviewrating').innerHTML = document.querySelector('.rating_input').value;
        document.querySelector('.userreviewtext').innerHTML = document.querySelector('.rating_review').value;
        document.querySelector('.user_review').style.display = 'grid';
        document.querySelector('.review_form').style.display = 'none';
    }else{
        alert('please make sure that your Rating and review are valid')
    }
}

function changereviewview(){
    const user_review = document.querySelector('.user_review');
    user_review.style.display = 'none';
    document.querySelector('.review_form').style.display = 'grid';
    document.querySelector('.rating_input').value = document.querySelector('.userreviewrating').innerHTML;
    document.querySelector('.rating_review').value = document.querySelector('.userreviewtext').innerHTML;
}

function changereview(){
    const ratingfield = document.querySelector('.rating_input');
    const reviewfield = document.querySelector('.rating_review');
    if(ratingfield.value != '' && reviewfield.value != ''){
        fetch('/postrating',{
            method: 'POST',
            body: JSON.stringify({
                task:'change',
                game_id: document.querySelector('#game_id').value,
                rating: ratingfield.value,
                review: reviewfield.value,
            })
        })
        document.querySelector('.userreviewrating').innerHTML = document.querySelector('.rating_input').value;
        document.querySelector('.userreviewtext').innerHTML = document.querySelector('.rating_review').value;
        document.querySelector('.user_review').style.display = 'grid';
        document.querySelector('.review_form').style.display = 'none';
    }else{
        alert('please make sure that your Rating and review are valid')
    }
}

function ratingcolor(){
    const mainrating = document.querySelector('.rating');
    if (mainrating.innerHTML >= 7){
        mainrating.style.backgroundColor = '#2dd62d';
    }else if(mainrating.innerHTML >= 5){
        mainrating.style.backgroundColor = '#ffe600';  
    }
    else{
        mainrating.style.backgroundColor = '#ff0000';
    }
    document.querySelectorAll('.userreviewrating').forEach(item => {
        if (item.innerHTML >= 7){
            item.style.backgroundColor = '#2dd62d';
        }else if(item.innerHTML >= 5){
            item.style.backgroundColor = '#ffe600';  
        }
        else{
            item.style.backgroundColor = '#ff0000';
        }
    })
}

function playlistchange(){
    const button = document.querySelector('.wl')
    if (button.dataset.add == 'False'){
        fetch('/addtopl',{
            method: 'POST',
            body: JSON.stringify({
                task:'add',
                game_id: document.querySelector('#game_id').value,
            })
        })
        button.dataset.add = 'True';
    }else{
        fetch('/addtopl',{
            method: 'POST',
            body: JSON.stringify({
                task:'remove',
                game_id: document.querySelector('#game_id').value,
            })
        })
        button.dataset.add = 'False';
    }

}
