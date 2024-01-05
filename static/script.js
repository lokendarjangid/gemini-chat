window.addEventListener('unload', function () {
    // Send a synchronous GET request to the server to clear the session
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/clear_session', true);  // Synchronous request
    xhr.send();
});
