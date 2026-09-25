'Prison Cell Bars.\n\nSymbol plan: Five evenly spaced prison bars connect two horizontal rails. Thick rail outlines reduce to single strokes.\nKeyshape: SQUARE; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8e9e2f83-517f-469a-92b2-445c602e2f0f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jail_8e9e2f83-517f-469a-92b2-445c602e2f0f.svg'
AUTHOR = 'gpt-6'

class PrisonBarBarrier(Solo48):
    icon_id = 'prison-bar-barrier'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('prison', 'bar', 'barrier')

    def build(self):
        # Five evenly spaced prison bars connect two horizontal rails. Thick rail outlines reduce to single strokes.
        axis_x = 24
        p_6_6 = (6, 6)
        p_6_42 = (6, 42)
        p_15_6 = (15, 6)
        p_15_42 = (15, 42)
        p_24_6 = (24, 6)
        p_24_42 = (24, 42)
        p_33_6 = (2 * axis_x - p_15_6[0], p_15_6[1])
        p_33_42 = (2 * axis_x - p_15_42[0], p_15_42[1])
        p_42_6 = (2 * axis_x - p_6_6[0], p_6_6[1])
        p_42_42 = (2 * axis_x - p_6_42[0], p_6_42[1])
        self.add_line('top-1', p_6_6, p_15_6)
        self.add_line('top-1-join-1', p_15_6, p_24_6)
        self.add_line('top-1-join-2', p_24_6, p_33_6)
        self.add_line('top-1-join-3', p_33_6, p_42_6)
        self.add_contour('top', 'top-1', 'top-1-join-1', 'top-1-join-2', 'top-1-join-3', closed=False)
        self.add_line('bottom-1', p_6_42, p_15_42)
        self.add_line('bottom-1-join-1', p_15_42, p_24_42)
        self.add_line('bottom-1-join-2', p_24_42, p_33_42)
        self.add_line('bottom-1-join-3', p_33_42, p_42_42)
        self.add_contour('bottom', 'bottom-1', 'bottom-1-join-1', 'bottom-1-join-2', 'bottom-1-join-3', closed=False)
        self.add_line('bar6-1', p_6_6, p_6_42)
        self.add_contour('bar6', 'bar6-1', closed=False)
        self.relate("connect", 'bar6', 'top')
        self.relate("connect", 'bar6', 'bottom')
        self.add_line('bar15-1', p_15_6, p_15_42)
        self.add_contour('bar15', 'bar15-1', closed=False)
        self.relate("connect", 'bar15', 'top')
        self.relate("connect", 'bar15', 'bottom')
        self.add_line('bar24-1', p_24_6, p_24_42)
        self.add_contour('bar24', 'bar24-1', closed=False)
        self.relate("connect", 'bar24', 'top')
        self.relate("connect", 'bar24', 'bottom')
        self.add_line('bar33-1', p_33_6, p_33_42)
        self.add_contour('bar33', 'bar33-1', closed=False)
        self.relate("connect", 'bar33', 'top')
        self.relate("connect", 'bar33', 'bottom')
        self.add_line('bar42-1', p_42_6, p_42_42)
        self.add_contour('bar42', 'bar42-1', closed=False)
        self.relate("connect", 'bar42', 'top')
        self.relate("connect", 'bar42', 'bottom')
