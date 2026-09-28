"""Durga Face with Nose Ring.

Plan: Disembodied almond eyes, small round forehead ornament, curved mouth and large right nose ring. Merge brows into eye outlines and remove the crowded nose dot. Shared human references inform minimal facial vocabulary. Bounds (6,6)-(42,42).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '21d086a9-9520-4bd8-a1ad-5e4a483646a8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__durga-face-with-nose-ring/20260927T160114Z-thuan-mac-1/reference/navaratri_21d086a9-9520-4bd8-a1ad-5e4a483646a8.svg'
AUTHOR = 'gpt-6'

class DurgaFaceWithNoseRing(Solo48):
    icon_id = 'durga-face-with-nose-ring'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('durga', 'face', 'with', 'nose', 'ring')

    def build(self):
        # Separate almond eyes, swept brows, bindi and distinct nose ring and smile.
        self.add_arc('bindi-a',(21,9),(27,9),radius_x=3)
        self.add_arc('bindi-b',(27,9),(21,9),radius_x=3)
        self.add_contour('bindi','bindi-a','bindi-b',closed=True)
        self.add_bezier('brow-left',(8,12),((11,10),(15,10),(18,13)))
        self.add_bezier('brow-right',(30,13),((33,10),(37,10),(40,12)))
        for name,x in [('left-eye',12),('right-eye',36)]:
            self.add_arc(name+'-top',(x-6,24),(x+6,24),radius_x=6,radius_y=3)
            self.add_arc(name+'-bottom',(x+6,24),(x-6,24),radius_x=6,radius_y=3)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        self.add_bezier('nose',(22,32),((25,35),(29,35),(34,34)))
        self.add_arc('ring-a',(34,34),(42,34),radius_x=4)
        self.add_arc('ring-b',(42,34),(34,34),radius_x=4)
        self.add_contour('ring','ring-a','ring-b',closed=True)
        self.relate('connect','nose','ring')
        self.add_arc('smile',(15,39),(27,39),radius_x=6,radius_y=3,sweep=False)
