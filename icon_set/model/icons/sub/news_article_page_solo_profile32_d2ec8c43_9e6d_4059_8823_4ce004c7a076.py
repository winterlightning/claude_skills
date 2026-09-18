"""Independent 32px profile of news-article-page-solo.
Snapshot of the reviewed reuse drawing; validate before publication.
Edit these primitives independently of the linked source models.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'd2ec8c43-9e6d-4059-8823-4ce004c7a076'
SOURCE_PATH = 'pictographic-primitives/content/newspaper_d2ec8c43-9e6d-4059-8823-4ce004c7a076.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d2ec8c43-9e6d-4059-8823-4ce004c7a076', 'pictographic-primitives/content/newspaper_d2ec8c43-9e6d-4059-8823-4ce004c7a076.svg'), ('d2ec8c43-9e6d-4059-8823-4ce004c7a076', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/content/newspaper_d2ec8c43-9e6d-4059-8823-4ce004c7a076.svg'))
PROFILE_SOURCE_KEYS = ('solo/news-article-page-solo', 'solo/news-article-page-solo-b005-04')
SOLO_SOURCE_ICON_IDS = ('news-article-page-solo', 'news-article-page-solo-b005-04')
REFERENCE_EXPORT_SHA256 = 'd6621b1619d0c960358bcd327148514b5572e5e34dcf89f6af9d83fd5b5f21e3'

class Drawing(Sub32):
    icon_id = 'news-article-page-solo-profile32'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = 'objects/interface-essential'
    profile_source_keys = PROFILE_SOURCE_KEYS

    def build(self):
        self.add_line('p1-r1-1', (5, 2), (20, 2))
        self.add_line('p1-r1-2', (20, 2), (27, 9))
        self.add_line('p1-r1-3', (27, 9), (27, 30))
        self.add_line('p1-r1-4', (27, 30), (5, 30))
        self.add_line('p1-r1-5', (5, 30), (5, 2))
        self.add_contour('path-1-1', 'p1-r1-1', 'p1-r1-2', 'p1-r1-3', 'p1-r1-4', 'p1-r1-5', closed=False)
        self.add_line('p2-r1-1', (11, 11), (20, 11))
        self.add_line('p2-r1-2', (20, 11), (20, 17))
        self.add_line('p2-r1-3', (20, 17), (11, 17))
        self.add_line('p2-r1-4', (11, 17), (11, 11))
        self.add_contour('path-2-1', 'p2-r1-1', 'p2-r1-2', 'p2-r1-3', 'p2-r1-4', closed=False)
        self.add_line('p3-r1-1', (11, 23), (21, 23))
        self.add_contour('path-3-1', 'p3-r1-1', closed=False)
