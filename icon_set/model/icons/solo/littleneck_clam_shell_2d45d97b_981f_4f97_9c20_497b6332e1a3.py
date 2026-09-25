'Littleneck Clam Shell.\n\nSymbol plan: Clam shell with broad hinge and one inset arch; reduce nested ridges.\nKeyshape: VRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2d45d97b-981f-4f97-9c20-497b6332e1a3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/littleneck_2d45d97b-981f-4f97-9c20-497b6332e1a3.svg'
AUTHOR = 'gpt-6'

class LittleneckClamShell(Solo48):
    icon_id = 'littleneck-clam-shell'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('littleneck', 'clam', 'shell')

    def build(self):
        # Clam shell with broad hinge and one inset arch; reduce nested ridges.
        axis_x = 24
        p_8_9 = (8, 9)
        p_8_18 = (8, 18)
        p_8_22 = (8, 22)
        p_9_29 = (9, 29)
        p_10_44 = (10, 44)
        p_14_4 = (14, 4)
        p_14_20 = (14, 20)
        p_14_34 = (14, 34)
        p_16_14 = (16, 14)
        p_19_26 = (19, 26)
        p_24_4 = (24, 4)
        p_24_14 = (24, 14)
        p_29_26 = (2 * axis_x - p_19_26[0], p_19_26[1])
        p_32_14 = (2 * axis_x - p_16_14[0], p_16_14[1])
        p_34_4 = (2 * axis_x - p_14_4[0], p_14_4[1])
        p_34_20 = (2 * axis_x - p_14_20[0], p_14_20[1])
        p_34_34 = (2 * axis_x - p_14_34[0], p_14_34[1])
        p_38_44 = (2 * axis_x - p_10_44[0], p_10_44[1])
        p_39_29 = (2 * axis_x - p_9_29[0], p_9_29[1])
        p_40_9 = (2 * axis_x - p_8_9[0], p_8_9[1])
        p_40_18 = (2 * axis_x - p_8_18[0], p_8_18[1])
        p_40_22 = (2 * axis_x - p_8_22[0], p_8_22[1])
        self.add_bezier('shell-1', p_14_34, (p_9_29, p_8_22, p_8_18))
        self.add_bezier('shell-2', p_8_18, (p_8_9, p_14_4, p_24_4))
        self.add_bezier('shell-3', p_24_4, (p_34_4, p_40_9, p_40_18))
        self.add_bezier('shell-4', p_40_18, (p_40_22, p_39_29, p_34_34))
        self.add_line('shell-5', p_34_34, p_38_44)
        self.add_line('shell-6', p_38_44, p_10_44)
        self.add_line('shell-7', p_10_44, p_14_34)
        self.add_contour('shell', 'shell-1', 'shell-2', 'shell-3', 'shell-4', 'shell-5', 'shell-6', 'shell-7', closed=True)
        self.add_bezier('ridge-1', p_19_26, (p_14_20, p_16_14, p_24_14))
        self.add_bezier('ridge-2', p_24_14, (p_32_14, p_34_20, p_29_26))
        self.add_contour('ridge', 'ridge-1', 'ridge-2', closed=False)
