class CommentsRepository:
    def __init__(self):
        self.comments = [
            {"id": 1, "text": "Life is good", "categories": "positive", "date": "2023-02-5"},
            {"id": 2, "text": "All will be great if you will be good man", "categories": "positive","date": "2023-02-4"},
            {"id": 3, "text": "nothing to do it's a thrill", "categories": "negative", "date": "2023-02-3"},
            {"id": 4, "text": "Don't need work you need only sleep", "categories": "negative", "date": "2023-02-2"},
            {"id": 5, "text": "Sample text 1", "categories": "positive", "date": "2023-02-01"},
            {"id": 6, "text": "Sample text 2", "categories": "negative", "date": "2023-01-31"},
            {"id": 7, "text": "Another positive statement", "categories": "positive", "date": "2023-01-30"},
            {"id": 8, "text": "Negative sentiment expressed here", "categories": "negative", "date": "2023-01-29"},
            {"id": 9, "text": "Positivity shines through", "categories": "positive", "date": "2023-01-28"},
            {"id": 10,"text": "A negative outlook on life", "categories": "negative", "date": "2023-01-27"}
        ]

    def get_all(self):
        return self.comments

    def search(self, text):
        res = []
        for comment in self.comments:
            if text.lower() in comment['text'].lower():
                res.append(comment)
        return res

    def save(self, comment):
        comment['id'] = self.get_next_id()
        self.comments.insert(0, comment)
        return comment

    def get_next_id(self):
        return len(self.comments) + 1