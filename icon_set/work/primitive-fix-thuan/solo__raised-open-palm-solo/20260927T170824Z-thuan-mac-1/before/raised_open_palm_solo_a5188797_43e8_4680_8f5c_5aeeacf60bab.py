'Open Hand Gesture.\n\nSymbol plan: Raised open palm with four staggered round fingers and thumb; straighten finger creases to keep eight-unit spacing. Palm leans toward lower left.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: hand.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a5188797-43e8-4680-8f5c-5aeeacf60bab'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/handful_a5188797-43e8-4680-8f5c-5aeeacf60bab.svg'
AUTHOR = 'gpt-6'

class RaisedOpenPalmSolo(Solo48):
    icon_id = 'raised-open-palm-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('raised', 'open', 'palm', 'solo')

    def build(self):
        # Raised open palm with four staggered round fingers and thumb; straighten finger creases to keep eight-unit spacing. Palm leans toward lower left.
        axis_x = 24
        p_4_20 = (4, 20)
        p_4_28 = (4, 28)
        p_5_34 = (5, 34)
        p_12_15 = (12, 15)
        p_12_23 = (12, 23)
        p_12_28 = (12, 28)
        p_12_34 = (12, 34)
        p_14_40 = (14, 40)
        p_20_12 = (20, 12)
        p_20_15 = (20, 15)
        p_20_25 = (20, 25)
        p_28_12 = (2 * axis_x - p_20_12[0], p_20_12[1])
        p_28_14 = (28, 14)
        p_28_25 = (2 * axis_x - p_20_25[0], p_20_25[1])
        p_30_40 = (30, 40)
        p_35_37 = (35, 37)
        p_36_14 = (36, 14)
        p_36_19 = (36, 19)
        p_36_28 = (2 * axis_x - p_12_28[0], p_12_28[1])
        p_44_19 = (44, 19)
        p_44_29 = (44, 29)
        p_44_35 = (44, 35)
        self.add_bezier('hand-1', p_4_28, (p_4_20, p_12_23, p_12_28))
        self.add_line('hand-2', p_12_28, p_12_15)
        self.add_arc('hand-3', p_12_15, p_20_15, radius_x=4, radius_y=4, sweep=True)
        self.add_line('hand-4', p_20_15, p_20_12)
        self.add_arc('hand-5', p_20_12, p_28_12, radius_x=4, radius_y=4, sweep=True)
        self.add_line('hand-6', p_28_12, p_28_14)
        self.add_arc('hand-7', p_28_14, p_36_14, radius_x=4, radius_y=4, sweep=True)
        self.add_line('hand-8', p_36_14, p_36_19)
        self.add_arc('hand-9', p_36_19, p_44_19, radius_x=4, radius_y=4, sweep=True)
        self.add_line('hand-10', p_44_19, p_44_29)
        self.add_bezier('hand-11', p_44_29, (p_44_35, p_35_37, p_30_40))
        self.add_line('hand-12', p_30_40, p_14_40)
        self.add_bezier('hand-13', p_14_40, (p_12_34, p_5_34, p_4_28))
        self.add_contour('hand', 'hand-1', 'hand-2', 'hand-3', 'hand-4', 'hand-5', 'hand-6', 'hand-7', 'hand-8', 'hand-9', 'hand-10', 'hand-11', 'hand-12', 'hand-13', closed=True)
        self.add_line('finger-one-1', p_20_15, p_20_25)
        self.add_contour('finger-one', 'finger-one-1', closed=False)
        self.relate("connect", 'finger-one', 'hand')
        self.add_line('finger-two-1', p_28_14, p_28_25)
        self.add_contour('finger-two', 'finger-two-1', closed=False)
        self.relate("connect", 'finger-two', 'hand')
        self.add_line('finger-three-1', p_36_19, p_36_28)
        self.add_contour('finger-three', 'finger-three-1', closed=False)
        self.relate("connect", 'finger-three', 'hand')
