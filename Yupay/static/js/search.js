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
    var user_id = $('#userid').val();
    var data = JSON.stringify({
            "user_id": user_id
        });
    data = user_id
    $.ajax({
        url:'search/',
        type:'GET',
        contentType: 'application/json',
        data : data,
        dataType:'json',
        success: function(result) {
            alert(json.stringify(response));
            var url = 'http://'+ document.domain+ ':'+ location.port + '/search/';
            $(location).attr('href',url);
        },
        error: function(){
            alert(json.stringify(response));
            var url = 'http://'+ document.domain+ ':'+ location.port + '/search/';
            $(location).attr('href',url);
        }
    });
}