'Sandbag: a broad tied neck and symmetric shoulders, with a stable level base.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '13b7d462-ded5-5fff-978a-c0240f20bf63'
SOURCE_PATH = 'pictographic-primitives/protection/protection sand bag_13b7d462-ded5-5fff-978a-c0240f20bf63.svg'
AUTHOR = 'gpt-6'

class ProtectionSandBag(Solo48):
    icon_id = 'protection-sand-bag'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'protection'
    aliases = ()
    keywords = ('protection', 'sand', 'bag')

    def build(self):
        # Sandbag: a broad tied neck and symmetric shoulders, with a stable level base.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('tie',(16,4),(32,4),(28,12),(20,12),(16,4))
        a('shoulder-left',(20,12),(10,24),10,12,sweep=False)
        p('bottom',(10,24),(8,44),(40,44),(38,24))
        a('shoulder-right',(38,24),(28,12),10,12,sweep=False)
        link('connect','shoulder-left','bottom')
        link('connect','shoulder-right','bottom')
        link('connect','shoulder-left','tie')
        link('connect','shoulder-right','tie')
