var urlRegex = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|])/ig;
var photoRegex = /(\b(https?|ftp|file):\/\/[-A-Z0-9+&@#\/%?=~_|!:,.;]*[-A-Z0-9+&@#\/%=~_|]).(?:jpg|gif|png)/ig;

var url_url= $('#content-url').html().match(urlRegex);
var url_photo= $('#content-url').html().match(photoRegex);

$('#content-url').html( $('#content-url').html().replace(urlRegex,''));

$.each( url_url, function(i,value){
	var convert_url='<a href="'+url_url[i]+'">'+url_url[i]+'</a><br>';
    $('#urls').append(convert_url)
});

$.each( url_photo, function(i,value){
   var convert_photo='<img src="'+url_photo[i]+'" width="150" height="150" alt="Nba"><br>';
   $('#photos').append(convert_photo)
});