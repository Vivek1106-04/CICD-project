// Change 'localhost' to your GCP Public IP during the final deployment phase
const API_URL = 'http://127.0.0.1:5001/student-details';

fetch(API_URL)
    .then(response => response.json())
    .then(data => {
        document.getElementById('student-name').textContent = data.student_name;
        document.getElementById('roll-number').textContent = data.roll_number;
    })
    .catch(error => {
        console.error('Error fetching data:', error);
        document.getElementById('student-name').textContent = "Error loading data";
    });
