"""Three-Light Ceiling Fixture. SQUARE centerlines (6,6)-(42,42): three heads spread across a shared canopy. Reduce the canopy to its bar and the bell flares to tapered outlines; preserve the outward angles.
Lucide lamp-ceiling / lamp-floor inform simple shades and explicit support joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f22a8a30-790b-4725-b4c1-de88b2abc933'
SOURCE_PATH = 'pictographic-primitives/lamps/lamp three_f22a8a30-790b-4725-b4c1-de88b2abc933.svg'
AUTHOR = 'gpt-6'


class ThreeLightCeilingFixture(Solo48):
    icon_id = 'three-light-ceiling-fixture'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/lighting'
    aliases = ()
    keywords = ('lamp', 'ceiling', 'fixture', 'spotlight', 'three', 'lighting')

    def build(self) -> None:
        self.add_line('cord',(24,6),(24,12))
        self.add_polyline('canopy',(12,12),(24,12),(36,12))
        self.relate('connect','cord','canopy')
        self.add_line('middle-stem',(24,12),(24,34))
        self.relate('connect','middle-stem','canopy')
        self.relate('connect','middle-stem','cord')
        self.add_polyline('middle-shade',(20,34),(24,34),(28,34),(30,42),(18,42),closed=True)
        self.relate('connect','middle-stem','middle-shade')
        for side in (-1,1):
            p='left' if side<0 else 'right'
            def pt(x,y): return (x if side<0 else 48-x,y)
            self.add_line(p+'-stem',pt(12,12),pt(13,19))
            self.add_polyline(p+'-shade',pt(10,17),pt(13,19),pt(16,21),pt(14,30),pt(6,26),closed=True)
            self.relate('connect',p+'-stem',p+'-shade')
            self.relate('connect',p+'-stem','canopy')
