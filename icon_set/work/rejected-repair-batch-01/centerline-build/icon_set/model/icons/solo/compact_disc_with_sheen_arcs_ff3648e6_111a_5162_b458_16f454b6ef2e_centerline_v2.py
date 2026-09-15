"""Lengthen both disc reflection arcs into balanced opposing sweeps while keeping a clear open gap between their ends.
Independent centerline revision; original snapshot preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ff3648e6-111a-5162-b458-16f454b6ef2e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/cd_ff3648e6-111a-5162-b458-16f454b6ef2e.svg'
AUTHOR = 'gpt-6'

class CompactDiscWithSheenArcs(Solo48):
    icon_id = 'compact-disc-with-sheen-arcs-centerline-v2'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('cd', 'disc', 'dvd', 'media', 'storage', 'music', 'shine', 'disk')

    def build(self) -> None:

        def circle(name, cx, cy, radius):
            points = [(cx + radius, cy), (cx, cy + radius), (cx - radius, cy), (cx, cy - radius)]
            for i in range(4):
                self.add_arc(f'{name}-{i}', points[i], points[(i + 1) % 4], radius_x=radius)
            self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)
        circle('rim', 24, 24, 20)
        circle('hub', 24, 24, 2)
        self.add_arc('sheen-upper', (24, 13), (35, 28), radius_x=11)
        self.add_arc('sheen-lower', (24, 35), (13, 20), radius_x=11)
    variant_of = 'compact-disc-with-sheen-arcs'
    variant_label = 'Batch 01 centerline repair'
