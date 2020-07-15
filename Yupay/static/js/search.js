
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
            console.log(response);
            alert(json.stringify(response));
        },
        error: function(){
            console.log(response);
            alert(json.stringify(response));
        }
    });
}