"""Independent full icon-solo drawing from the original batch-04 brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd2a83b3d-ee41-4915-81af-29e371bfd9b0'
SOURCE_PATH = 'pictographic-primitives/other/magnifying glass with plus_d2a83b3d-ee41-4915-81af-29e371bfd9b0.svg'
AUTHOR = 'gpt-6'


class IndependentSolo(Solo48):
    icon_id = 'magnifying-glass-batch-04-v2'
    variant_of = 'magnifying-glass-batch-04'
    variant_label = 'Independent icon-solo; original reference only'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/tools'
    aliases = ()
    keywords = ('magnifying', 'glass', 'batch', '04')

    def build(self):
        # Plan: circle center (21,21), radius15; 3-4-5 node (30,33); radial handle.
        # SQUARE centerline extremes (6,6)-(42,42). Lucide search's single lens and stem.
        self.add_arc('lens-main',(30,33),(6,21),radius_x=15,large_arc=True,sweep=False)
        self.add_arc('lens-return',(6,21),(30,33),radius_x=15,sweep=False)
        self.add_contour('lens','lens-main','lens-return',closed=True)
        self.add_line('handle',(30,33),(42,42))
        self.relate('connect','handle','lens')
