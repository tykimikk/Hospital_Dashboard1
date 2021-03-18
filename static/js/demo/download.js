var elements = document.getElementsByClassName("downloadPng dropdown-item")  


var myFunction = function() {
  var chartname = this.getAttribute("download")
  var url_base64 = document.getElementById(chartname).toDataURL("image/png")
  this.href = url_base64;
};
for (var i = 0; i < elements.length; i++) {
  elements[i].addEventListener('click', myFunction, true);

}