'Microphone: circular capsule ends, a concentric cradle and no cramped grille ticks.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43ee606c-4f75-4eea-ae65-cbce49a24ba4'
SOURCE_PATH = 'pictographic-primitives/audio/microphone_43ee606c-4f75-4eea-ae65-cbce49a24ba4.svg'
AUTHOR = 'gpt-6'

class MicrophoneAudio(Solo48):
    icon_id = 'microphone-audio'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('microphone', 'audio')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('capsule-1', (24, 4), (31, 11), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('capsule-2', (31, 11), (31, 21))
        self.add_arc('capsule-3', (31, 21), (24, 28), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_arc('capsule-5', (24, 28), (17, 21), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('capsule-6', (17, 21), (17, 11))
        self.add_arc('capsule-7', (17, 11), (24, 4), radius_x=7, radius_y=7, large_arc=False, sweep=True)
        self.add_line('support-left', (8, 22), (8, 24))
        self.add_arc('support-bottom', (8, 24), (40, 24), radius_x=16, radius_y=16, large_arc=False, sweep=False)
        self.add_line('support-right', (40, 24), (40, 22))
        self.add_line('stem', (24, 40), (24, 44))
        self.add_contour('capsule', *('capsule-1', 'capsule-2', 'capsule-3', 'capsule-5', 'capsule-6', 'capsule-7'), closed=True)
        self.add_contour('support', *('support-left', 'support-bottom', 'support-right'), closed=False)
        self.relate('connect', *('stem', 'support'))
