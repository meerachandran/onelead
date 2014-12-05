require(["dojo/_base/declare", "dijit/form/DateTextBox", "dojo/date/locale", "dojo/dom", "dojo/domReady!"],
        function(declare, DateTextBox, locale, dom){
        declare("AttnDateTextBox", DateTextBox, {
        attnFormat: {selector: 'date', datePattern: 'dd-MMM-yyyy', locale: 'en-us'},
        value: "", // prevent parser from trying to convert to Date object
        postMixInProperties: function(){ // change value string to Date object
            this.inherited(arguments);
            // convert value to Date object
            this.value = locale.parse(this.value, this.attnFormat);
        },
        // To write back to the server in Oracle format, override the serialize method:
        serialize: function(dateObject, options){
            return locale.format(dateObject, this.attnFormat).toUpperCase();
        }
    });
    function showServerValue(){
			console.log("hello");        
			//dom.byId('slotsdiv').innerHTML = "doom";
			//document.getElementsByName('attn')[0].value;
				
    }
    new AttnDateTextBox({
        value: "31-DEC-2009",
        name: "attn",
        onChange: function(v){ setTimeout(showServerValue, 0)}
    }, "attn").startup();
    showServerValue();
});

//Submit button
require(["dijit/form/Button", "dojo/dom", "dojo/domReady!"], function(Button, dom){
    // Create a button programmatically:
    var myButton = new Button({
        label: "Save!"
    }, "progButtonNode").startup();
});
//Combo box
require(["dojo/parser", "dijit/form/ComboBox"]);
