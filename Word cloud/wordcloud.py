from flask import Flask, render_template
from wordcloud import WordCloud
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def show_wordcloud():
# Combine the job listings into one string
job_listings = """..."""  # Insert the job listings text here

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400).generate(job_listings)
img = BytesIO()
wordcloud.to_image().save(img, 'PNG')
img.seek(0)
plot_url = base64.b64encode(img.getvalue()).decode('utf-8')
return render_template('wordcloud.html', plot_url=plot_url)

if __name__ == '__main__':
app.run(debug=True)