import hashlib

class URLShortener:
    """
    Mini URL shortener.

    Store:
    - code_to_url   : short_code -> long_url
    - url_to_code   : long_url -> short_code
    - click_counts  : short_code -> int

    Collision rule:
    - If generated code already exists for another URL,
      generate a new one using an extra value (counter).
    """

    def __init__(self):
        self.code_to_url = {}  # code -> url
        self.url_to_code = {}  # url -> code
        self.click_counts = {}  # code -> click_count

    def _make_code(self, url, extra=""):
        """
        Create a short code using hashing.

        :param url: URL to be shortened
        :param extra: extra string to handle collisions
        :return: first 6 characters of the MD5 hash of (url + extra)
        """
        # Generate MD5 hash and return the first 6 characters
        digest = hashlib.md5((url + extra).encode()).hexdigest()
        return digest[:6]

    def shorten(self, url):
        """
        Return a short code for the URL.
        - If URL already shortened, return existing code
        - Otherwise generate code
        - Resolve collisions if code belongs to a different URL
        - Save mappings + click count = 0
        """
        # Check if the URL already has a short code
        if url in self.url_to_code:
            return self.url_to_code[url]
        
        # Generate the short code
        code = self._make_code(url)
        extra = ""
        counter = 1
        
        # Resolve collision by appending counter to the hash
        while code in self.code_to_url and self.code_to_url[code] != url:
            extra = str(counter)
            code = self._make_code(url, extra)
            counter += 1
        
        # Save the mappings
        self.code_to_url[code] = url
        self.url_to_code[url] = code
        self.click_counts[code] = 0  # Initialize click count to 0

        return code

    def open_url(self, code):
        """
        Return original URL and increase click count.
        Return None if code not found.
        """
        if code not in self.code_to_url:
            return None
        
        # Increase click count
        self.click_counts[code] += 1
        return self.code_to_url[code]

    def get_stats(self, code):
        """
        Return a dictionary with:
        { "code": ..., "url": ..., "clicks": ... }
        Return None if code not found.
        """
        if code not in self.code_to_url:
            return None
        
        url = self.code_to_url[code]
        clicks = self.click_counts[code]
        return {"code": code, "url": url, "clicks": clicks}


# FOR TESTING:

shortener = URLShortener()

url1 = "https://example.com/products/usb-cable"
url2 = "https://example.com/about"
url3 = "https://example.com/products/usb-cable"  # same as url1

# Shorten URLs
code1 = shortener.shorten(url1)
code2 = shortener.shorten(url2)
code3 = shortener.shorten(url3)

print("Codes:", code1, code2, code3)  # code1 and code3 should match
print("Open code1:", shortener.open_url(code1))  # Should return the original URL
print("Open code1 again:", shortener.open_url(code1))  # Should increase click count
print("Stats code1:", shortener.get_stats(code1))  # Should show click count and URL