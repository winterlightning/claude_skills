"""News Article Page: user-requested grid-fitted 32px version of news-article-page-solo.
Plan: retain source primitive/contour topology and fit VRECT_XL ink (2, 0, 30, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='d2ec8c43-9e6d-4059-8823-4ce004c7a076'
SOURCE_PATH='pictographic-primitives/content/newspaper_d2ec8c43-9e6d-4059-8823-4ce004c7a076.svg'
SOLO_SOURCE_ICON_ID='news-article-page-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='news-article-page-sub32'
    keyshape=Keyshape.VRECT_XL
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'news article page')
    def build(self):
        self.add_line('page-1', (4, 2), (20, 2))
        self.add_line('page-2', (20, 2), (28, 9))
        self.add_line('page-3', (28, 9), (28, 30))
        self.add_line('page-4', (28, 30), (4, 30))
        self.add_line('page-5', (4, 30), (4, 2))
        self.add_line('picture-1', (11, 11), (20, 11))
        self.add_line('picture-2', (20, 11), (20, 17))
        self.add_line('picture-3', (20, 17), (11, 17))
        self.add_line('picture-4', (11, 17), (11, 11))
        self.add_line('text', (11, 23), (21, 23))
        self.add_contour('page', 'page-1', 'page-2', 'page-3', 'page-4', 'page-5', closed=True)
        self.add_contour('picture', 'picture-1', 'picture-2', 'picture-3', 'picture-4', closed=True)
        self.add_anchor('center',(16, 16))
