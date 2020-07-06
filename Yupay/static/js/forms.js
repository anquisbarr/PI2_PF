function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function getData(){
    //$('#action').html("Authenticating...");
    var RUC = $('#RUC').val();
    var company_name = $('#name').val();
    var user_id = $('#userid').val();
    var service = $('#service').val();
    var amount = $('#monto').val();
    var message = JSON.stringify({
            "RUC": RUC,
            "Company_name": company_name,
            "user_id": user_id,
            "service": service,
            "amount" : amount
        });
    $.ajax({
        url:'stamp/',
        type:'POST',
        contentType: 'application/json;charset=utf-8',
        data : message,
        dataType:'json',
        success: function(result) {
            alert(result.Result);
        }
    });
}