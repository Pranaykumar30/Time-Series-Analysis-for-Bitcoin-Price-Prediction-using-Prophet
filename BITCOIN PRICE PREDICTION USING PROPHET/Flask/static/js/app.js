document.getElementById("predictionForm").addEventListener("submit", function(event) {
    var dateInput = document.getElementById("dateInput").value;

    if (dateInput === "") {
        alert("Please select a date for prediction.");
        event.preventDefault();
    }
});
