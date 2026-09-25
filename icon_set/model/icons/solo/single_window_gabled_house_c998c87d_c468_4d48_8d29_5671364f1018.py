'House with Window.\n\nSymbol plan: Gabled house and centered window; omit pane cross because four tiny panes cannot retain required openings.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: house.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c998c87d-c468-4d48-8d29-5671364f1018'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/sunroom_c998c87d-c468-4d48-8d29-5671364f1018.svg'
AUTHOR = 'gpt-6'

class SingleWindowGabledHouse(Solo48):
    icon_id = 'single-window-gabled-house'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('single', 'window', 'gabled', 'house')

    def build(self):
        # Gabled house and centered window; omit pane cross because four tiny panes cannot retain required openings.
        axis_x = 24
        p_6_22 = (6, 22)
        p_6_42 = (6, 42)
        p_19_25 = (19, 25)
        p_19_33 = (19, 33)
        p_24_6 = (24, 6)
        p_29_25 = (2 * axis_x - p_19_25[0], p_19_25[1])
        p_29_33 = (2 * axis_x - p_19_33[0], p_19_33[1])
        p_42_22 = (2 * axis_x - p_6_22[0], p_6_22[1])
        p_42_42 = (2 * axis_x - p_6_42[0], p_6_42[1])
        self.add_line('house-1', p_6_22, p_24_6)
        self.add_line('house-2', p_24_6, p_42_22)
        self.add_line('house-3', p_42_22, p_42_42)
        self.add_line('house-4', p_42_42, p_6_42)
        self.add_line('house-5', p_6_42, p_6_22)
        self.add_contour('house', 'house-1', 'house-2', 'house-3', 'house-4', 'house-5', closed=True)
        self.add_line('window-1', p_19_25, p_29_25)
        self.add_line('window-2', p_29_25, p_29_33)
        self.add_line('window-3', p_29_33, p_19_33)
        self.add_line('window-4', p_19_33, p_19_25)
        self.add_contour('window', 'window-1', 'window-2', 'window-3', 'window-4', closed=True)
