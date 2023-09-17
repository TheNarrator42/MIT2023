
document.getElementById('button').addEventListener('click', function() {
    fetch('/receive_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'text/plain', // Specify the content type as plain text
        },
        body: document.getElementById('email').value
    })
    .then(response => response.text())
    .then(data => {
    // Process the result received from the server
    alert('Response from server: ' + data);
    document.getElementById("inputImage").src="../static/images/output_0_0.png";
    document.getElementById("inputText").innerHTML = document.getElementById('email').value;
    document.getElementById("inputKeyword").innerHTML = "Prompt: " + data;
    console.log('Hello');
    })
    .catch(error => {
    console.error('Error:', error);
});

});