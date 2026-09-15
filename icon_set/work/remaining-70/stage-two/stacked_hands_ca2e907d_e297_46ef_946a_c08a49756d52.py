# Refinement: Open the wrist-to-knuckle gap while preserving the shared grip endpoint.
# Repair: Move the upper wrist outward to clear the central knuckles.
"""Three hands reach in from above and the lower sides to overlap at the center. Parallel finger lines cross the topmost hand, while the forearms spread outward in three directions.
Lucide hand construction; no exact three-hand stack match. Three pairs of forearm edges meet a broad overlapping hand. Finger creases omitted. Three-direction composition remains intentionally asymmetric.
SQUARE: centerline extremes (6,6)-(42,42); freshly authored on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ca2e907d-e297-46ef-946a-c08a49756d52'
SOURCE_PATH = 'pictographic-primitives/work/workflow teamwork hand gather_ca2e907d-e297-46ef-946a-c08a49756d52.svg'
AUTHOR = 'gpt-6'

class StackedHands(Solo48):
    icon_id = 'stacked-hands'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/work'
    aliases = ()
    keywords = ('hands', 'stack', 'teamwork', 'group', 'together', 'cooperation')

    def build(self) -> None:
        self.add_polyline('central-hand', (14, 22), (22, 16), (38, 26), (30, 34), (22, 34), closed=True)
        self.add_polyline('top-left', (18, 6), (18, 16), (14, 22), closed=False)
        self.add_polyline('top-right', (34, 6), (34, 14), (40, 18), (38, 26), closed=False)
        self.add_polyline('left-upper', (6, 26), (14, 22), closed=False)
        self.add_polyline('left-lower', (6, 42), (14, 36), (22, 34), closed=False)
        self.add_line('right-upper', (42, 24), (38, 26))
        self.add_polyline('right-lower', (42, 42), (34, 36), (30, 34), closed=False)
        self.relate('connect', 'top-left', 'central-hand')
        self.relate('connect', 'top-right', 'central-hand')
        self.relate('connect', 'left-upper', 'central-hand')
        self.relate('connect', 'left-lower', 'central-hand')
        self.relate('connect', 'right-upper', 'central-hand')
        self.relate('connect', 'right-lower', 'central-hand')
        self.relate('connect', 'top-left', 'left-upper')
        self.relate('connect', 'top-right', 'right-upper')
