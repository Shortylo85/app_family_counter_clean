$('#post-form').on('submit',function(event){
    event.preventDefault();

    $.ajax({
      url: '/post-message/',
      type: 'POST',
      data: { msgbox: $("#msg").val() },

      success: function(json){
        $("#msg").val('');
        $("#msg-items").append('<div class="uk-card uk-card-primary uk-card-body uk-width-3-4@m uk-margin uk-align-right"><h1>' + json.user + '</h1><p>' + json.msg + '</p></div>');

        var msg_container = document.getElementById("#msg-container");
        msg_container.scrollTop = msg_container.scrollHeight;
      }
    });
});

function getMessages(){

}
