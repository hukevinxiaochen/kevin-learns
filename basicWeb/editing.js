// add text one character at a time to simulate interactive writing
function typeText(div, message, len) {
    if(len > message.length) return;
    
    div.innerText = message.substr(0, len);
    setTimeout(function() { typeText(div, message, len + 1); }, 65);
}

// code that generates errors will abort the entire script
// uncomment the below code to see what I mean

/*
 * var pre = document.getElementsByTagName("pre")[0];
 * pre.style.display = "none"
 */

// start black & green writer
document.body.style.backgroundColor = "Black";
var div = document.createElement("div");
div.style.color = "#37CC64";
document.body.appendChild(div);
typeText(div, "You can use the Javascript Preview mode as a development environment.\n" +
              "            \n" +
              "Enable the Console where you switched mode.", 0);
