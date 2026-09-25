"""Sniffing Dog Line Drawing.

Plan: Sparse continuous dog gesture: angular upper-left head, long neck, curved chest and upward sweeping tail. Preserve the unusual reference rather than invent fine anatomy.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd062882b-c4f5-520d-aa54-de42ac8fa8b1'
SOURCE_PATH = 'pictographic-primitives/pets/dog snifting smelling_d062882b-c4f5-520d-aa54-de42ac8fa8b1.svg'
AUTHOR = 'gpt-6'

class SniffingDogLine(Solo48):
    icon_id = 'sniffing-dog-line'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'sniffing', 'smelling', 'nose', 'line-art', 'pet', 'scent')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        self.add_polyline('head',(22,12),(26,6),(14,6),(6,12),(16,18),(14,28))
        arc('chest',(14,28),(24,42),10,14,False)
        arc('tail-root',(24,42),(34,32),10,sweep=False)
        line('tail',(34,32),(38,22))
        line('tail-tip',(38,22),(42,22))
        self.relate('connect','head','chest')
        contour('lower','chest','tail-root','tail','tail-tip')
