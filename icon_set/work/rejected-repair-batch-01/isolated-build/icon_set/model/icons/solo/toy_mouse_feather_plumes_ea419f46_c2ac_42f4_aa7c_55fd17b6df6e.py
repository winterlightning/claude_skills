"""Toy Mouse with Feather Plumes.

Plan: One connected outer silhouette owns two broad rear plumes, pointed ear, round haunch and right-facing snout; one eye.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ea419f46-c2ac-42f4-aa7c-55fd17b6df6e'
SOURCE_PATH = 'pictographic-primitives/pets/cat mouse toy_ea419f46-c2ac-42f4-aa7c-55fd17b6df6e.svg'
AUTHOR = 'gpt-6'

class ToyMouseFeatherPlumes(Solo48):
    icon_id = 'toy-mouse-feather-plumes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('mouse', 'toy', 'cat-toy', 'feathers', 'plush', 'play', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        arc('plume-outer',(6,6),(14,24),8,18,False)
        arc('haunch',(14,24),(14,42),8,9,False)
        line('belly',(14,42),(34,42))
        arc('snout',(34,42),(42,34),8,sweep=False)
        line('nose-slope',(42,34),(34,24))
        line('ear-1',(34,24),(30,18))
        line('ear-2',(30,18),(26,24))
        line('ear-3',(26,24),(20,24))
        arc('plume-right',(20,24),(22,6),12,16,False)
        line('plume-valley-right',(22,6),(14,14))
        arc('plume-valley-left',(14,14),(6,6),12,8,False)
        contour('outline','plume-outer','haunch','belly','snout','nose-slope','ear-1','ear-2','ear-3','plume-right','plume-valley-right','plume-valley-left',closed=True)
        self.add_dot('eye',(29,33))
