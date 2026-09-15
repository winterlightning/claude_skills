"""Siberian Husky Face.

Plan: Tall pointed ears and broad cheek-mask outline around a narrow inner face, with eyes and central muzzle reduced.
Centerline extremes: (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a79702ba-8765-4a37-a132-551076abd518'
SOURCE_PATH = 'pictographic-primitives/pets/siberian husky_a79702ba-8765-4a37-a132-551076abd518.svg'
AUTHOR = 'gpt-6'

class SiberianHuskyFace(Solo48):
    icon_id = 'siberian-husky-face'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/pets"
    aliases = ()
    keywords = ('dog', 'husky', 'siberian-husky', 'face', 'breed', 'ears', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('outer-left',(8,36),(12,20),(8,16),(14,4),(18,16),(20,22))
        self.add_polyline('outer-right',mirror((20,22)),mirror((18,16)),mirror((14,4)),mirror((8,16)),mirror((12,20)),mirror((8,36)))
        line('forehead',(18,16),mirror((18,16)))
        self.relate('connect','forehead','outer-left')
        self.relate('connect','forehead','outer-right')
        self.add_polyline('mask',(20,22),(16,28),(8,36),(12,44))
        self.add_polyline('mask-right',mirror((20,22)),mirror((16,28)),mirror((8,36)),mirror((12,44)))
        self.relate('connect','outer-left','mask')
        self.relate('connect','outer-right','mask-right')
        self.add_polyline('nose',(22,34),(24,36),mirror((22,34)))
