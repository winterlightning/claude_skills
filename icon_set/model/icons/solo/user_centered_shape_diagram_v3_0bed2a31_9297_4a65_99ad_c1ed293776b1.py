"""Independent full icon-solo drawing from the original batch-04 brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0bed2a31-9297-4a65-99ad-c1ed293776b1'
SOURCE_PATH = 'pictographic-primitives/users/user experience design_0bed2a31-9297-4a65-99ad-c1ed293776b1.svg'
AUTHOR = 'gpt-6'


class IndependentSolo(Solo48):
    icon_id = 'user-centered-shape-diagram-v3'
    variant_of = 'user-centered-shape-diagram'
    variant_label = 'Independent icon-solo; original reference only'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'users'
    categories = ('users', 'primitives')
    aliases = ()
    keywords = ('user', 'centered', 'shape', 'diagram')

    def build(self):
        # Plan: central bust; square above, circle left, triangle right; three orbit arcs.
        # SQUARE extremes (6,6)-(42,42); user.svg anatomy and Lucide shapes.
        self.add_polyline('square',(20,6),(28,6),(28,14),(20,14),closed=True)
        self.add_arc('head-top',(21,24),(27,24),radius_x=3)
        self.add_arc('head-bottom',(27,24),(21,24),radius_x=3)
        self.add_contour('head','head-top','head-bottom',closed=True)
        # Exact 8 centerline / 4 ink head-to-shoulder gap, circular head.
        self.add_arc('shoulder-left',(18,41),(24,35),radius_x=6)
        self.add_arc('shoulder-right',(24,35),(30,41),radius_x=6)
        self.add_contour('shoulders','shoulder-left','shoulder-right')
        self.add_arc('circle-top',(6,30),(14,30),radius_x=4)
        self.add_arc('circle-bottom',(14,30),(6,30),radius_x=4)
        self.add_contour('circle','circle-top','circle-bottom',closed=True)
        self.add_polyline('triangle',(37,26),(42,35),(32,35),closed=True)
        self.add_bezier('orbit-left',(7,21),((7,17),(10,13),(13,12)))
        self.add_bezier('orbit-right',(35,12),((39,15),(41,19),(41,22)))
        self.add_bezier('orbit-bottom',(16,40),((18,41),(21,42),(24,42)),((27,42),(30,41),(32,40)))
