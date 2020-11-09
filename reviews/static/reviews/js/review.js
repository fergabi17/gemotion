const TAG_CONTAINER = document.querySelector('.tag-container');
const INPUT = document.querySelector('#emotion-input');

var tags = [];

var emotions = {
    list: [],
    pk: [],
    categories: [],
    loadEmotions: function(emotions, categories){
        emotions = JSON.parse(emotions.replace(/(&quot\;)/g,"\""));
        for ( var key in emotions){
            this.list.push(key);
        }
        this.pk= emotions;
        this.categories = categories;
    }
}

function createTag(label){
    const DIV = document.createElement('div');
    const SPAN = document.createElement('span');
    const CLOSE_BTN = document.createElement('i');

    DIV.setAttribute('class', 'tag');
    SPAN.innerHTML = label;
    CLOSE_BTN.setAttribute('class', 'material-icons');
    CLOSE_BTN.setAttribute('data-item', label);
    CLOSE_BTN.innerHTML = 'close';

    DIV.appendChild(SPAN);
    DIV.appendChild(CLOSE_BTN);

    return DIV;
}

function addTags(){
    reset();
    tags.slice().reverse().forEach( function(tag) {
        const INPUT_CONTENT = createTag(tag);
        TAG_CONTAINER.prepend(INPUT_CONTENT);
    })
}

function reset(){
    document.querySelectorAll('.tag').forEach( function(tag){
        tag.parentElement.removeChild(tag);
    })
}

function printTags(){
    var pkInput = document.querySelector('#pk-list');
    var pkList = [];
    tags.forEach (function(tag) {
        pkList.push(emotions.pk[tag]);
    })
    pkInput.value = pkList;
}


var addInput = function (e){
    if (e.key === 'Enter' || e === "onclick"){
        var userInput = INPUT.value.trim();
        if (emotions.list.includes(userInput)){
            tags.push(INPUT.value);
            addTags();
            INPUT.value = '';
        } else if (emotions.categories.includes(userInput)){
            INPUT.value = 'category';
        } else {
            INPUT.value = '';
        }
 
    }
}

INPUT.addEventListener('keyup', addInput);

document.addEventListener('click', function(e){
    if (e.target.tagName === "I"){
        const TAG_LABEL = e.target.getAttribute('data-item');
        const INDEX = tags.indexOf(TAG_LABEL);
        tags = [... tags.slice(0, INDEX), ... tags.slice(INDEX + 1)];
        addTags();
    }
})


