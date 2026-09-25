"""Twin Towers with Connecting Bridge.

Symbol plan: Two mirrored pointed towers joined by a broad bridge. Drop narrow upper tiers and facade ticks.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Lucide building-2: sparse facades and shared building attachments; reference supplies paired spires.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '49935e36-084e-59cc-8f7a-3108d62113bc'
SOURCE_PATH = 'pictographic-primitives/building/modern architecture twin building_49935e36-084e-59cc-8f7a-3108d62113bc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'twin-towers-with-connecting-bridge'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('building', 'architecture', 'structure', 'roof', 'property', 'exterior', 'construction', 'urban')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        for j,x in enumerate((6,30)):
            path('tower-'+str(j),(x,42),(x,34),(x,26),(x,16),(x+6,6),(x+12,16),(x+12,26),(x+12,34),(x+12,42),(x,42),closed=True)
        for j,y in enumerate((26,34)):
            line('bridge-'+str(j),(18,y),(30,y))
            connect('bridge-'+str(j),'tower-0');connect('bridge-'+str(j),'tower-1')
