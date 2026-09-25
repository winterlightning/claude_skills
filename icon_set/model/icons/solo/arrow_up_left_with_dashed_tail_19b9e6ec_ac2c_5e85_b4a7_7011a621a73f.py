"""Arrow Up Left with Dashed Tail.

Plan: SQUARE centerlines (6,6)-(42,42); diagonal arrow mirrored about x=y, paired shaft and paired tail dashes.
Construction references: Lucide arrow-big-up: open shaft and continuous head contour.
Reduction: One dash per shaft edge; increased diagonal shaft width.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19b9e6ec-ac2c-5e85-b4a7-7011a621a73f'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow dash corner left up_19b9e6ec-ac2c-5e85-b4a7-7011a621a73f.svg'
SOURCE_ICON_IDS = ('19b9e6ec-ac2c-5e85-b4a7-7011a621a73f',)
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow dash corner left up_19b9e6ec-ac2c-5e85-b4a7-7011a621a73f.svg',)
AUTHOR = 'gpt-6'


class ArrowUpLeftWithDashedTail(Solo48):
    icon_id = 'arrow-up-left-with-dashed-tail'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'up', 'left', 'with', 'dashed', 'tail')

    def build(self) -> None:
        self.add_polyline("head-and-shaft",(26,34),(14,22),(6,30),(6,6),(30,6),(22,14),(34,26))
        for name,a,b in [("lower",(32,40),(34,42)),("upper",(40,32),(42,34))]:
            self.add_line(f"dash-{name}",a,b)
