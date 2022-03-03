function onload(){
    eel.fetch_index()(call_back)
}

function call_back(pyOutput){
    console.log("HERE IN CALL BACK")
    console.log(pyOutput)
    document.getElementById('template').innerHTML = pyOutput

}
function BtnClick(){
 var urlField = document.querySelector('table');

// create a Range object
  var range = document.createRange();
  // set the Node to select the "range"
  range.selectNode(urlField);
  // add the Range to the set of window selections
  window.getSelection().addRange(range);

  // execute 'copy', can't 'cut' in this case
  document.execCommand('copy');

}



