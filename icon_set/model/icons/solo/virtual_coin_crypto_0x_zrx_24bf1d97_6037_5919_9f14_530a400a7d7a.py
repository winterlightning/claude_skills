"""An outlined X on a coin with exposed diagonal slash ends.
Symbol plan and construction: circle: a continuous ring; supplied reference owns the outlined X.
Keyshape: CIRCLE preserves the coin radius and provides a consistent ring.
Omissions: None; X arms shortened and widened.
Review: The outlined X has deeper visible notches and enough space to the ring. Slash endpoints use exact radius20 nodes (12,40) and (36,8), with shared X nodes (18,32) and (30,16), on one diagonal."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '24bf1d97-6037-5919-9f14-530a400a7d7a'
SOURCE_PATH = 'pictographic-primitives/finance/virtual coin crypto 0x zrx_24bf1d97-6037-5919-9f14-530a400a7d7a.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'virtual-coin-crypto-0x-zrx'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'finance'
    categories = ('primitives', 'finance')
    aliases = ()
    keywords = ('virtual', 'coin', 'crypto', '0x', 'zrx')







    def build(self):
        # Coin circle split at exact 3-4-5 radial nodes for the two exposed slash ends.
        ring=[(24,4),(36,8),(44,24),(24,44),(12,40),(4,24),(24,4)]
        for j,(a,b) in enumerate(zip(ring,ring[1:])):
            self.add_arc('coin-'+str(j),a,b,radius_x=20)
        self.add_contour('coin',*('coin-'+str(j) for j in range(6)),closed=True)
        self.add_polyline('x-outline',(21,13),(24,18),(27,13),(30,16),(35,21),(30,24),(35,27),(27,35),(24,30),(21,35),(18,32),(13,27),(18,24),(13,21),closed=True)
        self.add_line('slash-low',(12,40),(18,32))
        self.add_line('slash-high',(30,16),(36,8))
        for n in ['slash-low','slash-high']:
            self.relate('connect',n,'coin');self.relate('connect',n,'x-outline')
