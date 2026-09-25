"""PureScript emblem: opposing chevrons flank three alternating slanted bars.
HRECT_L supplies room for the three-bar rhythm. Bars share width and slope;
chevrons mirror about x=24. Ribbon outlines are reduced to single strokes.
Lucide chevron-right supplies the uninterrupted two-segment construction.
The complete mark is one emblem; brackets are not a meaningful wrapper.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "423ee93e-e3bf-4a17-8d43-6193ba22aba2"
SOURCE_PATH = "pictographic-primitives/_uncategorized_31/purescript logo_423ee93e-e3bf-4a17-8d43-6193ba22aba2.svg"
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = "purescript-chevron-emblem"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("Three Parallelograms Between Brackets",)
    keywords = ("purescript", "logo", "chevron", "emblem", "programming", "language")
    def build(self):
        for side in range(2):
            mirror=lambda x:48-x if side else x
            self.add_polyline(f'chevron-{side}',(mirror(10),16),(mirror(4),24),(mirror(10),32))
        for i,y in enumerate((10,24,38)):
            slope=2 if i%2==0 else -2
            self.add_line(f'bar-{i}',(17,y-slope),(31,y+slope))
