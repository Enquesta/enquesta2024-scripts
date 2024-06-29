// script.js

document.addEventListener('DOMContentLoaded', () => {
    const rectangles = document.querySelectorAll('.rectangle');
    const questionDisplay = document.querySelector('.question-display');
    const questionContent = document.querySelector('.question-content');
    const deleteButton = document.querySelector('.delete-button');
    const backButton = document.querySelector('.back-button');
    let currentRectangle = null;

    rectangles.forEach(rectangle => {
        rectangle.addEventListener('click', () => {
            const question = rectangle.getAttribute('data-question');
            questionContent.textContent = question;
            questionDisplay.style.display = 'flex';
            currentRectangle = rectangle;
        });
    });

    backButton.addEventListener('click', () => {
        questionDisplay.style.display = 'none';
    });

    deleteButton.addEventListener('click', () => {
        if (currentRectangle) {
            currentRectangle.remove();
            questionDisplay.style.display = 'none';
        }
    });
});
