"""Fresh SOLO48 revision of horizontal-blind-with-right-pull from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '8cae4a5a-3789-5381-a527-c8750fce7a6f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-blind-with-right-pull/20260927T061852Z-thuan-mac-1/reference/blinds horizontal closed_8cae4a5a-3789-5381-a527-c8750fce7a6f.svg'
AUTHOR = "gpt-6"

class HorizontalBlindWithRightPull(Solo48):
    icon_id = 'horizontal-blind-with-right-pull'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('horizontal', 'blind', 'with', 'right', 'pull')

    def build(self) -> None:

        # Full width slats and a weighted right pull.
        poly(self,'headrail',(4,8),(44,8),(44,16),(4,16),closed=True)
        line(self,'support',(8,16),(8,32))
        for i,y in enumerate((24,32)):
            line(self,f'slat-{i}',(4,y),(36,y))
        line(self,'cord',(40,16),(40,34))
        ellipse(self,'pull',40,37,3)
        contacts(self)
