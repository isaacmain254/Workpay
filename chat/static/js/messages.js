const USER_ID = $('#logged-in-ser').val()

let loc = window.location;
let wsStart = "ws://";
console.log("testing");

if (loc.protocol === "https") {
  wsStart = "wss://";
}

let endpoint = wsStart + loc.host + loc.pathname;

var socket = new WebSocket(endpoint);

// will be fired when connection with websocket is open
socket.onopen = async function (e) {
  console.log("open", e);
  $("#message-form").on("submit", function (event) {
    event.preventDefault();
    let message = $("input#message-text").val();
    let send_to

    let data = {
      // type: 'message',
      'message': message,
      'sent_by' : USER_ID,
      'send_to': send_to
    }
    // send the data using JSON to transmit objects
    data =  JSON.stringify(data)
    socket.send(data)

    // clear the text input
    $(this)[0].reset();
  });
};

socket.onmessage = async function (e) {
  console.log("message", e);
  const data = JSON.parse(e.data);
  let message = data["message"];
  newMessage(message)
  

};

socket.onerror = async function (e) {
  console.log("error", e);
};

socket.onclose = async function (e) {
  console.log("close", e);
};

function newMessage(message){
  $("#message-container").append(`
  <div class="d-flex gap-3 my-3">
                            <img class="img-fluid rounded-circle " src="{% static 'images/mainawambui.jpg' %}"
                                width="40" height="40" alt="" />
                            <div>
                                <div class="text-bg-secondary px-3 py-1 rounded-pill">${message}</div>
                                <small class="fw-lighter">10:45AM today</small>
                            </div>
                        </div>
  `);

}







// $("input").on("focus", function (e) {
//  $("input#message-text").css('background', 'blue')
// });
