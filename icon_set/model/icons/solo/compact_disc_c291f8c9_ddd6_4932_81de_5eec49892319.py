'Concentric disc and central hole, informed by Lucide disc; no detail removed. CIRCLE visible radius 22; SOLO48 stroke 4.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c291f8c9-ddd6-4932-81de-5eec49892319'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/cd_c291f8c9-ddd6-4932-81de-5eec49892319.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('c291f8c9-ddd6-4932-81de-5eec49892319', 'pictographic-primitives/computers/batch-03/cd_c291f8c9-ddd6-4932-81de-5eec49892319.svg'),)

class CompactDisc(Solo48):
    icon_id = 'compact-disc'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('compact', 'disc')

    def build(self) -> None:
        # CIRCLE envelope: center (24,24), centerline radius 20, visible radius 22.
        # Shared cardinal nodes keep concentric geometry and attachments exact.
        def circle(name, cx, cy, radius):
            points = [(cx + radius, cy), (cx, cy + radius), (cx - radius, cy), (cx, cy - radius)]
            for i in range(4):
                self.add_arc(f'{name}-{i}', points[i], points[(i + 1) % 4], radius_x=radius)
            self.add_contour(name, *[f'{name}-{i}' for i in range(4)], closed=True)
        circle('disc', 24, 24, 20)
        circle('hole', 24, 24, 6)
