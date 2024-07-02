import os

# File Paths
input_questions = 'questions.txt'
input_answers = 'answers.txt'
input_topics = 'topics.txt'
output_file = 'main1.html'

# The main html stuff
html_content = """
<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

		<title>Enquesta-Round 2-Bidding War</title>

		<link rel="stylesheet" href="dist/reset.css">
		<link rel="stylesheet" href="dist/reveal.css">
		<link rel="stylesheet" href="dist/theme/black.css">

		<!-- Theme used for syntax highlighted code -->
		<link rel="stylesheet" href="plugin/highlight/monokai.css">
		<style>
            .horizontal-links a {
                display: inline;
                margin-right: 10px; /* Optional: Adds space between links */
        }
        .disabled-link {
            pointer-events: none;
            color: grey;
            text-decoration: none;
        }
        </style>
	</head>

	<body>
		<div class="reveal">
			<div class="slides">
"""
#Reading Topics
with open(input_topics, 'r') as file:
    topics = file.readlines()

# Reading Questions
rows1, cols1 = len(topics), 3
questions = [["" for _ in range(cols1)] for _ in range(rows1)]
x1 = -1
z1 = -1
with open(input_questions, 'r') as file:
    lines = file.readlines()
    for y in range(0,len(lines)):
        lines[y].strip()
        if lines[y].startswith('#'):
            x1 += 1
            z1 = -1
        else:
            if(lines[y].startswith('-')):
                z1 += 1
            questions[x1][z1] += lines[y]
            questions[x1][z1].replace('-','')

# Reading Answers
rows2,cols2=len(topics), 4
answers = [["empty" for _ in range(cols2)] for _ in range(rows2)]
x2 = -1
z2 = 0
with open(input_answers, 'r') as file:
    lines = file.readlines()
    for y in range(0,len(lines)):
        if lines[y].startswith('#'):
            x2 += 1
            z2 = 0
        else:
            answers[x2][z2] = lines[y]
            z2 += 1


#Adding Topics
html_content += '<section id=0>\n'
html_content += '<div class="horizontal-links">\n'
for x in range(0, len(topics)):
    html_content += '<a href="#/' + topics[x] + '" class="one-time-link">' + topics[x] + '</a>\n'
    if (x == len(topics)/2):
        html_content += '</div>\n<div class="horizontal-links">\n'
html_content += '</div>\n'
html_content += '</section>\n'


# Adding Questions, Answers and Header Slides
for x in range(0, len(topics)):
    html_content += '<section id="'+topics[x]+'">\n<h1>'+topics[x]+'</h1>'

    html_content += '<div class="horizontal-links">\n'
    for y in range(0, len(questions[x])):
        html_content += '<a href="#/' + topics[x] + str(30-y*10) + str(x)+'">' + str(30-y*10) + '</a>\n'
    html_content += '</div>\n'
    html_content += '</section>\n'

    for y in range(0, len(questions[x])):
        html_content += '<section id="'+ topics[x] + str(30-y*10)+str(x)+'">\n'
        html_content += '<section>' + questions[x][y] + '</section>\n'
        html_content += '<section data-background-image="memes/meme' + str(x) + (
            '.png" data-background-size="contain" data-background-position="center"></section>\n')
        html_content += '<section><p>' + answers[x][y]
        html_content += '</p><a href="#/0">Back to Topics</a>' + '</section>\n'
        #print(questions[x][y])
        html_content += '</section>\n'
    html_content += '<section><a href="#/0">Back to Topics</a></section>'

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
            const links = document.querySelectorAll('.one-time-link');
            
            links.forEach(link => {
                link.addEventListener('click', (event) => {
                    // Allow the link to function once
                    setTimeout(() => {
                        link.classList.add('disabled-link');
                        link.removeAttribute('href');
                    }, 100);
                });
            });
        });
		</script>
	</body>
</html>
"""

# Adding html content to file
with open(output_file, 'w') as file:
    file.write(html_content)



