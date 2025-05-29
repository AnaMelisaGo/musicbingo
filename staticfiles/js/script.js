// TOAST
document.addEventListener('DOMContentLoaded', function () {
    const toastElList = document.querySelectorAll('.toast');
    const toastList = [...toastElList].map(toastEl => new bootstrap.Toast(toastEl));
    toastList.forEach(toast => toast.show());
});

// playlist modal
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
    if (urlParams.get('open_modal') === '3') {
        const backGame = document.getElementById('backGameModal');
        backGame.click();
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

// trash button
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('.delete-video-btn').forEach(function(button) {
        button.addEventListener('click', function() {
            const index = this.getAttribute('data-index');
            const input = document.getElementById('clear_video_' + index);
            if (input) {
                input.value = 'true';
                const previewCell = this.closest('td').previousElementSibling;
                previewCell.innerHTML = '<small>Video removed</small>';
                previewCell.classList.add('text-muted');
                this.remove();
            }
        });
    });
});

// To display video file name when selected
document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('input[type="file"]').forEach(input => {
        input.addEventListener('change', function () {
            const fileNameDisplay = this.closest('td').querySelector('.file-name-display');
            if (this.files.length > 0) {
                fileNameDisplay.textContent = this.files[0].name;
            } else {
                fileNameDisplay.textContent = '';
            }
        });
    });
});

// auto-play button
document.addEventListener('DOMContentLoaded', function() {
    const autoPlayCheckbox = document.getElementById('autoCheckbox');
    const video = document.getElementById('videoPlayer');
    const nxtBtn = document.getElementById('nextButton');
    let intervalId = null;

    // Restore the auto-play state from localStorage
    if (localStorage.getItem('autoPlay') === 'true') {
        autoPlayCheckbox.checked = true;
    }

    // Auto-play function
    function enableAutoPlay() {
        if (video) {
            video.onended = () => nxtBtn.click();
        } else {
            intervalId = setInterval(() => {
                console.log('Next number is ...');
                nxtBtn.click();
            }, 10000);
        }
    }

    //if the checkbox is checked, enable auto-play
    if (autoPlayCheckbox.checked) enableAutoPlay();

    // Save the auto-play state to localStorage for any changes
    autoPlayCheckbox.addEventListener('change', function(){
        if (this.checked) {
            console.log('Auto-play on!');
            localStorage.setItem('autoPlay', this.checked);
            enableAutoPlay();
        } else {
            console.log('Auto-play off!')
            if (video) video.onended = null;
            clearInterval(intervalId);
            localStorage.setItem('autoPlay', false);
        }
    });

});