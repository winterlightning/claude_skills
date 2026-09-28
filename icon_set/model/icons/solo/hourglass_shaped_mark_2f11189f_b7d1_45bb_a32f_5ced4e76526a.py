"""Two triangular outlines meet tip to tip as a standalone hourglass ornament."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2f11189f-b7d1-45bb-a32f-5ced4e76526a'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/group_2f11189f-b7d1-45bb-a32f-5ced4e76526a.svg'
AUTHOR = 'gpt-6'

class HourglassShapedMark(Solo48):
    icon_id = 'hourglass-shaped-mark'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    categories = ('primitives', 'decoration')
    aliases = ()
    keywords = ('hourglass', 'triangle', 'geometric', 'mark', 'bowtie', 'outline', 'symbol')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_polyline('upper', (24, 24), (8, 4), (40, 4), (24, 24), closed=True)
        self.add_polyline('lower', (24, 24), (40, 44), (8, 44), (24, 24), closed=True)
        self.relate('connect', 'upper', 'lower')
