import fitz
import sys

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

if __name__ == "__main__":
  no_of_arguments = len(sys.argv)
  if (no_of_arguments) == 3:
    pdf_path = (sys.argv[1])
    target_word = (sys.argv[2])
  else:
    pdf_path=input("Location of the pdf: ")
    target_word=input("Target word: ")
  
  found_sentences = extract_sentences_with_word(pdf_path, target_word)

  if found_sentences:
    for sentence, page_number in found_sentences:
      print(f"Page {page_number}:")
      print(f"{sentence}")
      print(f"--------------------")
  else:
      print(f"No sentences containing '{target_word}' found in the PDF.")
