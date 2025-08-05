import nlpcloud

class MyAPI:
    def sentiment_analysis(self, text):
        client = nlpcloud.Client("finetuned-llama-3-70b", "b44e989ef9d1294f119aa616a239a323c75257be", gpu=True)
        d = client.sentiment(text,target='NLP Cloud')
        response=d['scored_labels'][1]['label']
        if response is None:
            return "Error: No response from NLP Cloud"
        return response

    def language_detection(self,text):
        client = nlpcloud.Client("python-langdetect", "0292b9a164d1f648374ec2481a1c22bee43d5ad5", gpu=False)
        language=client.langdetection(text)
        response=language['languages'][0]
        print(response)
        return response
    
            
    def semantic_analysis(self, text1, text2):
        client = nlpcloud.Client("paraphrase-multilingual-mpnet-base-v2", "0292b9a164d1f648374ec2481a1c22bee43d5ad5", gpu=False)
        response = client.semantic_similarity([text1, text2])
        if response is None:
            return "Error: No response from NLP Cloud"
        return response
