from collections import defaultdict

class Author:
    def __init__(self, name):
      
        self.name = name
        self._articles=[]

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, 'name') and self._name is not None:
             return
        elif type(value) is not str or len(value) == 0:
            return
        self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))


class Magazine:
    def __init__(self, name, category):
        
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) is str and 2 <= len(value) <= 16: 
             self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if  isinstance(value, str) and len(value) > 0:
             self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles if titles else None

    
    def contributing_authors(self):
        articles_per_author = defaultdict(int)
        for article in self.articles():
            articles_per_author[article.author] += 1
        contributing_authors = [author for author, count in articles_per_author.items() if count > 2]
        return contributing_authors if contributing_authors else None
    
    
class Article:
    all = []

    def __init__(self, author, magazine, title):
        
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if type (value) is not str or len(value) == 0: 
           return 
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if  isinstance(value, Magazine):
            self._magazine = value
        else:
            raise ValueError("Magazine must be an instance of Magazine class")
