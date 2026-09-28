"""Remove the internal feather rib, leaving three outer feather curves and an empty feather fan. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '830efce8-4d56-4dec-b303-e983ea0fe715'
SOURCE_PATH = 'pictographic-primitives/symbol/shutterstock badminton_830efce8-4d56-4dec-b303-e983ea0fe715.svg'
AUTHOR = 'gpt-6'

class BadmintonShuttlecock(Solo48):
    icon_id = 'badminton-shuttlecock'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    categories = ('symbol', 'state')
    aliases = ()
    keywords = ('badminton', 'shuttlecock', 'sport', 'racket', 'game', 'birdie', 'court', 'play', 'sub icon')

    def build(self) -> None:
        """Symbol plan: Remove the internal feather rib, leaving three outer feather curves and an empty feather fan. Reference: inspected current parent; no useful exact Lucide match selected."""
        self.add_line('feather-left', (14, 26), (18, 10))
        self.add_arc('feather-top', (18, 10), (28, 10), radius_x=5, radius_y=4)
        self.add_arc('feather-middle', (28, 10), (38, 16), radius_x=10, radius_y=6)
        self.add_arc('feather-right', (38, 16), (42, 26), radius_x=4, radius_y=10)
        self.add_line('feather-base', (42, 26), (22, 34))
        self.add_arc('cork-bottom', (22, 34), (6, 34), radius_x=8)
        self.add_arc('cork-left', (6, 34), (14, 26), radius_x=8)
        self.add_contour('outline', 'feather-left', 'feather-top', 'feather-middle', 'feather-right', 'feather-base', 'cork-bottom', 'cork-left', closed=True)
        self.add_line('cork-divider', (14, 26), (22, 34))
        self.relate('connect', 'outline', 'cork-divider')


# Reviewed source-equivalent container sub-icon references.
SOURCE_REFERENCES = [('a72d1038-bdfa-446e-bd28-56516d6ea08b', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/badminton ball_a72d1038-bdfa-446e-bd28-56516d6ea08b.svg')]
