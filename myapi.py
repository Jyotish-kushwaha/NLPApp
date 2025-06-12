import nlpcloud

class MyAPI:
    def sentiment_analysis(self, text):
        client = nlpcloud.Client("finetuned-llama-3-70b", "d46242408fefcd04cd34b62c3e6e74c335f1d1a6", gpu=True)
        d = client.sentiment(text,target='NLP Cloud')
        response=d['scored_labels'][1]['label']
        if response is None:
            return "Error: No response from NLP Cloud"
        return response

    def language_detection(self,text):
        client = nlpcloud.Client("python-langdetect", "d46242408fefcd04cd34b62c3e6e74c335f1d1a6", gpu=False)
        language=client.langdetection(text)
        response=language['languages'][0]
        return response
        
        
    def semantic_analysis(self, text1, text2):
        client = nlpcloud.Client("paraphrase-multilingual-mpnet-base-v2", "d46242408fefcd04cd34b62c3e6e74c335f1d1a6", gpu=False)
        response = client.semantic_similarity([text1, text2])
        if response is None:
            return "Error: No response from NLP Cloud"
        return response