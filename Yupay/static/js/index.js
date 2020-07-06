function goToForms(){
    $.ajax({
        url:'forms/',
        type:'GET',
        success: function(response){
            //alert(JSON.stringify(response));
            $('#action').html("");
            if(response['status']==401){
            $('#action').append('<img width="30" height="30" src="images/equis.jpg"/>');
            }else{
            var url = 'http://'+ document.domain+ ':'+ location.port + '/forms/';
            $(location).attr('href',url);
            }
                        //$('#action').html(response['statusText']);
        }
    });
}