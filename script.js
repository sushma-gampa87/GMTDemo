// script.js

// Function to handle form submission
function handleFormSubmission(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(event.target);
    const apiUrl = 'https://api.example.com/calculateTax'; // Replace with your API URL

    // Make API call to backend for tax calculation
    fetch(apiUrl, {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        displayTaxCalculationResults(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Function to display tax calculation results
function displayTaxCalculationResults(data) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = ''; // Clear previous results

    const resultElement = document.createElement('div');
    resultElement.innerHTML = `<h3>Tax Calculation Results</h3><p>Tax Amount: ${data.taxAmount}</p>`; // Adjust based on API response
    resultsContainer.appendChild(resultElement);
}

// Event listener for form submission
const form = document.getElementById('taxForm'); // Ensure you have a form with id='taxForm'
form.addEventListener('submit', handleFormSubmission);