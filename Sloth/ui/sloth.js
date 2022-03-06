var isLoadForTemplate = false
function onload(){
    eel.fetch_index()(call_back)
}

function call_back(pyOutput){
    //console.log("HERE IN CALL BACK")
    //console.log(pyOutput)
    document.getElementById('template').innerHTML = pyOutput

}
function saveForm(FormData){
    console.log(FormData)
}

    var copyBtn = document.querySelector('#copy_btn');
    copyBtn.addEventListener('click', function () {
    console.log("call event listener")
    var urlField = document.getElementById('template');

    // create a Range object
    var range = document.createRange();
    // set the Node to select the "range"
    // Start at the `hello` element.
    range.setStart(urlField.childNodes[0], 0);

    // End in the `world` node
    range.setEnd(urlField.childNodes[1], 0);

    range.selectNodeContents(urlField);
    let sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);

    // add the Range to the set of window selections
    //window.getSelection().addRange(range);

    // execute 'copy', can't 'cut' in this case
    document.execCommand('copy');
    }, false);





