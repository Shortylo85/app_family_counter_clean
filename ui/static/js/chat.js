$('#post-form').on('submit',function(event){
    event.preventDefault();
    console.log("hi")

    $.ajax({
      url: '/post-message/',
      type: 'POST',
      data: { msg_value : $("#my_msg").val() },


      success: function(json){
        $("#my_msg").val('');
        $("#msg-items").append('<div class="uk-card uk-card-primary uk-card-body uk-width-3-4@m uk-margin uk-align-right"><h3>'+ json.user +'</h3><p>' + json.msg + '</p></div>');
        // var msg_container = document.getElementById("#msg-container");
        // msg_container.scrollTop = msg_container.scrollHeight;
      }
    });
});

// function getMessages(){
//   if(!scrolling){
//     $.get('/view-message/',function(messages){
//       $("#msg-items").html(messages);
//       // var msg_container = document.getElementById("#msg-container");
//       // msg_container.scrollTop = msg_container.scrollHeight;
//     });
//   }
//   scrolling = false;
// }
//
// var scrolling = false;
//
// $(function(){
//   $("#msg-container").on('scroll',function(){
//     scrolling = true;
//   });
//   refreshTimer = setInterval(getMessages, 10000);
// });
//
$(document).ready(function(){
  $("#submit").attr('disabled','disabled');
  $("#my_msg").keyup(function(){
    if($(this).val() != ''){
      $("#submit").removeAttr('disabled')
    }else{
      $("#submit").attr('disabled','disabled');
    }
  });
});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
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
