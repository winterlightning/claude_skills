"""Osamu Tezuka portrait: a round face under a tilted beret, with big rectangular glasses and a small smile.

Plan: SQUARE (6,6)-(42,42). The head outline is one closed loop: a beret crown of two cubics whose apex leans right (the tilted beret), the two lenses forming the sides of the head at eye level (their outer edges are the head sides), and an elliptical jaw (rx18, ry19) below. A bridge joins the lenses and a small smile sits 9 below them.
Review of the rejected drawing: the head was a box with a flat hat band and the lenses were two boxes hanging from a bar, so it read as a radio or a bag; the original is a round face with a soft beret and clear glasses.
Omissions: the beret's fringe line, its top nub and the ears, which cannot keep 8 units from the lenses on a 36-unit square.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f413d6df-ba3a-4f55-a70c-471a86b51122'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__osamu-tezuka-portrait/20260928T042731Z-thuan-mac-1/reference/kawaii manga father original creator tetsuka osamu_f413d6df-ba3a-4f55-a70c-471a86b51122.svg'
AUTHOR = "claude-fable-5-1"


class OsamuTezukaPortrait(Solo48):
    icon_id = 'osamu-tezuka-portrait'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('manga-artist-portrait', 'tezuka')
    keywords = ('osamu', 'tezuka', 'portrait', 'manga', 'beret', 'glasses', 'artist')

    def build(self) -> None:
        L, R, top, brow, chin = 6, 42, 6, 15, 23     # head sides, crown apex, lens top, lens bottom
        # beret crown: apex leans right at (28,6); both apex controls stay on y=6 so the top is exact
        self.add_bezier('crown-left', (L, brow), ((6, 9), (18, 6), (28, top)))
        self.add_bezier('crown-right', (28, top), ((36, 6), (42, 10), (R, brow)))
        # lenses double as the sides of the head
        self.add_line('lens-left-top', (L, brow), (18, brow))
        self.add_line('lens-left-inner-upper', (18, brow), (18, 19))
        self.add_line('lens-left-inner-lower', (18, 19), (18, chin))
        self.add_line('lens-left-bottom', (18, chin), (L, chin))
        self.add_line('lens-left-outer', (L, chin), (L, brow))
        self.add_contour('lens-left', 'lens-left-top', 'lens-left-inner-upper', 'lens-left-inner-lower',
                         'lens-left-bottom', 'lens-left-outer', closed=True)
        self.add_line('lens-right-top', (30, brow), (R, brow))
        self.add_line('lens-right-outer', (R, brow), (R, chin))
        self.add_line('lens-right-bottom', (R, chin), (30, chin))
        self.add_line('lens-right-inner-lower', (30, chin), (30, 19))
        self.add_line('lens-right-inner-upper', (30, 19), (30, brow))
        self.add_contour('lens-right', 'lens-right-top', 'lens-right-outer', 'lens-right-bottom',
                         'lens-right-inner-lower', 'lens-right-inner-upper', closed=True)
        self.add_line('bridge', (18, 19), (30, 19))
        # jaw: half ellipse from lens bottom corners, bottom exactly at 42
        self.add_arc('jaw', (L, chin), (R, chin), radius_x=18, radius_y=19, sweep=False)
        self.add_contour('crown', 'crown-left', 'crown-right')
        self.relate('connect', 'crown', 'lens-left')
        self.relate('connect', 'crown', 'lens-right')
        self.relate('connect', 'jaw', 'lens-left')
        self.relate('connect', 'jaw', 'lens-right')
        self.relate('connect', 'bridge', 'lens-left')
        self.relate('connect', 'bridge', 'lens-right')
        self.add_arc('smile', (21, 32), (27, 32), radius_x=6, sweep=False)
