"""Cat Scratching Post with Toy.

Plan: Two shelves and broad base on posts; right-hand curved wand with a suspended round ball. Platforms reduced to single strokes.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ce534c44-2117-472a-9638-8e0c72806fa4'
SOURCE_PATH = 'pictographic-primitives/pets/cat scratcher_ce534c44-2117-472a-9638-8e0c72806fa4.svg'
AUTHOR = 'gpt-6'

class CatScratchingPostWithToy(Solo48):
    icon_id = 'cat-scratching-post-with-toy'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('cat-tree', 'scratcher', 'scratching-post', 'cat', 'furniture', 'toy', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('top',(6,6),(14,6),(22,6))
        self.add_polyline('shelf',(6,24),(14,24),(26,24),(32,24))
        self.add_polyline('base',(6,42),(14,42),(26,42),(42,42))
        line('upper-post',(14,6),(14,24))
        for part in ('top','shelf'):self.relate('connect','upper-post',part)
        for i,x in enumerate((14,26)):
         line(f'lower-post-{i}',(x,24),(x,42))
         for part in ('shelf','base'): self.relate('connect',f'lower-post-{i}',part)
        arc('wand',(26,24),(38,6),12,18)
        line('drop',(38,6),(38,14))
        arc('ball-right',(38,14),(38,22),4)
        arc('ball-left',(38,22),(38,14),4)
        contour('ball','ball-right','ball-left',closed=True)
        self.relate('connect','wand','shelf')
        self.relate('connect','wand','drop')
        self.relate('connect','drop','ball')
