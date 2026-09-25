"""Sitting Cat Side View.

Plan: Right-facing cat silhouette with angular ears, straight chest, rounded haunch and separate curled tail attached at rump.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58377584-5a28-47bf-954d-6f0f493ca1fb'
SOURCE_PATH = 'pictographic-primitives/pets/cat_58377584-5a28-47bf-954d-6f0f493ca1fb.svg'
AUTHOR = 'gpt-6'

class SittingCatSideView(Solo48):
    icon_id = 'sitting-cat-side-view'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('cat', 'sitting', 'profile', 'tail', 'feline', 'pet', 'silhouette')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('head',(22,16),(22,6),(30,12),(34,12),(42,6),(42,42),(24,42))
        arc('haunch',(24,42),(24,22),10)
        line('neck',(24,22),(22,16))
        contour('haunch-neck','haunch','neck')
        self.relate('connect','head','haunch-neck')
        arc('tail',(14,32),(6,20),8,12)
        self.relate('connect','tail','haunch-neck')
