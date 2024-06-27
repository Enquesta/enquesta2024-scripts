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
	</head>

	<body>
		<div class="reveal">
			<div class="slides">
"""

# Reading Questions
with open(input_questions, 'r') as file:
    questions = file.readlines()

# Reading Answers
with open(input_answers, 'r') as file:
    answers = file.readlines()

# Adding Questions and Answers
for x in range(0, len(answers)):
    html_content += '<section>\n'
    html_content += '<section>' + questions[x] + '</section>\n'
    html_content += '<section data-background-image="memes/meme' + str(x) + ('.png" data-background-size="cover" data-background-position="center"></section>\n')
    html_content += '<section>' + answers[x] + '</section>\n'
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
		</script>
	</body>
</html>
"""

# Adding html content to file
with open(output_file, 'w') as file:
    file.write(html_content)



