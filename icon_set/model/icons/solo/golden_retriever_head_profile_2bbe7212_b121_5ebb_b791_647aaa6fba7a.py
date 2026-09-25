"""Golden Retriever Head Profile.

Plan: Rounded right-facing skull, long floppy ear, projecting snout and open curved neck. Ear is part of head outline.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2bbe7212-b121-5ebb-b791-647aaa6fba7a'
SOURCE_PATH = 'pictographic-primitives/pets/golden retriever_2bbe7212-b121-5ebb-b791-647aaa6fba7a.svg'
AUTHOR = 'gpt-6'

class GoldenRetrieverHeadProfile(Solo48):
    icon_id = 'golden-retriever-head-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('dog', 'golden-retriever', 'retriever', 'head', 'profile', 'breed', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        arc('crown',(6,24),(24,6),18)
        arc('forehead',(24,6),(34,16),10)
        line('snout-top',(34,16),(42,18))
        arc('snout',(42,18),(30,30),12)
        arc('throat',(30,30),(28,42),2,12,False)
        contour('head','crown','forehead','snout-top','snout','throat')
        arc('ear',(6,24),(18,30),12,6,False)
        line('ear-inner',(18,30),(18,14))
        contour('flop','ear','ear-inner')
        self.relate('connect','head','flop')
        line('neck',(6,42),(6,24))
        self.relate('connect','neck','flop')
        self.relate('connect','neck','head')
