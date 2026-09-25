"""Pet Nail Clipper.

Plan: Open U-shaped cutting jaws meet at a shared pivot above two splayed handles; simplify handle thickness.
Centerline extremes: (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'badbf8b0-7dfa-4711-867a-c97defe4ad42'
SOURCE_PATH = 'pictographic-primitives/pets/pets nail clipper_badbf8b0-7dfa-4711-867a-c97defe4ad42.svg'
AUTHOR = 'gpt-6'

class PetNailClipper(Solo48):
    icon_id = 'pet-nail-clipper'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('nail-clipper', 'clipper', 'grooming', 'claws', 'trim', 'pet', 'tool')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        line('jaw-left-tip',(18,4),(14,4))
        arc('jaw-left',(14,4),(24,22),10,18,False)
        arc('jaw-right',(24,22),mirror((14,4)),10,18,False)
        line('jaw-right-tip',mirror((14,4)),mirror((18,4)))
        contour('jaws','jaw-left-tip','jaw-left','jaw-right','jaw-right-tip')
        line('handle-left',(24,22),(8,44))
        line('handle-right',(24,22),mirror((8,44)))
        self.relate('connect','jaws','handle-left')
        self.relate('connect','jaws','handle-right')
        self.relate('connect','handle-left','handle-right')
