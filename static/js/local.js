function resetForm(form) {
    // clearing inputs
    var inputs = form.getElementsByTagName('input');
    for (var i = 0; i<inputs.length; i++) {
        switch (inputs[i].type) {
            // case 'hidden':
            case 'text':
                inputs[i].value = '';
                break;
            case 'radio':
            case 'checkbox':
                inputs[i].checked = false;
        }
    }

    // clearing selects
    var selects = form.getElementsByTagName('select');
    for (var i = 0; i<selects.length; i++)
        selects[i].selectedIndex = 0;

    // clearing textarea
    var text= form.getElementsByTagName('textarea');
    for (var i = 0; i<text.length; i++)
        text[i].innerHTML= '';

    return false;
}

function show_search_row() {
    $("#search_row").show();
}

function toggle_search_row() {
    $("#search_row").toggle();
}

function validate_search_invoice() {
    console.log("in validate search invoice")
    var value = $("#invoice_number").val();
        if (value!=="") {
            console.log(value.length);
            if (value.length < 3) {
                alert('Ensure this value is greater than 3 characters.');
            }
            else {
                $("#form").submit();
                $("#invoice_number").val(value);
            }
        } else {
            $("#form").submit();
        }
}

function validate_date(txtDate) {

    var currVal = txtDate;
    if(currVal == '')
        return false;

    //Checks for mm/dd/yyyy format.
    var rxDatePattern = /^(\d{1,2})(\/|-)(\d{1,2})(\/|-)(\d{4})$/;
    var dtArray = currVal.match(rxDatePattern);

    if (dtArray == null)
        return false;

    dtMonth = dtArray[1];
    dtDay= dtArray[3];
    dtYear = dtArray[5];

    if (dtMonth < 1 || dtMonth > 12)
        return false;
    else if (dtDay < 1 || dtDay> 31)
        return false;
    else if ((dtMonth==4 || dtMonth==6 || dtMonth==9 || dtMonth==11) && dtDay ==31)
        return false;
    else if (dtMonth == 2)
    {
        var isleap = (dtYear % 4 == 0 && (dtYear % 100 != 0 || dtYear % 400 == 0));
        if (dtDay> 29 || (dtDay ==29 && !isleap))
                return false;
    }
    return true;
}
