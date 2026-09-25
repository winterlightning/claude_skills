'Musical Kazoo Instrument.\n\nSymbol plan: Diagonal kazoo with a large membrane housing interrupting the body silhouette; inner opening omitted.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0c7edd3-bf2b-4e89-8471-4b408715e085'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kazoo_e0c7edd3-bf2b-4e89-8471-4b408715e085.svg'
AUTHOR = 'gpt-6'

class Kazoo(Solo48):
    icon_id = 'kazoo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('kazoo',)

    def build(self):
        # Diagonal kazoo with a large membrane housing interrupting the body silhouette; inner opening omitted.
        axis_x = 24
        p_6_35 = (6, 35)
        p_10_18 = (10, 18)
        p_13_42 = (13, 42)
        p_16_25 = (16, 25)
        p_17_9 = (17, 9)
        p_25_16 = (25, 16)
        p_35_6 = (35, 6)
        p_42_13 = (42, 13)
        self.add_line('kazoo-1', p_6_35, p_16_25)
        self.add_bezier('kazoo-2', p_16_25, (p_10_18, p_17_9, p_25_16))
        self.add_line('kazoo-3', p_25_16, p_35_6)
        self.add_line('kazoo-4', p_35_6, p_42_13)
        self.add_line('kazoo-5', p_42_13, p_13_42)
        self.add_line('kazoo-6', p_13_42, p_6_35)
        self.add_contour('kazoo', 'kazoo-1', 'kazoo-2', 'kazoo-3', 'kazoo-4', 'kazoo-5', 'kazoo-6', closed=True)
