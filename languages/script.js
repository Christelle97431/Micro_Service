var myHeaders = new Headers();
myHeaders.append("Accept", "application/json");

var formdata = new FormData();
formdata.append("username", "{username}");
formdata.append("email", "{email}");
formdata.append("password", "{password}");
formdata.append("password_confirmation", "{password_confirmation}");

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: formdata,
  redirect: 'follow'
};

fetch("http://127.0.0.1:5000/register", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));