"""Fish Toy on String.

Plan: Asymmetric hanging string attaches to fish top; fish body owns pointed tail, simplified eye and no knot.
Keyshape centerline extremes: (6,6)-(42,42)
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d5d2642-d0f9-524e-8717-7df77edf4e9f'
SOURCE_PATH = 'pictographic-primitives/pets/cat fish toy_6d5d2642-d0f9-524e-8717-7df77edf4e9f.svg'
AUTHOR = 'gpt-6'

class FishToyOnString(Solo48):
    icon_id = 'fish-toy-on-string'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('fish', 'toy', 'cat-toy', 'string', 'play', 'pet', 'teaser')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        arc('fish-top',(6,30),(24,18),18,12)
        line('tail-upper',(24,18),(33,25))
        self.add_polyline('tail',(33,25),(42,20),(42,42),(33,35))
        arc('fish-bottom',(33,35),(6,30),18,12)
        self.relate('connect','fish-top','tail-upper')
        self.relate('connect','tail-upper','tail')
        self.relate('connect','tail','fish-bottom')
        self.relate('connect','fish-bottom','fish-top')
        line('string',(24,6),(24,18))
        self.relate('connect','string','fish-top')
        self.relate('connect','string','tail-upper')
        self.add_dot('eye',(18,28))
