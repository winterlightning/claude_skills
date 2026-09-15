"""Tall pillar and curved top flow into the sloping soundboard. Two spaced vertical strings use shared frame junctions, endpoints on the frame. Omit doubled pillar and base trim. Extremes (8,4)-(40,44)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c34bbf3c-dbfc-52d8-9c2d-c0bac391ca8b'
SOURCE_PATH = 'pictographic-primitives/music/harp_c34bbf3c-dbfc-52d8-9c2d-c0bac391ca8b.svg'
AUTHOR = 'gpt-6'

class Harp(Solo48):
    icon_id = 'harp'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/music"
    aliases = ()
    keywords = ('harp', 'string', 'instrument', 'orchestra', 'classical', 'music', 'plucked')

    def build(self):
        self.add_line('pillar',(8,44),(8,4))
        self.add_bezier('neck-a',(8,4), ((12,4),(12,8),(16,8)))
        self.add_bezier('neck-b',(16,8), ((20,8),(24,12),(28,12)))
        self.add_bezier('neck-c',(28,12), ((32,12),(36,12),(40,12)))
        self.add_line('soundboard-a',(40,12),(28,28))
        self.add_line('soundboard-b',(28,28),(16,44))
        self.add_line('base',(16,44),(8,44))
        self.add_contour('frame','pillar','neck-a','neck-b','neck-c','soundboard-a','soundboard-b','base',closed=True)
        self.add_line('string-1',(16,8),(16,44))
        self.add_line('string-2',(28,12),(28,28))
        self.relate('connect','string-1','frame')
        self.relate('connect','string-2','frame')
