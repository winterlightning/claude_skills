"""An upright light bulb with a rounded envelope, narrow neck and small rounded terminal. Five short rays spread above and beside the glass, and a horizontal line marks the base.
Mirrored glass and five rays; Lucide lightbulb. Five rays reduced to dots; flat socket base remains intrinsic to the glass outline.
Keyshape SQUARE; centerline extremes (6,6)-(42,42). Square envelope balances the complete scene. Source inspected as a standalone physical or conceptual subject."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd2aca27-c840-4398-bf95-7914b16b0275'
SOURCE_PATH = 'pictographic-primitives/work/bulb_dd2aca27-c840-4398-bf95-7914b16b0275.svg'
AUTHOR = 'gpt-6'


class GlowingLightBulb(Solo48):
    icon_id = 'glowing-light-bulb'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('bulb', 'light', 'glow', 'idea', 'lamp', 'illumination')

    def build(self) -> None:
        self.add_arc('glass-top', (15, 24), (33, 24), radius_x=9, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('glass-right', (33, 24), (29, 34), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_line('neck-right', (29, 34), (29, 42))
        self.add_line('base', (29, 42), (19, 42))
        self.add_line('neck-left', (19, 42), (19, 34))
        self.add_arc('glass-left', (19, 34), (15, 24), radius_x=14, radius_y=14, sweep=True, large_arc=False)
        self.add_contour('glass', 'glass-top', 'glass-right', 'neck-right', 'base', 'neck-left', 'glass-left', closed=True)
        self.add_dot('ray-top', (24, 6))
        self.add_dot('ray-left', (6, 24))
        self.add_dot('ray-right', (42, 24))
        self.add_dot('ray-nw', (10, 10))
        self.add_dot('ray-ne', (38, 10))

SOURCE_REFERENCES = (('6230f0a2-a422-49f8-9b63-57668a37457e', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/lightbulb on_6230f0a2-a422-49f8-9b63-57668a37457e.svg'),)
