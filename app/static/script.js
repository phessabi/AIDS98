$(document).on('ready', function() {
$('.field').on('focus', function() {
  $('body').addClass('is-focus');

});

$('.field').on('blur', function() {
  $('body').removeClass('is-focus is-type');
});





});
function detectSpam() {
var inp = $('#sentence').val();
$.post( "http://127.0.0.1:5001/detect",{content: inp}, function( data ) {
  var result = data.result;
  var reasons = data.reasons;
  var pretext = ''
  var posttext = ''
  var output = "<span style='color: black; font-weight: bold;'>Not Sure</span>"
  if(result == 'False'){
    output = "<span style='color: Green; font-weight: bold;'>Not Spam</span>";
  }
  if(result == 'True'){
    pretext = 'due to having words: <br>'
    posttext = '<br>it was a spam!'
    output = "<span style='color: Red; font-weight: bold;'>Spam</span>";
  }
  reasons = ''.concat(pretext, "<span style='color: red; font-weight: bold;'>", reasons, "</span>", posttext);
  $('#result').html(output);
  $('#reasons').html(reasons);
});
}
function clean() {
var inp = $('#sentence').val("");
}