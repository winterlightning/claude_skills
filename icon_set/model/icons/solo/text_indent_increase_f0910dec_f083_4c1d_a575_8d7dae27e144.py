'Increase Text Indent.\n\nSymbol plan: Standalone indentation layout with upper and lower abstract text rules and centered right arrow; no actual characters.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: no useful subject match; reference-informed geometric construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f0910dec-f083-4c1d-a575-8d7dae27e144'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/text width_f0910dec-f083-4c1d-a575-8d7dae27e144.svg'
AUTHOR = 'gpt-6'

class TextIndentIncrease(Solo48):
    icon_id = 'text-indent-increase'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('text', 'indent', 'increase')

    def build(self):
        # Standalone indentation layout with upper and lower abstract text rules and centered right arrow; no actual characters.
        axis_x = 24
        p_4_8 = (4, 8)
        p_4_24 = (4, 24)
        p_4_40 = (4, 40)
        p_31_17 = (31, 17)
        p_31_31 = (31, 31)
        p_38_24 = (38, 24)
        p_44_8 = (2 * axis_x - p_4_8[0], p_4_8[1])
        p_44_40 = (2 * axis_x - p_4_40[0], p_4_40[1])
        self.add_line('top-1', p_4_8, p_44_8)
        self.add_contour('top', 'top-1', closed=False)
        self.add_line('bottom-1', p_4_40, p_44_40)
        self.add_contour('bottom', 'bottom-1', closed=False)
        self.add_line('shaft-1', p_4_24, p_38_24)
        self.add_contour('shaft', 'shaft-1', closed=False)
        self.add_line('head-1', p_31_17, p_38_24)
        self.add_line('head-2', p_38_24, p_31_31)
        self.add_contour('head', 'head-1', 'head-2', closed=False)
        self.relate("connect", 'shaft', 'head')
