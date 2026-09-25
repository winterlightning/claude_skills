"""A raised diagonal lid above a wide case and two repeated legs. Omit the lid notch and music desk. Extremes (6,6)-(42,42). Lucide piano case/keyboard construction."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='7f7177a7-92d9-4d12-8d63-4b44b0875369'
SOURCE_PATH='pictographic-primitives/music/piano_7f7177a7-92d9-4d12-8d63-4b44b0875369.svg'
AUTHOR='gpt-6'

class GrandPiano(Solo48):
    icon_id='grand-piano'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "music"
    aliases=()
    keywords=('piano', 'grand-piano', 'instrument', 'classical', 'concert', 'keyboard', 'music')

    def build(self):
        self.add_polyline('case',(6,26),(42,26),(42,34),(38,34),(10,34),(6,34),closed=True)
        self.add_polyline('lid',(6,26),(36,6),(42,26))
        self.relate('connect','lid','case')
        for n,x in enumerate((10,38)):
            self.add_line(f'leg-{n}',(x,34),(x,42))
            self.relate('connect',f'leg-{n}','case')
