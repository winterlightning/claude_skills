'Human Ear Hearing Icon.\n\nSymbol plan: Rounded outer ear and inner fold with inward lobe; coherent curves informed by Lucide ear.\nKeyshape: VRECT_M; authored on SOLO48, not scaled from source.\nLucide: ear.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c05e8ff-9397-4507-a6d5-9c724f6dae88'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/ear_9c05e8ff-9397-4507-a6d5-9c724f6dae88.svg'
AUTHOR = 'gpt-6'

class HumanEarHearingIcon(Solo48):
    icon_id = 'human-ear-hearing-icon'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('human', 'ear', 'hearing', 'icon')

    def build(self):
        # Rounded outer ear and inner fold with inward lobe; coherent curves informed by Lucide ear.
        axis_x = 24
        p_10_18 = (10, 18)
        p_10_37 = (10, 37)
        p_10_41 = (10, 41)
        p_14_44 = (14, 44)
        p_19_11 = (19, 11)
        p_19_19 = (19, 19)
        p_19_24 = (19, 24)
        p_19_30 = (19, 30)
        p_19_44 = (19, 44)
        p_24_44 = (24, 44)
        p_26_24 = (26, 24)
        p_27_29 = (27, 29)
        p_27_36 = (27, 36)
        p_27_40 = (27, 40)
        p_28_21 = (28, 21)
        p_30_12 = (30, 12)
        p_38_18 = (2 * axis_x - p_10_18[0], p_10_18[1])
        p_38_29 = (38, 29)
        self.add_arc('outer-1', p_10_18, p_38_18, radius_x=14, radius_y=14, sweep=True)
        self.add_bezier('outer-2', p_38_18, (p_38_29, p_27_29, p_27_36))
        self.add_bezier('outer-3', p_27_36, (p_27_40, p_24_44, p_19_44))
        self.add_bezier('outer-4', p_19_44, (p_14_44, p_10_41, p_10_37))
        self.add_contour('outer', 'outer-1', 'outer-2', 'outer-3', 'outer-4', closed=False)
        self.add_bezier('inner-1', p_28_21, (p_30_12, p_19_11, p_19_19))
        self.add_bezier('inner-2', p_19_19, (p_19_24, p_26_24, p_19_30))
        self.add_contour('inner', 'inner-1', 'inner-2', closed=False)
