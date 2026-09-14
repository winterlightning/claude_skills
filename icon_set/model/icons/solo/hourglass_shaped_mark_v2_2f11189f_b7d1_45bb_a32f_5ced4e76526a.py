"""Two triangular outlines meet tip to tip as a standalone hourglass ornament."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '2f11189f-b7d1-45bb-a32f-5ced4e76526a'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/group_2f11189f-b7d1-45bb-a32f-5ced4e76526a.svg'
AUTHOR = 'gpt-6'

class HourglassShapedMarkVariant2(Solo48):
    icon_id = 'hourglass-shaped-mark-v2'
    variant_of = 'hourglass-shaped-mark'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('hourglass', 'triangle', 'geometric', 'mark', 'bowtie', 'outline', 'symbol')

    def build(self) -> None:
        self.add_polyline('upper', (24, 24), (8, 4), (40, 4), (24, 24), closed=True)
        self.add_polyline('lower', (24, 24), (40, 44), (8, 44), (24, 24), closed=True)
        self.relate('connect', 'upper', 'lower')
