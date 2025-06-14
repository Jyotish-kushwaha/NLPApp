import nlpcloud

class MyAPI:
    def sentiment_analysis(self, text):
        client = nlpcloud.Client("finetuned-llama-3-70b", "6589ee5868328ad091bcd7a21401eddd14fa31fc", gpu=True)
        d = client.sentiment(text,target='NLP Cloud')
        response=d['scored_labels'][1]['label']
        if response is None:
            return "Error: No response from NLP Cloud"
        return response

    def language_detection(self,text):
        client = nlpcloud.Client("python-langdetect", "b44e989ef9d1294f119aa616a239a323c75257be", gpu=False)
        language=client.langdetection(text)
        response=language['languages'][0]
        print(response)
        return response
    
            
    def semantic_analysis(self, text1, text2):
        client = nlpcloud.Client("paraphrase-multilingual-mpnet-base-v2", "6589ee5868328ad091bcd7a21401eddd14fa31fc", gpu=False)
        response = client.semantic_similarity([text1, text2])
        if response is None:
            return "Error: No response from NLP Cloud"
        return response