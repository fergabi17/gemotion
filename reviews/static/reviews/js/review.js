const TAG_CONTAINER = document.querySelector('.tag-container');
const INPUT = document.querySelector('#emotion-input');

// List of emotions to be rendered
tags = [];
// List of emotions and categories from Database
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

// Creates a tag html element for each emotion input
function createTag(label){
    const DIV = document.createElement('div');
    const SPAN = document.createElement('span');
    const CLOSE_BTN = document.createElement('i');

    DIV.setAttribute('class', 'tag');
    SPAN.innerHTML = label;
    CLOSE_BTN.setAttribute('class', 'material-icons close-button');
    CLOSE_BTN.setAttribute('data-item', label);
    CLOSE_BTN.innerHTML = 'close';

    DIV.appendChild(SPAN);
    DIV.appendChild(CLOSE_BTN);

    return DIV;
}

// Adds html tags into the tag container
function addTags(){
    reset();
    tags.slice().reverse().forEach( function(tag) {
        const INPUT_CONTENT = createTag(tag);
        TAG_CONTAINER.prepend(INPUT_CONTENT);
    })
}

// Clears the tag container
function reset(){
    document.querySelectorAll('.tag').forEach( function(tag){
        tag.parentElement.removeChild(tag);
    })
}

// Prints the selected emotions PK as an input value to be submitted
function printTags(){
    var pkInput = document.querySelector('#pk-list');
    var pkList = [];
    tags.forEach (function(tag) {
        pkList.push(emotions.pk[tag]);
    })
    if (pkList.length > 0){
        pkInput.value = JSON.stringify(pkList);
    }
}


// Validates the user input, adds it and clear the input
var addInput = function (e, emotion){
    if (e.key === 'Enter' || e === "onclick" || e ==='byCategory'){
        var userInput = e ==='byCategory' ? emotion : INPUT.value.trim();
        if (emotions.list.includes(userInput) && !tags.includes(userInput)){
            tags.push(userInput);
            addTags();
            INPUT.value = '';
            // $('.collapse').removeClass('show');
        } else if (emotions.categories.includes(userInput)){
            INPUT.value = 'Use button bellow :)';
        } else {
            INPUT.value = '';
        }
        
    }
}

INPUT.addEventListener('keyup', addInput);

document.addEventListener('click', function(e){
    var clickedClass = e.target.className;
    if (e.target.tagName === "I" && clickedClass == 'material-icons close-button'){
        const TAG_LABEL = e.target.getAttribute('data-item');
        const INDEX = tags.indexOf(TAG_LABEL);
        tags = [... tags.slice(0, INDEX), ... tags.slice(INDEX + 1)];
        addTags();
    }
})


