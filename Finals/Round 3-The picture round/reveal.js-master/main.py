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
    <link rel="stylesheet" href="./dist/reveal.css">
    <link rel="stylesheet" href="./dist/theme/white.css">
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
            margin-top: -2.5%;
            margin-left: -10%;
            width: 105vw;
            height: 105vh;
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
        .disabled-link {
            pointer-events: none;
            color: grey;
            text-decoration: none;
        }
                .remove-rectangle{
            background-color: #4CAF50; /* Green background */
            border: none;             /* Remove border */
            color: white;             /* White text */
            padding: 15px 32px;       /* Padding */
            text-align: center;       /* Center text */
            text-decoration: none;    /* Remove underline */
            display: inline-block;    /* Display inline-block */
            font-size: 16px;          /* Font size */
            margin: 4px 2px;          /* Margin */
            cursor: pointer;          /* Pointer cursor on hover */
            border-radius: 12px;      /* Rounded corners */
            box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* Add shadow */
            transition: 0.3s; /* Smooth transition for shadow and hover */
        }

        /* Hover effects */
        .remove-rectangle:hover {
            background-color: #45a049; /* Darker green background */
            box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2); /* Change shadow */
        }

        /* Active state */
        .remove-rectangle:active {
            background-color: #3e8e41; /* Even darker green background */
            transform: translateY(2px); /* Move down a bit when clicked */
        }

        /* Add focus outline */
        .remove-rectangle:focus {
            outline: none; /* Remove default focus outline */
            box-shadow: 0 0 8px rgba(0, 140, 186, 0.5); /* Add custom focus outline */
        }
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <!-- Main Slide with rectangles -->
"""

#Reading Questions
z1 = -1
questions = ["" for _ in range(16)]
with open(input_questions, 'r') as file:
    lines1 = file.readlines()
    for i in range(len(lines1)):
        if (lines1[i].startswith('-')):
            z1 += 1
            questions[z1] += lines1[i]



#Reading Answers
z2 = -1
answers = ["" for _ in range(16)]
with open(input_answers, 'r') as file:
    lines2 = file.readlines()
    for i in range(len(lines2)):
        if (lines2[i].startswith('-')):
            z2 += 1
            answers[z2] += lines2[i]

#Reading images
questions_with_images = -1
images = []
n_images = []
for i in range(0, len(questions)-1):
    if questions[i][len(questions[i]) - 3] == '#':
        questions_with_images += 1
        images.append(i)
        n_images.append(int(questions[i][len(questions[i]) - 2]))
print(images)
print(n_images)

# Rectangle Generation, Main Slide
html_content += '<section data-background="Round3BG.png">\n<div class="main-slide">\n'
for i in range(0,16):
    html_content += '<div class="rectangle" data-link="a'+str(i+2)+'" data-index="'+str(i+1)+'" data-one-time="true">'+str(i+1)+'</div>'
html_content += '</div>\n</section>\n'

# Question Slide generation
for x in range(0, 16):
    html_content += '<section id="a'+str(x+2)+'">\n'
    html_content += '<section><h4>Question ' +str(x+ 1)+ '</h4><p class="r-fit-text">'+questions[x]+'</p></section>\n'
    if x in images:
        html_content += '<section data-background=images/image'+str(x)+'-0.png data-background-size="contain">\n'

        html_content += '</section>\n'
    html_content += '<section data-background="memes/meme0.png"></section>\n'
    html_content += '<section><p>' + answers[x] + '</p>\n<div class="option-buttons"><button class="remove-rectangle" data-index="'+str(x+1)+'">Correct!(Removes Box)</button>\n</section>\n'

    html_content += '</section>\n'

#Closing the html file off, adding some script

html_content += """
        </div>
    </div>

    <script src="./dist/reveal.js"></script>
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
            const links = document.querySelectorAll('[data-one-time="true"]');
            
            links.forEach(link => {
                link.addEventListener('click', (event) => {
                    // Allow the link to function once
                    setTimeout(() => {
                        link.classList.add('disabled-link');
                        link.removeAttribute('data-link');
                    }, 100);
                });
            });

        });
    </script>
</body>
</html>

"""

#Adding to main file
with open(output_file, 'w') as file:
    file.write(html_content)