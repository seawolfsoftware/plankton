from enum import Enum


class Curation(str, Enum):
    """
    Curations allow the API consumer to specify a curated set of content
    and describes the scope against which a Query will operate.
    It is not a format type.
    """
    Articles = "ARTICLES"
    Blogs = "BLOGS"
    Pages = "PAGES"
    Podcasts = "PODCASTS"
    Videos = "VIDEOS"
