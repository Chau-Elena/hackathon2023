function sendData() {
    var form = document.getElementById("image-form");
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("response").innerHTML = this.responseText;
        }
    };
    xhr.open("POST", "/upload");
    xhr.send(new FormData(form));
}