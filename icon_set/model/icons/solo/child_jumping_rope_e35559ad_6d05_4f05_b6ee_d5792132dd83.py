'A child is airborne with bent legs and both arms spread outward holding a skipping rope. The rope forms a tall rounded arch over the circular head and connects near each hand.\n\nConstruction: Child jumps within an overhead rope arc. The rope terminates at both hands. Bounds (6,6)-(42,42).\nLucide: Shared Lucide construction: geometric arcs and coherent contours; no additional subject-specific original used.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e35559ad-6d05-4f05-b6ee-d5792132dd83'
SOURCE_PATH = 'pictographic-primitives/wayfinding/family child jumping rope_e35559ad-6d05-4f05-b6ee-d5792132dd83.svg'
AUTHOR = 'gpt-6'

class ChildJumpingRope(Solo48):
    icon_id = 'child-jumping-rope'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('child', 'rope', 'skipping', 'jumping', 'play', 'exercise')

    def build(self):
        # Exact shared contact nodes; continuous shapes remain coherent contours.
        self.add_line('head', (24, 16), (24, 16))
        self.add_line('body-1', (24, 25), (24, 33))
        self.add_line('arms-1', (6, 30), (15, 29))
        self.add_line('arms-2', (15, 29), (24, 25))
        self.add_line('arms-3', (24, 25), (33, 29))
        self.add_line('arms-4', (33, 29), (42, 30))
        self.add_line('legs-1', (16, 42), (24, 33))
        self.add_line('legs-2', (24, 33), (32, 42))
        self.add_arc('rope', (6, 24), (42, 24), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('rope-left', (6, 24), (6, 30))
        self.add_line('rope-right', (42, 24), (42, 30))
        self.add_contour('body', 'body-1', closed=False)
        self.add_contour('arms', 'arms-1', 'arms-2', 'arms-3', 'arms-4', closed=False)
        self.add_contour('legs', 'legs-1', 'legs-2', closed=False)
        self.relate('connect', 'body', 'arms')
        self.relate('connect', 'body', 'legs')
        self.relate('connect', 'rope', 'rope-left')
        self.relate('connect', 'rope', 'rope-right')
        self.relate('connect', 'rope-left', 'arms')
        self.relate('connect', 'rope-right', 'arms')
