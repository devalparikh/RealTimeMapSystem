var mymap = L.map('mapid').setView([51.505, -0.09], 13);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
  attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
  maxZoom: 18,
  id: 'mapbox/streets-v11',
  tileSize: 512,
  zoomOffset: -1,
  accessToken: 'pk.eyJ1IjoiZGV2YWxwcCIsImEiOiJja2RyeWRqOW4xNHY5MzBwNnY4YnBrbDgwIn0.9WEvpT3kByZtSTxiYPOPVA'
}).addTo(mymap);

// mapMarkers1 = [];
// mapMarkers2 = [];
// mapMarkers3 = [];

// var source = new EventSource('/topic/TOPICNAME'); //ENTER YOUR TOPICNAME HERE
// source.addEventListener('message', function(e){

