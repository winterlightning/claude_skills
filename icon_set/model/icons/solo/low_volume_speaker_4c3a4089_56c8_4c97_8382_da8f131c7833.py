'Low Volume Speaker.\n\nSymbol plan: Flared speaker with one separated sound arc.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: volume-1.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4c3a4089-56c8-4c97-8382-da8f131c7833'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/volume low_4c3a4089-56c8-4c97-8382-da8f131c7833.svg'
AUTHOR = 'gpt-6'

class LowVolumeSpeaker(Solo48):
    icon_id = 'low-volume-speaker'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('low', 'volume', 'speaker')

    def build(self):
        # Flared speaker with one separated sound arc.
        axis_x = 24
        p_4_18 = (4, 18)
        p_4_30 = (4, 30)
        p_14_18 = (14, 18)
        p_14_30 = (14, 30)
        p_27_8 = (27, 8)
        p_27_40 = (27, 40)
        p_40_15 = (40, 15)
        p_40_33 = (40, 33)
        p_44_19 = (44, 19)
        p_44_21 = (44, 21)
        p_44_24 = (44, 24)
        p_44_27 = (44, 27)
        p_44_29 = (44, 29)
        self.add_line('speaker-1', p_4_18, p_14_18)
        self.add_line('speaker-2', p_14_18, p_27_8)
        self.add_line('speaker-3', p_27_8, p_27_40)
        self.add_line('speaker-4', p_27_40, p_14_30)
        self.add_line('speaker-5', p_14_30, p_4_30)
        self.add_line('speaker-6', p_4_30, p_4_18)
        self.add_contour('speaker', 'speaker-1', 'speaker-2', 'speaker-3', 'speaker-4', 'speaker-5', 'speaker-6', closed=True)
        self.add_bezier('sound-1', p_40_15, (p_44_19, p_44_21, p_44_24))
        self.add_bezier('sound-2', p_44_24, (p_44_27, p_44_29, p_40_33))
        self.add_contour('sound', 'sound-1', 'sound-2', closed=False)
