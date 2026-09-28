"""Fresh SOLO48 revision of horizontal-blind-with-left-pull from its claimed original reference.

The original and rejected drawing were compared before this construction.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '77c28f48-9238-51ba-ae64-d8f35d09e0b1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__horizontal-blind-with-left-pull/20260927T061852Z-thuan-mac-1/reference/blinds horizontal open_77c28f48-9238-51ba-ae64-d8f35d09e0b1.svg'
AUTHOR = "gpt-6"

class HorizontalBlindWithLeftPull(Solo48):
    icon_id = 'horizontal-blind-with-left-pull'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('horizontal', 'blind', 'with', 'left', 'pull')

    def build(self) -> None:

        # Full width slats and a weighted left pull.
        def p(x,y): return (48-x,y)
        poly(self,'headrail',p(4,8),p(44,8),p(44,16),p(4,16),closed=True)
        line(self,'support',p(8,16),p(8,32))
        for i,y in enumerate((24,32)):
            line(self,f'slat-{i}',p(4,y),p(36,y))
        line(self,'cord',p(40,16),p(40,34))
        ellipse(self,'pull',*p(40,37),3)
        contacts(self)
