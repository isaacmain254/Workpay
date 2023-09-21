let client = document.getElementById("client");
let freelancer = document.getElementById("freelancer");
let joinBtn = document.getElementById("joinBtn");
// joinBtn.disabled = true;

client.addEventListener("change", submitUserGroup);
freelancer.addEventListener("change", submitUserGroup);
function submitUserGroup() {
  if (
    document.getElementById("client").value === "" ||
    document.getElementById("freelancer").value === ""
  ) {
    joinBtn.disabled = true;
  } else {
    joinBtn.disabled = false;
  }
}
