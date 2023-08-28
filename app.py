import fitz
import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def extract_sentences_with_word(pdf_path, target_word):
  sentences = []
  pdf_document = fitz.open(pdf_path)

  for page_number in range(pdf_document.page_count):
    page = pdf_document[page_number]
    page_text = page.get_text()

    all_sentences = page_text.split('.')

    for sentence in all_sentences:
      if target_word.lower() in sentence.lower():
        sentences.append((sentence.strip() + '.', page_number + 1))

  pdf_document.close()
  return sentences

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    target_word = request.form.get("target_word")

    if 'pdf_file' not in request.files:
      return redirect(request.url)

    pdf_file = request.files['pdf_file']
    if pdf_file.filename == '':
      return redirect(request.url)

    if pdf_file and pdf_file.filename.endswith('.pdf'):
      pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], pdf_file.filename)
      pdf_file.save(pdf_path)
      found_sentences = extract_sentences_with_word(pdf_path, target_word)
      os.remove(pdf_path)

      return render_template("result.html", sentences=found_sentences)

  return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)
