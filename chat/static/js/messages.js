
let message_sender = maina
let message_receiver = Rose

let loc = window.location;
let wsStart = "ws://";
console.log("testing");


if (loc.protocol === "https") {
  wsStart = "wss://";
}

let endpoint = wsStart + loc.host + loc.pathname;

var socket = new WebSocket(endpoint);

socket.onopen = async function (e) {
  console.log("open", e);
  
};

socket.onmessage = async function (e) {
  console.log("message", e);
};

socket.onerror = async function (e) {
  console.log("error", e);
};

socket.onclose = async function (e) {
  console.log("close", e);
};

// $("input").on("focus", function (e) {
//  $("input#message-text").css('background', 'blue')
// });

// send message
$("#message-form").submit(function (e) {
  e.preventDefault();
  var message = $("input#message-text").val();
  console.log(message);
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
  $(this)[0].reset();
});
