"""House with Circular Arrow. Reference preserves whole subject. Lucide house informs closed roof/body contour.
Arrow paths own their attached heads; house centered; paired valve arrows rotate as one definition.
Simplification omits house doorway and valve collar to preserve open gaps.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '2f2d2d00-4473-5ac8-a255-8067130dfca6'
SOURCE_PATH = 'pictographic-primitives/construction/renovation_2f2d2d00-4473-5ac8-a255-8067130dfca6.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'house-with-circular-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'construction'
    aliases = ()
    keywords = ('house', 'with', 'circular', 'arrow')
    def build(self):
        self.add_bezier("renewal", (40,24), ((40,35),(33,44),(24,44)), ((15,44),(8,35),(8,24)), ((8,15),(15,8),(24,8)), ((29,8),(33,9),(36,12)))
        self.add_polyline("arrowhead", (28,12),(36,12),(36,4))
        self.relate("connect", "renewal", "arrowhead")
        self.add_polyline("house", (18,25),(24,20),(30,25),(30,31),(18,31),closed=True)
