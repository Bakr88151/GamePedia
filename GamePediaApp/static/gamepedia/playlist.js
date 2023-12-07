document.addEventListener("DOMContentLoaded", ()=>{
    loadgames(page_number)
})
var page_number = 1

function loadgames(num){
    const games = document.querySelector('.games');
    fetch(`/getplaylist/${num}`)
    .then(response => response.json())
    .then(result => {
        result.forEach(element => {
            const link = document.createElement('a');
            link.href = `/game/${element.id}`;
            link.className = 'gameanchor';
            const container = document.createElement('div');
            container.className = 'card';
            const img_container = document.createElement('div');
            img_container.className = "img_container";
            const img = document.createElement('img');
            img.className = 'card-img-top';
            img.src = element.poster;
            const card_body = document.createElement('div');
            card_body.className = 'card-body';
            const title = document.createElement('h5');
            title.className = 'card-title';
            title.innerHTML = element.title;
            const genres = document.createElement('p');
            genres.className = 'card-text';
            genres.innerHTML = element.genres.toString().replaceAll(',', ', ');
            const rating = document.createElement('p');
            rating.className = 'rating';
            rating.innerHTML = `${element.avg_rating}`;
            container.append(img_container)
            if (rating.innerHTML >= 7){
                container.dataset.color = 'green';
            }else if(rating.innerHTML >= 5){
                container.dataset.color = 'yellow';  
            }
            else{
                container.dataset.color = 'red';
            }
            img_container.append(img);
            card_body.append(title);
            card_body.append(genres);
            card_body.append(rating);
            container.append(card_body);
            link.append(container);
            games.append(link);
            ratingcolor(rating);
        });
    })
    page_number += 1
}

function ratingcolor(item){
    if (item.innerHTML >= 7){
        item.style.color = '#2dd62d';
    }else if(item.innerHTML >= 5){
        item.style.color = '#ffe600';  
    }
    else{
        item.style.color = '#ff0000';
    }
}
