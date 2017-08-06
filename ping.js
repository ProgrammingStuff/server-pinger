var http = require("http");
setInterval(function() {
    http.get("http://uhc-server.herokuapp.com");
}, 1740000); // every 29 mins 5min=(300000)
