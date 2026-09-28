"""A video camera (the "smile" video call reference): a body with a lens cone.

SOLO48 HRECT_M: visible (2, 8)-(46, 40), centerline (4, 10)-(44, 38).

Symbol plan: Lucide `video`: a rounded body (r4 corners) from (4,10) to
(30,38), and on its right side a lens cone whose two edges leave the body
at y=19 and y=29 (split nodes on the side) and flare to a flat front at
x=44 spanning y=14..34; mirrored about y=24.
Revision: the rejected drawing's body had uneven corners and a pinched
lens; the camera is now the clean Lucide construction.
Construction reference: Lucide `video`.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5b89f261-bd85-4abc-8e75-64ff35cd7b4f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__smile/20260926T160211Z-thuan-mac-1/reference/smile_5b89f261-bd85-4abc-8e75-64ff35cd7b4f.svg'
AUTHOR = "claude-opus-5-5"

L, T, R, B, C = 4, 10, 30, 38, 4
LENS_ROOT_T, LENS_ROOT_B = 19, 29
FRONT_X, FRONT_T, FRONT_B = 44, 14, 34


class Drawing(Solo48):
    icon_id = 'smile'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('video camera', 'video call')
    keywords = ('video', 'camera', 'call', 'record', 'movie', 'facetime', 'smile')

    def build(self):
        self.add_line('top', (L + C, T), (R - C, T))
        self.add_arc('corner-tr', (R - C, T), (R, T + C), radius_x=C, sweep=True)
        self.add_line('right-a', (R, T + C), (R, LENS_ROOT_T))
        self.add_line('right-b', (R, LENS_ROOT_T), (R, LENS_ROOT_B))
        self.add_line('right-c', (R, LENS_ROOT_B), (R, B - C))
        self.add_arc('corner-br', (R, B - C), (R - C, B), radius_x=C, sweep=True)
        self.add_line('bottom', (R - C, B), (L + C, B))
        self.add_arc('corner-bl', (L + C, B), (L, B - C), radius_x=C, sweep=True)
        self.add_line('left', (L, B - C), (L, T + C))
        self.add_arc('corner-tl', (L, T + C), (L + C, T), radius_x=C, sweep=True)
        self.add_contour('body', 'top', 'corner-tr', 'right-a', 'right-b', 'right-c', 'corner-br', 'bottom', 'corner-bl', 'left', 'corner-tl', closed=True)
        self.add_line('lens-top', (R, LENS_ROOT_T), (FRONT_X, FRONT_T))
        self.add_line('lens-front', (FRONT_X, FRONT_T), (FRONT_X, FRONT_B))
        self.add_line('lens-bottom', (FRONT_X, FRONT_B), (R, LENS_ROOT_B))
        self.add_contour('lens', 'lens-top', 'lens-front', 'lens-bottom')
        self.relate('connect', 'lens', 'body')
