class PageBuilder:
    def __init__(self):
        self.page_title = ""
        self.page_poster_path = ""
        self.story_pages = []
        #   Example of page: 
        #   {
        #       "title": "Hello World!",
        #       "description": "This is a test description",
        #       "path_to_image": "assets/images/test.jpg",
        #   }

    def add_page_title(self, title):
        self.page_title = title

    def add_page_poster(self, poster_path):
        self.page_poster_path = poster_path

    def add_page_story(self, story_title, story_desc, story_path):
        self.story_pages.append({
            "title": story_title,
            "description": story_desc,
            "path_to_image": story_path
        })

    def build_page(self):
        return