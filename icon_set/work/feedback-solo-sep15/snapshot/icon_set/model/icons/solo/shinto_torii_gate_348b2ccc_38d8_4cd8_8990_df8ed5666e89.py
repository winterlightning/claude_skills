"""A torii gate with upturned upper beam, lower crossbar and splayed posts. Keep all defining gate parts; no useful local exact Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '348b2ccc-38d8-4cd8-8990-df8ed5666e89'
SOURCE_PATH = 'pictographic-primitives/religion/shinto_348b2ccc-38d8-4cd8-8990-df8ed5666e89.svg'
AUTHOR = 'gpt-6'

class ToriiGate(Solo48):
    icon_id = 'shinto-torii-gate'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/religion"
    aliases = ()
    keywords = ('torii', 'gate', 'shinto', 'japanese', 'shrine', 'entrance')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(name+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        # Centerline box (6,6)-(42,42); shared axis x=24.
        self.add_arc('top',(6,6),(42,6),radius_x=56,sweep=False)
        self.add_polyline('beam',(42,6),(40,16),(33,16),(15,16),(8,16),(6,6))
        self.relate('connect','top','beam')
        self.add_polyline('post-left',(15,16),(13,26),(10,42))
        self.add_polyline('post-right',(33,16),(35,26),(38,42))
        self.add_polyline('crossbar',(6,26),(13,26),(35,26),(42,26))
        for n in ('left','right'):
         self.relate('connect','post-'+n,'beam');self.relate('connect','post-'+n,'crossbar')
