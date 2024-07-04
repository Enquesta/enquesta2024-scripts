import os

# File Paths
input_questions = 'questions.txt'
input_answers = 'answers.txt'
output_file = 'main1.html'

# The main html stuff
html_content = """
<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

		<title>Enquesta-Round 1-Pounce and Bounce</title>

		<link rel="stylesheet" href="dist/reset.css">
		<link rel="stylesheet" href="dist/reveal.css">
		<link rel="stylesheet" href="dist/theme/black.css">

		<!-- Theme used for syntax highlighted code -->
		<link rel="stylesheet" href="plugin/highlight/monokai.css">
    <style>
        .image-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }
        .image-container img {
            max-width: 100%;
            max-height: 100%;
            object-fit: contain;
            box-sizing: border-box;
        }
    </style>
	</head>

	<body>
		<div class="reveal">
			<div class="slides">
"""

#Reading Questions
z1 = -1
questions = ["" for _ in range(6)]
with open(input_questions, 'r') as file:
    lines1 = file.readlines()
    for i in range(len(lines1)):
        if (lines1[i].startswith('-')):
            z1 += 1
            questions[z1] += lines1[i]


#Reading Answers
z2 = -1
answers = ["" for _ in range(6)]
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

#Adding Questions, Answers, Images
for i in range(len(questions)):
    html_content += '<section>'
    html_content += '<section><h4>Question ' +str(i+1)+'</h4><p>'+questions[i]+'<p></section>\n'
    if i in images:
        for j in range(0, n_images[images.index(i)]):
            html_content += '<section>\n<div class="image-container">\n'
            html_content += '<img src="images/image' + str(i) + '-' + str(j) + '.png">'
            html_content += '</div>\n</section>\n'
    html_content += '<section data-background="memes/meme0.png"></section\n>'
    html_content += '<section>' + answers[i] + '</section>\n'
    html_content += '</section>\n'

# Closing html tags
html_content += """			
            </div>
		</div>

		<script src="dist/reveal.js"></script>
		<script src="plugin/notes/notes.js"></script>
		<script src="plugin/markdown/markdown.js"></script>
		<script src="plugin/highlight/highlight.js"></script>
		<script>
			// More info about initialization & config:
			// - https://revealjs.com/initialization/
			// - https://revealjs.com/config/
			Reveal.initialize({
				hash: true,

				// Learn about plugins: https://revealjs.com/plugins/
				plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
			});
			document.addEventListener('DOMContentLoaded', () => {
    function updateImageSize() {
        const imageContainer = document.querySelector('.image-container');
        const image = imageContainer.querySelector('img');
        const containerWidth = imageContainer.offsetWidth;
        const containerHeight = imageContainer.offsetHeight;

        // Ensure image fits within the container
        if (image.naturalWidth > containerWidth || image.naturalHeight > containerHeight) {
            image.style.maxWidth = `${containerWidth}px`;
            image.style.maxHeight = `${containerHeight}px`;
        } else {
            image.style.maxWidth = '100%';
            image.style.maxHeight = '100%';
        }
    }

    updateImageSize();
    window.addEventListener('resize', updateImageSize);
});
		</script>
	</body>
</html>
"""

# Adding html content to file
with open(output_file, 'w') as file:
    file.write(html_content)



