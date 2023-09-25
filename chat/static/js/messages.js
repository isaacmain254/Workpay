

const sent_by_id = $('#logged-in-user').val()
console.log('sent_by_id', sent_by_id)
let room_name = JSON.parse(document.getElementById('thread_id').textContent)

console.log('room name is:', room_name)
let loc = window.location;
let wsStart = "ws://";


if (loc.protocol === "https") {
  wsStart = "wss://";
}

let endpoint = wsStart + loc.host + loc.pathname


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
      'sender_id' : sent_by_id,
      // "thread_id" : room_name,
      // 'send_to': send_to
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
  console.log(data)
  let message = data["message"];
  let sender_id = data["sender_id"]

  console.log('sender_id is',sender_id)
  newMessage(message, sender_id)
  

};

socket.onerror = async function (e) {
  console.log("error", e);
};

socket.onclose = async function (e) {
  console.log("close", e);
};

function newMessage(message, sender_id){
  if (sent_by_id === sender_id){
  $("#message-container").append(`
    <div class="d-flex flex-row-reverse gap-3 my-3">
                            
                            <div class="position-relative">
                                <div class="text-bg-secondary px-3 py-1 rounded-pill">
                                ${message}
                                </div>
                                
                            </div>
                        </div>
    ` )
  } else {
    $("#message-container").append(`
  <div class="d-flex gap-3 my-3">
                          
                            <div>
                                <div class="text-bg-secondary px-3 py-1 rounded-pill">${message}</div>
                                
                            </div>
                        </div>
  `);
  }

}

