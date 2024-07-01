import os

# File Paths
input_questions = 'questions.txt'
input_answers = 'answers.txt'
output_file = 'main1.html'

html_content = ""
# The main html stuff
html_content += """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rectangles in Reveal.js</title>
    <link rel="stylesheet" href="https://unpkg.com/reveal.js/dist/reveal.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js/dist/theme/white.css">
    <style>
        :root {
            --rectangle-width: 100%;
            --rectangle-height: 100%;
        }
        .main-slide{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            grid-template-rows: repeat(4, 1fr);
            gap: 0px;
            width: 100%;
            height: 100%;
        }
        .rectangle {
            background-color: #007bff;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            height: var(--rectangle-height); /* Full height of grid cell */
            width: var(--rectangle-width); /* Full width of grid cell */
            transition: transform 0.3s ease, background-color 0.3s ease;
        }
        .rectangle:hover {
            transform: scale(1.05);
        }
        .rectangle.transparent {
            background-color: transparent;
            opacity: 0; /* Adjust opacity as needed */
        }
        .option-buttons {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 10px;
            margin-top: 20px;
        }
        .option-buttons button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <!-- Main Slide with rectangles -->
"""

#Reading Questions
with open(input_questions, 'r') as file:
    questions = file.readlines()

#Reading Answers
with open(input_answers, 'r') as file:
    answers = file.readlines()

# Rectangle Generation, Main Slide
html_content += '<section>\n<div class="main-slide">\n'
for i in range(0,16):
    html_content += '<div class="rectangle" data-link="a'+str(i+2)+'" data-index="'+str(i+1)+'">'+str(i+1)+'</div>'
html_content += '</div>\n</section>\n'

# Question Slide generation
for x in range(0, 16):
    html_content += '<section id="a'+str(x+2)+'">\n'
    html_content += '<section>' + questions[x] + '</section>\n'
    html_content += '<section></section>\n'
    html_content += '<section><h3>' + answers[x] + '</h3>\n<div class="option-buttons"><button class="remove-rectangle" data-index="'+str(x+1)+'">Correct!(Removes Box)</button>\n<button class="change-color" data-index="'+str(x+1)+'">Wrong!(Reddens Box)</button>\n</section>\n'

    html_content += '</section>\n'

#Closing the html file off, adding some script

html_content += """
        </div>
    </div>

    <script src="https://unpkg.com/reveal.js/dist/reveal.js"></script>
    <script>
        Reveal.initialize();

        document.addEventListener('DOMContentLoaded', () => {
            const mainSlide = document.querySelector('.main-slide');

            mainSlide.addEventListener('click', (event) => {
                const rectangle = event.target.closest('.rectangle');
                if (rectangle) {
                    const link = rectangle.getAttribute('data-link');
                    const targetSlide = document.querySelector(`#${link}`);
                    if (targetSlide) {
                        const slideIndex = [...document.querySelectorAll('.slides > section')].indexOf(targetSlide);
                        Reveal.slide(slideIndex);
                    }
                }
            });

            function addOptionEventListeners() {
                const removeButtons = document.querySelectorAll('.remove-rectangle');
                const changeColorButtons = document.querySelectorAll('.change-color');

                removeButtons.forEach(button => {
                    button.addEventListener('click', () => {
                        const index = button.getAttribute('data-index') - 1;
                        const rectangle = mainSlide.querySelector(`.rectangle[data-index="${index + 1}"]`);
                        if (rectangle) {
                            rectangle.classList.add('transparent'); // Make rectangle transparent
                        }
                    });
                });

                changeColorButtons.forEach(button => {
                    button.addEventListener('click', () => {
                        const index = button.getAttribute('data-index') - 1;
                        const rectangle = mainSlide.querySelector(`.rectangle[data-index="${index + 1}"]`);
                        if (rectangle) {
                            rectangle.style.backgroundColor = 'red'; // Change to desired color
                        }
                    });
                });
            }

            addOptionEventListeners();
                        function updateRectangleSizes() {
                const mainSlide = document.querySelector('.main-slide');
                const slideWidth = mainSlide.offsetWidth;
                const slideHeight = mainSlide.offsetHeight;

                // Calculate new dimensions for the rectangles
                const rectangleWidth = slideWidth / 4;
                const rectangleHeight = slideHeight / 4;

                // Update CSS variables
                document.documentElement.style.setProperty('--rectangle-width', `${rectangleWidth}px`);
                document.documentElement.style.setProperty('--rectangle-height', `${rectangleHeight}px`);
            }

            // Call the function initially
            updateRectangleSizes();

            // Update sizes on window resize
            window.addEventListener('resize', updateRectangleSizes);
        });
    </script>
</body>
</html>

"""

#Adding to main file
with open(output_file, 'w') as file:
    file.write(html_content)