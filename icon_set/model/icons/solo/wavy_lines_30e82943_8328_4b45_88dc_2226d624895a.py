"""Two left-aligned wave strokes; a longer upper row and shorter lower row. HRECT extremes (4,8)-(44,40). Repeated tangent half-ellipses own wavelength and amplitude.
Reduction: Reduced the top row to two broad wave cycles and the lower row to one.
Lucide construction: No useful local wave match; repeated tangent ellipse construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '30e82943-8328-4b45-88dc-2226d624895a'
SOURCE_PATH = 'pictographic-primitives/nature/notes paper text_30e82943-8328-4b45-88dc-2226d624895a.svg'
AUTHOR = 'gpt-6'


class WavyLines(Solo48):
    icon_id = 'wavy-lines'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('waves', 'wavy', 'lines', 'water', 'wind', 'flow', 'text', 'ripple')

    def build(self) -> None:
        for row,(y,count) in enumerate(((12,4),(36,2))):
            members=[]
            for i in range(count):
                name=f"wave-{row}-{i}"
                self.add_arc(name,(4+10*i,y),(14+10*i,y),radius_x=5,radius_y=4,sweep=i%2==0)
                members.append(name)
            self.add_contour(f"row-{row}",*members)
