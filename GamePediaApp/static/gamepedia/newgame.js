document.addEventListener('DOMContentLoaded', ()=>{
    const dev_container = document.createElement('div')
    dev_container.className = 'searchbar_container';
    dev_container.id = 'dev_container';
    const dev_label = document.querySelector('[for="id_dev"]')
    dev_container.append(document.querySelector('#id_dev'));
    const pub_container = document.createElement('div')
    pub_container.className = 'searchbar_container';
    pub_container.id = 'pub_container';
    pub_container.append(document.querySelector('#id_pub'));
    const pub_label = document.querySelector('[for="id_pub"]')
    const ul = document.createElement('ul');
    ul.className = 'result_list';
    const ul1 = document.createElement('ul');
    ul1.className = 'result_list1';

    dev_container.append(ul);
    pub_container.append(ul1);
    document.querySelector('.form-group').append(dev_label)
    document.querySelector('.form-group').append(dev_container);
    document.querySelector('.form-group').append(pub_label)
    document.querySelector('.form-group').append(pub_container);

    const dev_input = document.querySelector('#id_dev');
    dev_input.addEventListener('input', () => quicksearch_dev());
    document.addEventListener('click',() => focus_searchdev())
    const dev_pub = document.querySelector('#id_pub');
    dev_pub.addEventListener('input', () => quicksearch_pub());
    document.addEventListener('click',() => focus_searchpub())
})

function quicksearch_dev() {
    const search_input = document.querySelector('#id_dev');
    const ul = document.querySelector('.result_list');
    ul.innerHTML = '';
    if (search_input.value != ''){
        fetch(`/quicksearchdev/${search_input.value}`)
        .then(response => response.json())
        .then(result => {
            if (Array.from(result).length > 0){
                ul.style.display = 'block'
                result.forEach(element => {
                    const li = document.createElement('li');
                    li.innerHTML = element.dev;
                    li.className = 'searchresult'
                    ul.append(li);
                    li.addEventListener('click', () => {
                        search_input.value = li.innerHTML;
                        ul.innerHTML = ''
                    })
                })
            }else{
                ul.style.display = 'none';}
    })
    }else{
        ul.style.display = 'none';
    } 
}


function focus_searchdev(){
    const ul = document.querySelector('.result_list');
    const search_input = document.querySelector('#id_dev');
    if($(search_input).is(':focus') & ul.childNodes.length > 0){
        ul.style.display = 'block';
    }else{
        ul.style.display = 'none'
    }
}

function quicksearch_pub() {
    const search_input = document.querySelector('#id_pub');
    const ul = document.querySelector('.result_list1');
    ul.innerHTML = '';
    if (search_input.value != ''){
        fetch(`/quicksearchpub/${search_input.value}`)
        .then(response => response.json())
        .then(result => {
            if (Array.from(result).length > 0){
                ul.style.display = 'block'
                result.forEach(element => {
                    const li = document.createElement('li');
                    li.innerHTML = element.pub;
                    li.className = 'searchresult'
                    ul.append(li);
                    li.addEventListener('click', () => {
                        search_input.value = li.innerHTML;
                        ul.innerHTML = ''
                    })
                })
            }else{
                ul.style.display = 'none';}
    })
    }else{
        ul.style.display = 'none';
    } 
}


function focus_searchpub(){
    const ul = document.querySelector('.result_list1');
    const search_input = document.querySelector('#id_pub');
    if($(search_input).is(':focus') & ul.childNodes.length > 0){
        ul.style.display = 'block';
    }else{
        ul.style.display = 'none'
    }
}
