import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key('lEWYDntznLXsB3caGihszyeGQOeudGzkDrjoMVxjEmk')
        #paralleldots.get_api_key()

    def sentiment_analysis(self,text):
        response = paralleldots.sentiment(text)
        return response

    def abuse_detection(self,text):
        response = paralleldots.abuse(text)
        return response

    def emotion_detection(self,text):
        response = paralleldots.emotion(text)
        return response

