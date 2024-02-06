from flask import Flask, request, jsonify
import wikipediaapi
from collections import Counter

from preprocessing import *

# TODO: make file and start scripts
# nltk.download('stopwords')

app = Flask(__name__)


# persist this in some place
search_history_list = []

wiki = wikipediaapi.Wikipedia(
    'WikiInsights (lalwanidheeraj1234@gmail.com)',
    'en',
    extract_format=wikipediaapi.ExtractFormat.WIKI
    )

@app.route('/wiki-word-frequency', methods=['GET'])
def wiki_word_frequency():
    topic = request.args.get('topic')
    n = int(request.args.get('n'))

    # using this query param to control weather or not to perform preprocessing
    if request.args.get('preprocess'):
        preprocess = (request.args.get('preprocess').lower() == 'true')
    else: # default value for preprocess is set to true
        preprocess = True

    page = wiki.page(topic)
    
    if page.exists():
        page_content = page.text
        if preprocess:
            # Future TODO: Provide more granular control over preprocessing
            page_content = clean_text(page_content)
    else:
        return jsonify({'error': 'Page not found'}), 404

    words = page_content.split()
    word_freq = Counter(words)
    top_words = dict(word_freq.most_common(n))

    search_history_list.append({'n': n, 'topic': topic, 'top_words': top_words})

    return jsonify({'topic': topic, 'top_words': top_words})


@app.route('/search-history', methods=['GET'])
def search_history():
    q = request.args.get('q', '').lower()

    if q == '':
        return jsonify({'q': q, 'data': search_history_list})

    filtered_results = []

    for entry in search_history_list:
        topic = entry['topic'].lower()
        if q == ''  or topic.startswith(q):
            filtered_results.append(entry)

    return jsonify({'q': q, 'data': list(filtered_results)})

if __name__ == '__main__':
    app.run(debug=True)
