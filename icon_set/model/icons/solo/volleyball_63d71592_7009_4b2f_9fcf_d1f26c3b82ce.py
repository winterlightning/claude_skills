'Professional Sports Volleyball Ball.\n\nSymbol plan: Volleyball with three broad curved panel groups. Reduce repeated fine seams while preserving the wrapped panel construction.\nKeyshape: CIRCLE; authored on SOLO48, not scaled from source.\nLucide: volleyball.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '63d71592-7009-4b2f-9fcf-d1f26c3b82ce'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/volleyball_63d71592-7009-4b2f-9fcf-d1f26c3b82ce.svg'
AUTHOR = 'gpt-6'

class Volleyball(Solo48):
    icon_id = 'volleyball'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('volleyball',)

    def build(self):
        # Volleyball with three broad curved panel groups. Reduce repeated fine seams while preserving the wrapped panel construction.
        axis_x = 24
        p_4_24 = (4, 24)
        p_13_18 = (13, 18)
        p_13_30 = (13, 30)
        p_15_9 = (15, 9)
        p_15_40 = (15, 40)
        p_16_24 = (16, 24)
        p_23_26 = (23, 26)
        p_24_4 = (24, 4)
        p_24_44 = (24, 44)
        p_34_26 = (34, 26)
        p_44_24 = (2 * axis_x - p_4_24[0], p_4_24[1])
        self.add_arc('ball-1', p_24_4, p_44_24, radius_x=20, radius_y=20, sweep=True)
        self.add_arc('ball-2', p_44_24, p_24_44, radius_x=20, radius_y=20, sweep=True)
        self.add_arc('ball-3', p_24_44, p_4_24, radius_x=20, radius_y=20, sweep=True)
        self.add_arc('ball-4', p_4_24, p_24_4, radius_x=20, radius_y=20, sweep=True)
        self.add_contour('ball', 'ball-1', 'ball-2', 'ball-3', 'ball-4', closed=True)
        self.add_bezier('sweep-a-1', p_24_4, (p_15_9, p_13_18, p_16_24))
        self.add_bezier('sweep-a-2', p_16_24, (p_23_26, p_34_26, p_44_24))
        self.add_contour('sweep-a', 'sweep-a-1', 'sweep-a-2', closed=False)
        self.add_bezier('sweep-b-1', p_16_24, (p_13_30, p_15_40, p_24_44))
        self.add_contour('sweep-b', 'sweep-b-1', closed=False)
        self.relate("connect", 'sweep-a', 'ball')
        self.relate("connect", 'sweep-b', 'ball')
        self.relate("connect", 'sweep-a', 'sweep-b')
