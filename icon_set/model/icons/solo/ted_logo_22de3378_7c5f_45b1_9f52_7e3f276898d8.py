"""Three monoline capital letters in a shared 32-unit height. Preserve TED as a complete wordmark with a true D counter and even horizontal bar levels."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22de3378-7c5f-45b1-9f52-7e3f276898d8'
SOURCE_PATH = 'pictographic-primitives/logos/ted logo_22de3378-7c5f-45b1-9f52-7e3f276898d8.svg'
AUTHOR = 'gpt-6'

class TedLogo(Solo48):
    icon_id = 'ted-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('ted', 'talks', 'conference', 'wordmark', 'logo', 'brand', 'ideas')

    def build(self):
        # Plan: Three monoline capital letters in a shared 32-unit height. Preserve TED as a complete wordmark with a true D counter and even horizontal bar levels.
        # Exact keyshape ink extremes are owned by Keyshape.HRECT_L on SOLO48.

        self.add_polyline('t-top',(4,8),(8,8),(12,8));self.add_line('t-stem',(8,8),(8,40));self.relate('connect','t-top','t-stem')
        self.add_polyline('e',(27,8),(20,8),(20,24),(20,40),(27,40));self.add_line('e-mid',(20,24),(27,24));self.relate('connect','e','e-mid')
        self.add_line('d-stem',(36,8),(36,40));self.add_arc('d-bowl',(36,40),(36,8),radius_x=8,radius_y=16,sweep=False);self.add_contour('d','d-stem','d-bowl',closed=True)

