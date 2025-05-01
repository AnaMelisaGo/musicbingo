// TOAST
document.addEventListener('DOMContentLoaded', function () {
    const toastElList = document.querySelectorAll('.toast');
    const toastList = [...toastElList].map(toastEl => new bootstrap.Toast(toastEl));
    toastList.forEach(toast => toast.show());
});

// Delete modal
document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('open_modal') === '1') {
        const deleteModalButton = document.getElementById('deleteModalButton');
        deleteModalButton.click();
    }
    if (urlParams.get('open_modal') === '2') {
        const backButton = document.getElementById('backButtonModal');
        backButton.click();
    }
});

// prize button
document.querySelectorAll('.prize-btn').forEach(button => {
    button.addEventListener('click', function() {
        const prize = this.getAttribute('data-prize');
        document.getElementById('prizeInput').value = prize;
    });
});


// Checking winning numbers
const selectedNumbers = new Set();

document.querySelectorAll('.winning-btn').forEach(button => {
    button.addEventListener('click', () => {
        const number = button.getAttribute('data-number');

        if (selectedNumbers.has(number)) {
            selectedNumbers.delete(number);
            button.classList.remove('btn-success');
            button.classList.add('btn-secondary');
        }
        else {
            selectedNumbers.add(number);
            button.classList.remove('btn-secondary');
            button.classList.add('btn-success');
        }

        document.getElementById('selected_numbers_input').value = JSON.stringify(Array.from(selectedNumbers));
    });
});

// canvas confetti home button

document.addEventListener('DOMContentLoaded', function() {
    const handleConfetti = () => {
        confetti({
            particleCount: 100,
            spread: 100,
            scalar: 2,
        });
    }

    const winnerConfetti = () => {
        confetti({
            particleCount: 700,
            spread: 500,
        });
    }

    const homeButton = document.querySelector('#home-button');
    if (homeButton) {
        homeButton.addEventListener('click', handleConfetti);
    }

    const checkWinner = document.querySelector('#check-winner');
    if (checkWinner) {
        checkWinner.addEventListener('click', winnerConfetti);
    }
});


