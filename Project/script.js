// script.js

function sendUrl() {
  var url = document.getElementById("urlInput").value;
  var loading = document.getElementById("gifimg");
  loading.removeAttribute("hidden");

  fetch("http://127.0.0.1:5000/a", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ url: url }),
  })
    .then((response) => response.json())
    .then((data) => {
      loading.setAttribute("hidden", "hidden");

      var element = document.getElementById("summary");
      element.classList.add("div1");
      var summaryText = "Summary: " + data.summary;
      document.getElementById("summary").innerText = summaryText;

      // Generate text-to-speech for the summary
      speak(summaryText);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

// Attach the event handler using addEventListener
document.getElementById("getInfoButton").addEventListener("click", sendUrl);

// Function to generate text-to-speech
function speak(text) {
  var synth = window.speechSynthesis;
  var utterance = new SpeechSynthesisUtterance(text);
  synth.speak(utterance);
}
