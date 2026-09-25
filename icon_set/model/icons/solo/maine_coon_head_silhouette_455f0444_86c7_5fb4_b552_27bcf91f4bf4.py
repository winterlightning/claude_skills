"""Maine Coon Head Silhouette.

Plan: Tall tufted ear points, flat crown, shaggy cheek notches and widening open neck; mirrored outline without face marks.
Centerline extremes: (6,6)-(42,42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '455f0444-86c7-5fb4-b552-27bcf91f4bf4'
SOURCE_PATH = 'pictographic-primitives/pets/maine coon_455f0444-86c7-5fb4-b552-27bcf91f4bf4.svg'
AUTHOR = 'gpt-6'

class MaineCoonHeadSilhouette(Solo48):
    icon_id = 'maine-coon-head-silhouette'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    aliases = ()
    keywords = ('cat', 'maine-coon', 'head', 'silhouette', 'breed', 'tufted-ears', 'feline')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,rx,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry or rx,sweep=sweep)
        def contour(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        axis=24
        def mirror(p): return (2 * axis - p[0], p[1])
        self.add_polyline('outline',(6,42),(10,32),(8,28),(12,18),(8,6),(18,14),mirror((18,14)),mirror((8,6)),mirror((12,18)),mirror((8,28)),mirror((10,32)),mirror((6,42)))
