'Loading: shorten the inward ends of eight balanced radial strokes to open the centre.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f025f753-a8b5-5dd6-a9ba-8ae928ebf25e'
SOURCE_PATH = 'pictographic-primitives/interface-essential/loading_f025f753-a8b5-5dd6-a9ba-8ae928ebf25e.svg'
AUTHOR = 'gpt-6'

class LoadingF025f753(Solo48):
    icon_id = 'loading-f025f753'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('loading', 'interface-essential')

    def build(self) -> None:
        # Eight equal radial sectors with a clear centre, reflected on the integer grid.
        for i,(a,b) in enumerate((((6,24),(12,24)),((36,24),(42,24)),((24,6),(24,12)),((24,36),(24,42)),((12,12),(16,16)),((32,16),(36,12)),((12,36),(16,32)),((32,32),(36,36)))):
            self.add_line(f'ray-{i}',a,b)
