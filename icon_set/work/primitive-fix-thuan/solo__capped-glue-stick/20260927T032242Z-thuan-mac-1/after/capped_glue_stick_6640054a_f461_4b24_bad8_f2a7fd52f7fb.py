"""Rebuild the glue stick as a narrow upright tube with a wider cap and a simple base seam. Applied to the original icon identity."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6640054a-f461-4b24-bad8-f2a7fd52f7fb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__capped-glue-stick/20260927T032242Z-thuan-mac-1/reference/paper glue_6640054a-f461-4b24-bad8-f2a7fd52f7fb.svg'
AUTHOR = 'gpt-6'

class CappedGlueStick(Solo48):
    icon_id = 'capped-glue-stick'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('glue', 'stick', 'adhesive', 'paper', 'craft', 'stationery', 'cap')

    def build(self) -> None:
        # Uniform upright case, inset vertical label and two structural seams.
        self.add_polyline('case',(12,4),(36,4),(38,6),(38,42),(36,44),(12,44),(10,42),(10,6),closed=True)
        self.add_line('cap-seam',(10,12),(38,12))
        self.add_line('base-seam',(10,36),(38,36))
        self.add_polyline('label',(20,20),(28,20),(28,28),(20,28),closed=True)
        self.relate('connect','case','cap-seam')
        self.relate('connect','case','base-seam')
