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

		<title>Enquesta-Prelims</title>

		<link rel="stylesheet" href="dist/reset.css">
		<link rel="stylesheet" href="dist/reveal.css">
		<link rel="stylesheet" href="dist/theme/black.css">

		<!-- Theme used for syntax highlighted code -->
		<link rel="stylesheet" href="plugin/highlight/monokai.css">
    <style>
        .custom-slide {
            border: 5px solid yellow; /* Add a yellow border */
            border-radius: 15px; /* Rounded corners */
            padding: 20px; /* Adjust padding for better appearance */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Add a subtle shadow */
        }
        .custom-slide h2 {
            margin-top: 0; /* Remove default top margin for better alignment */
        }
    </style>
	</head>

	<body>
		<div class="reveal">
			<div class="slides">
"""

#Reading Questions
z1 = -1
questionsx = ["" for _ in range(20)]
with open(input_questions, 'r') as file:
    lines1 = file.readlines()
    for i in range(len(lines1)):
        if (lines1[i].startswith('-')):
            z1 += 1
            questionsx[z1] += lines1[i]



#Reading images
questions_with_images = -1
images = []
n_images = []
for i in range(0, len(questionsx)-1):
    if questionsx[i][len(questionsx[i]) - 3] == '#':
        questions_with_images += 1
        images.append(i)
        n_images.append(int(questionsx[i][len(questionsx[i]) - 2]))
print(images)
print(n_images)

#Formatting Questions
questions = []
for i in questionsx:
    string = ""
    for j in range(len(i)):
        if j>0 and (j<len(i)-2):
            string += i[j]
    questions.append(i)


#Adding Questions and Images
for i in range(len(questions)):
    html_content += '<section>\n'
    html_content += '<section data-background="prelimsimage.png"'
    if (i+1)%4==0:
        html_content += ' class="custom-slide"'
    html_content += '><h4>Question ' +str(i+1)+ '</h4><p class="r-fit-text">'+questions[i]+'</p></section>\n'
    if i in images:
        html_content += '<section data-background="images/image'+str(i)+'-0.png" data-background-size="contain">\n</section>'
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



