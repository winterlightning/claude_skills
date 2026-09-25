"""Three white keys and two raised black keys. Shared repeated black-key width 8, step 16, and divider nodes. Extremes (4,8)-(44,40). Lucide piano keyboard divisions."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='5bc54420-3e68-4dcc-b24f-a8a9d29c4a53'
SOURCE_PATH='pictographic-primitives/music/piano keys_5bc54420-3e68-4dcc-b24f-a8a9d29c4a53.svg'
AUTHOR='gpt-6'

class PianoKeys(Solo48):
    icon_id='piano-keys'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    aliases=()
    keywords=('piano', 'keys', 'keyboard', 'instrument', 'music', 'octave', 'play')

    def build(self):
        self.add_polyline('case',(4,16),(12,16),(12,8),(20,8),(20,16),(28,16),(28,8),(36,8),(36,16),(44,16),(44,40),(32,40),(16,40),(4,40),closed=True)
        for n,x in enumerate((12,28)):
            self.add_polyline(f'black-key-{n}',(x,16),(x,28),(x+4,28),(x+8,28),(x+8,16))
            self.add_line(f'divider-{n}',(x+4,28),(x+4,40))
            self.relate('connect',f'black-key-{n}','case')
            self.relate('connect',f'divider-{n}','case')
            self.relate('connect',f'divider-{n}',f'black-key-{n}')
