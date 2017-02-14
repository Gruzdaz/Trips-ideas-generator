$(document).ready(function() {

    $('#search_submit').click(function(event){
        $('#loading').show();
        var form = $('#search-form');
        event.preventDefault();
        $.ajax({
            url: '/random_trip/',
            type: 'POST',
            data: form.serialize(),
            dataType: 'html',
            success: function (data){
                $('#loading').hide();
                $('#post').html(data);
            }

    });


});
 });

