function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      // document.getElementById("add").innerHTML =
      // this.responseText;
      alert("Hello object")
    }
  };
  xhttp.open("GET.html", "ajax_info.txt", true);
  xhttp.send();
}
