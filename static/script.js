function summarizeText() {
    const input = document.getElementById("inputText");
    const output = document.getElementById("output");

    if (!input || !output) {
        console.error("Missing input or output element");
        return;
    }

    const text = input.value.trim();

    if (text.length === 0) {
        output.innerText = "Please enter some text.";
        return;
    }

    fetch("/summarize", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Server returned " + response.status);
        }
        return response.json();
    })
    .then(data => {
        output.innerText = data.summary;
    })
    .catch(error => {
        console.error("Fetch error:", error);
        output.innerText = "Error summarizing text.";
    });
}
