# Variant of compact-disc-with-sheen-arcs; parent file remains unchanged.
"""A compact disc with a solid hub dot and paired reflection arcs. CIRCLE preserves the radial envelope; Lucide disc-3 informs opposing reflections."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ff3648e6-111a-5162-b458-16f454b6ef2e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/cd_ff3648e6-111a-5162-b458-16f454b6ef2e.svg'
AUTHOR = 'gpt-6'

class CompactDiscWithSheenArcsVariant2(Solo48):
    icon_id = 'compact-disc-with-sheen-arcs-v2'
    variant_of = 'compact-disc-with-sheen-arcs'
    variant_label = 'Solid disc hub'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('cd', 'disc', 'dvd', 'media', 'storage', 'music', 'shine', 'disk')

    def build(self) -> None:
        self.add_arc('rim-0', (24, 2), (46, 24), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('rim-1', (46, 24), (24, 46), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('rim-2', (24, 46), (2, 24), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('rim-3', (2, 24), (24, 2), radius_x=22, radius_y=22, sweep=True, large_arc=False)
        self.add_contour('rim', 'rim-0', 'rim-1', 'rim-2', 'rim-3', closed=True)
        self.add_arc('sheen-upper', (24, 10), (38, 24), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_arc('sheen-lower', (24, 38), (10, 24), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_dot('hub', (24, 24))
