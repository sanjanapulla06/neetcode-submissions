class Solution:
    def __init__(self):
        self.url_to_id = {}
        self.id_to_url = {}
        self.count = 0

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.url_to_id:
            self.count += 1
            shortUrl = str(self.count)
            self.url_to_id[longUrl] = shortUrl
            self.id_to_url[shortUrl] = longUrl

        return self.url_to_id[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.id_to_url[shortUrl]