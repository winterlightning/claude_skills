"""Farmer walking with hoe.
Plan: Walking farmer shoulders a long hoe; open stride and left blade. Head (26,17), r3; neck (26,28). Extrema (6,6)-(42,42).
Reference: human_ref/full_body_ref.png: circular detached heads, coherent torso and simple limbs; Lucide person-standing supports shared joints.
Reduction: Tilt simplified to an upright head and bent hip. Supporting arms merge with the shouldered hoe bar; narrow blade outline reduced to a stroke.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1898abfe-93e3-5805-8016-2bd361c14022'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__walking-farmer-shouldered-hoe/20260927T145855Z-thuan-mac-1/reference/farmer work_1898abfe-93e3-5805-8016-2bd361c14022.svg'
AUTHOR = "gpt-6"

class Batch28Icon(Solo48):
    icon_id = 'walking-farmer-shouldered-hoe'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "farming"
    categories = ("farming", "primitives")
    aliases = ()
    keywords = ('farmer', 'walking', 'with', 'hoe')

    def build(self):

        x,y,r=26,17,3
        self.add_arc('head-a',(x,y-r),(x,y+r),radius_x=r)
        self.add_arc('head-b',(x,y+r),(x,y-r),radius_x=r)
        self.add_contour('head','head-a','head-b',closed=True)

        self.add_polyline('brim',(x-10,y-r),(x-6,y-r),(x,y-r),(x+6,y-r),(x+10,y-r))
        # Broad brim alone clears the head and remains a readable farmer hat.
        self.relate('connect','head','brim')

        self.add_polyline('torso',(26,28),(26,32),(30,35))
        self.add_polyline('legs',(16,42),(30,35),(38,42));self.relate('connect','torso','legs')
        self.add_polyline('hoe',(6,28),(26,28),(36,28),(42,28))
        self.add_line('blade',(6,28),(6,38));self.relate('connect','hoe','blade')
        self.relate('connect','hoe','torso')
        self.mark_human_figure('farmer',head='head',torso='torso-1',torso_junction='start')
