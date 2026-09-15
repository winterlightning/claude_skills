'Llama: smooth muzzle and rump, upright long neck and two broad readable legs.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c296f6df-7f03-557e-90f3-1cb6a7f08661'
SOURCE_PATH = 'pictographic-primitives/animals/lama_c296f6df-7f03-557e-90f3-1cb6a7f08661.svg'
AUTHOR = 'gpt-6'


class Llama(Solo48):
    icon_id = 'llama'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('llama', 'alpaca', 'standing', 'andes', 'animal', 'wool', 'farm', 'south america')

    def build(self):
        # Llama: smooth muzzle and rump, upright long neck and two broad readable legs.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('neck',(16,42),(16,22),(10,22))
        a('snout',(10,22),(6,18),4)
        a('muzzle',(6,18),(10,14),4)
        p('head',(10,14),(20,10),(20,6),(28,6),(30,14),(30,24),(32,24))
        a('rump',(32,24),(42,34),10)
        p('legs',(42,34),(42,42),(34,42),(34,34),(24,34),(24,42),(16,42))
        link('connect','neck','snout')
        link('connect','snout','muzzle')
        link('connect','muzzle','head')
        link('connect','head','rump')
        link('connect','rump','legs')
        link('connect','legs','neck')
