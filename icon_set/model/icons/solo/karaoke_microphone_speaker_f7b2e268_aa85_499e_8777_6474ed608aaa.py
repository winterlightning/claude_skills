'Microphone and Audio Speaker.\n\nSymbol plan: Microphone with round grille and single-stroke handle/cable beside a two-driver speaker; drivers reduced to filled marks.\nKeyshape: HRECT_L; authored on SOLO48, not scaled from source.\nLucide: mic / speaker.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f7b2e268-aa85-499e-8777-6474ed608aaa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/karaoke 2_f7b2e268-aa85-499e-8777-6474ed608aaa.svg'
AUTHOR = 'gpt-6'

class KaraokeMicrophoneSpeaker(Solo48):
    icon_id = 'karaoke-microphone-speaker'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/reference'
    aliases = ()
    keywords = ('karaoke', 'microphone', 'speaker')

    def build(self):
        # Microphone with round grille and single-stroke handle/cable beside a two-driver speaker; drivers reduced to filled marks.
        axis_x = 24
        p_4_17 = (4, 17)
        p_4_37 = (4, 37)
        p_7_14 = (7, 14)
        p_7_40 = (7, 40)
        p_14_23 = (14, 23)
        p_14_31 = (14, 31)
        p_21_14 = (21, 14)
        p_21_40 = (21, 40)
        p_24_17 = (24, 17)
        p_24_37 = (24, 37)
        p_32_14 = (32, 14)
        p_32_34 = (32, 34)
        p_34_28 = (34, 28)
        p_38_20 = (38, 20)
        p_44_14 = (44, 14)
        p_44_33 = (44, 33)
        p_44_40 = (44, 40)
        self.add_line('speaker-1', p_7_14, p_21_14)
        self.add_arc('speaker-2', p_21_14, p_24_17, radius_x=3, radius_y=3, sweep=True)
        self.add_line('speaker-3', p_24_17, p_24_37)
        self.add_arc('speaker-4', p_24_37, p_21_40, radius_x=3, radius_y=3, sweep=True)
        self.add_line('speaker-5', p_21_40, p_7_40)
        self.add_arc('speaker-6', p_7_40, p_4_37, radius_x=3, radius_y=3, sweep=True)
        self.add_line('speaker-7', p_4_37, p_4_17)
        self.add_arc('speaker-8', p_4_17, p_7_14, radius_x=3, radius_y=3, sweep=True)
        self.add_contour('speaker', 'speaker-1', 'speaker-2', 'speaker-3', 'speaker-4', 'speaker-5', 'speaker-6', 'speaker-7', 'speaker-8', closed=True)
        self.add_line('driver-top-1', p_14_23, p_14_23)
        self.add_contour('driver-top', 'driver-top-1', closed=False)
        self.add_line('driver-bottom-1', p_14_31, p_14_31)
        self.add_contour('driver-bottom', 'driver-bottom-1', closed=False)
        self.add_arc('grille-1', p_32_14, p_44_14, radius_x=6, radius_y=6, sweep=True)
        self.add_arc('grille-2', p_44_14, p_32_14, radius_x=6, radius_y=6, sweep=True)
        self.add_contour('grille', 'grille-1', 'grille-2', closed=True)
        self.add_line('handle-1', p_38_20, p_34_28)
        self.add_contour('handle', 'handle-1', closed=False)
        self.relate("connect", 'handle', 'grille')
        self.add_bezier('wire-1', p_34_28, (p_32_34, p_44_33, p_44_40))
        self.add_contour('wire', 'wire-1', closed=False)
        self.relate("connect", 'wire', 'handle')
