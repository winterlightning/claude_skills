"""Great Dane Head.

Plan: Tall pointed cropped ears, long narrow cheek planes and squared muzzle split at base; mirrored silhouette.
Centerline extremes: (8,4)-(40,44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '71bbd30b-775c-5a19-a228-ee3626bdd438'
SOURCE_PATH = 'pictographic-primitives/pets/great dane_71bbd30b-775c-5a19-a228-ee3626bdd438.svg'
AUTHOR = 'gpt-6'

class GreatDaneHead(Solo48):
    icon_id = 'great-dane-head'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('dog', 'great-dane', 'head', 'breed', 'ears', 'large-dog', 'pet')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('outline',(8,22),(8,4),(18,16),mirror((18,16)),mirror((8,4)),mirror((8,22)),mirror((16,30)),mirror((16,44)),(16,44),(16,30),(8,22))
        line('muzzle',(24,34),(24,44))
        self.relate('connect','muzzle','outline')
