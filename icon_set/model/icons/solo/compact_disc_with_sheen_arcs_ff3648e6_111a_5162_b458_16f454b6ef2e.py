'Lucide disc-3 informs paired reflection arcs. Radius-two hub and radius-eleven sheen preserve nine-unit radial gaps. CIRCLE visible radius 22; SOLO48 stroke 4.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ff3648e6-111a-5162-b458-16f454b6ef2e'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/cd_ff3648e6-111a-5162-b458-16f454b6ef2e.svg'
AUTHOR = 'gpt-6'

class CompactDiscWithSheenArcs(Solo48):
    icon_id = 'compact-disc-with-sheen-arcs'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'computers'
    categories = ('computers', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('cd', 'disc', 'dvd', 'media', 'storage', 'music', 'shine', 'disk')

    def build(self) -> None:
        # CIRCLE envelope: center (24,24), centerline radius 20, visible radius 22.
        # Shared cardinal nodes keep concentric geometry and attachments exact.
        def circle(name, cx, cy, radius):
            points = [(cx + radius, cy), (cx, cy + radius), (cx - radius, cy), (cx, cy - radius)]
            for i in range(4):
                self.add_arc(f'{name}-{i}', points[i], points[(i + 1) % 4], radius_x=radius)
            self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)
        circle('rim', 24, 24, 20)
        self.add_dot('hub', (24,24))
        self.add_arc('sheen-upper', (24, 13), (35, 24), radius_x=11)
        self.add_arc('sheen-lower', (24, 35), (13, 24), radius_x=11)
