"""Notes flip (content), converted from the icons-json construction graph by json_to_solo --mode bezier. VRECT_L keyshape; curves kept as cubic beziers."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd68affa5-659e-5b1e-8361-c17d53d111df'
SOURCE_PATH = 'icons-json/content/notes flip_d68affa5-659e-5b1e-8361-c17d53d111df.json'
AUTHOR = 'json_to_solo'

class NotesFlipContent(Solo48):
    icon_id = 'notes-flip-content'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    aliases = ()
    keywords = ('notes', 'flip', 'content')

    def build(self):
        self.add_line('e0', (15, 13), (33, 13))
        self.add_line('e1', (15, 21), (33, 21))
        self.add_line('e2', (15, 29), (27, 29))
        self.add_line('e3', (8, 39), (8, 8))
        self.add_line('e4', (12, 4), (36, 4))
        self.add_line('e5', (40, 9), (40, 40))
        self.add_line('e6', (35, 44), (10, 44))
        self.add_bezier('e7', (8, 8), ((8, 7.636), (8.01, 6.909), (8.01, 6.555)), ((8.01, 5.373), (9.32, 4.009), (10.66, 4.009)), ((10.96, 4.009), (11.25, 4), (11.55, 4)), ((11.7, 4), (11.85, 4), (12, 4)))
        self.add_bezier('e8', (36, 4), ((36.11, 4), (36.21, 4), (36.32, 4)), ((39.02, 4), (40, 5.809), (40, 8.036)), ((40, 8.209), (40, 8.827), (40, 9)))
        self.add_bezier('e9', (40, 40), ((40, 40.155), (39.98, 40.673), (39.98, 40.827)), ((39.98, 42.264), (38.34, 44), (36.71, 44)), ((36.46, 44), (36.21, 44), (35.96, 44)), ((35.76, 44), (35.55, 44), (35.35, 44)), ((35.23, 44), (35.12, 44), (35, 44)))
        self.add_bezier('e10', (10, 44), ((9.03, 42.627), (8.02, 41.409), (8.02, 39.709)), ((8.01, 39.627), (8.01, 39.082), (8, 39)))
        self.add_contour('c0', 'e0')
        self.add_contour('c1', 'e1')
        self.add_contour('c2', 'e2')
        self.add_contour('c3', 'e3', 'e7', 'e4', 'e8', 'e5', 'e9', 'e6', 'e10', closed=True)
