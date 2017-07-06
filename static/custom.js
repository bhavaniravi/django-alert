$(function(){
    $("#id_model").change(function() {
      $.get("/alert/"+$('#id_model').find(":selected").text()+"/fields", function( data ) {
          $.each(data,function(key,value)
          {
              $("#id_field").append('<option value=' +value+ '>' + value + '</option>');
          });
        });
    });
});
