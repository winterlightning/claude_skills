'Partnership Agreement Handshake.\n\nSymbol plan: Clasped hands with a cuff and a single thumb fold. Fine finger creases omitted to keep the handshake clear.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: handshake.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0788c931-6c1a-4eae-bd4d-d84eeef4e11a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/global colaboration handshake_0788c931-6c1a-4eae-bd4d-d84eeef4e11a.svg'
AUTHOR = 'gpt-6'

class HorizontalHandshakeWithCuff(Solo48):
    icon_id = 'horizontal-handshake-with-cuff'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('horizontal', 'handshake', 'with', 'cuff')

    def build(self):
        # Clasped hands with a cuff and a single thumb fold. Fine finger creases omitted to keep the handshake clear.
        axis_x = 24
        p_4_12 = (4, 12)
        p_4_30 = (4, 30)
        p_12_12 = (12, 12)
        p_12_30 = (12, 30)
        p_19_18 = (19, 18)
        p_22_12 = (22, 12)
        p_22_24 = (22, 24)
        p_25_8 = (25, 8)
        p_27_19 = (27, 19)
        p_28_40 = (28, 40)
        p_30_8 = (30, 8)
        p_32_8 = (32, 8)
        p_38_29 = (38, 29)
        p_44_14 = (44, 14)
        p_44_29 = (44, 29)
        self.add_line('cuff-1', p_4_12, p_12_12)
        self.add_line('cuff-2', p_12_12, p_12_30)
        self.add_line('cuff-3', p_12_30, p_4_30)
        self.add_contour('cuff', 'cuff-1', 'cuff-2', 'cuff-3', closed=False)
        self.add_line('hands-1', p_12_12, p_22_12)
        self.add_bezier('hands-2', p_22_12, (p_25_8, p_30_8, p_32_8))
        self.add_line('hands-3', p_32_8, p_44_14)
        self.add_line('hands-4', p_44_14, p_44_29)
        self.add_line('hands-5', p_44_29, p_38_29)
        self.add_line('hands-6', p_38_29, p_28_40)
        self.add_line('hands-7', p_28_40, p_12_30)
        self.add_contour('hands', 'hands-1', 'hands-2', 'hands-3', 'hands-4', 'hands-5', 'hands-6', 'hands-7', closed=False)
        self.add_bezier('thumb-1', p_22_12, (p_19_18, p_22_24, p_27_19))
        self.add_line('thumb-2', p_27_19, p_38_29)
        self.add_contour('thumb', 'thumb-1', 'thumb-2', closed=False)
        self.relate("connect", 'hands', 'thumb')
        self.relate("connect", 'hands', 'cuff')
