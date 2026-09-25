'Lard Block in Container.\n\nSymbol plan: Domed lard mound on a broad shallow tray; omit small facet.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '021f2cff-c2ae-4ed2-ad66-8ee015332b9b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/lard_021f2cff-c2ae-4ed2-ad66-8ee015332b9b.svg'
AUTHOR = 'gpt-6'

class LardOnTray(Solo48):
    icon_id = 'lard-on-tray'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('lard', 'on', 'tray')

    def build(self):
        # Domed lard mound on a broad shallow tray; omit small facet.
        axis_x = 24
        p_4_29 = (4, 29)
        p_4_34 = (4, 34)
        p_9_13 = (9, 13)
        p_9_29 = (9, 29)
        p_10_40 = (10, 40)
        p_15_8 = (15, 8)
        p_24_8 = (24, 8)
        p_33_8 = (2 * axis_x - p_15_8[0], p_15_8[1])
        p_38_40 = (2 * axis_x - p_10_40[0], p_10_40[1])
        p_39_13 = (2 * axis_x - p_9_13[0], p_9_13[1])
        p_39_29 = (2 * axis_x - p_9_29[0], p_9_29[1])
        p_44_29 = (2 * axis_x - p_4_29[0], p_4_29[1])
        p_44_34 = (2 * axis_x - p_4_34[0], p_4_34[1])
        self.add_line('tray-1', p_4_29, p_44_29)
        self.add_line('tray-2', p_44_29, p_44_34)
        self.add_arc('tray-3', p_44_34, p_38_40, radius_x=6, radius_y=6, sweep=True)
        self.add_line('tray-4', p_38_40, p_10_40)
        self.add_arc('tray-5', p_10_40, p_4_34, radius_x=6, radius_y=6, sweep=True)
        self.add_line('tray-6', p_4_34, p_4_29)
        self.add_contour('tray', 'tray-1', 'tray-2', 'tray-3', 'tray-4', 'tray-5', 'tray-6', closed=True)
        self.add_bezier('lard-1', p_9_29, (p_9_13, p_15_8, p_24_8))
        self.add_bezier('lard-2', p_24_8, (p_33_8, p_39_13, p_39_29))
        self.add_contour('lard', 'lard-1', 'lard-2', closed=False)
        self.relate("connect", 'tray', 'lard')
