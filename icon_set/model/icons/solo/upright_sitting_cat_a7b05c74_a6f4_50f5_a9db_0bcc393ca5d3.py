"""Upright Sitting Cat.

Plan: Upright cat with paired ears, narrow neck, round left haunch and long straight right chest. Asymmetric sitting posture.
Centerline extremes: (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7b05c74-a6f4-50f5-a9db-0bcc393ca5d3'
SOURCE_PATH = 'pictographic-primitives/pets/cat sitting_a7b05c74-a6f4-50f5-a9db-0bcc393ca5d3.svg'
AUTHOR = 'gpt-6'

class UprightSittingCat(Solo48):
    icon_id = 'upright-sitting-cat'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('cat', 'sitting', 'silhouette', 'feline', 'pet', 'upright', 'kitten')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis = 24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('ears',(18,16),(18,4),(26,10),(32,10),(40,4),(40,16))
        line('chest',(40,16),(40,44))
        line('base',(40,44),(16,44))
        arc('haunch',(16,44),(16,28),8)
        line('shoulder',(16,28),(24,22))
        arc('cheek',(24,22),(18,16),6)
        contour('body','chest','base','haunch','shoulder','cheek')
        self.relate('connect','ears','body')
