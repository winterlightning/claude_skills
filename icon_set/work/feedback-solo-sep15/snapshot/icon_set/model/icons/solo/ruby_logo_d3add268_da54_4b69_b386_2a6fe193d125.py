"""Asymmetric cut gemstone with shared facet junctions. Lucide gem informs explicit crown/pavilion connections; preserve the source tilt."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd3add268-da54-4b69-b386-2a6fe193d125'
SOURCE_PATH = 'pictographic-primitives/logos/ruby logo_d3add268-da54-4b69-b386-2a6fe193d125.svg'
AUTHOR = 'gpt-6'

class RubyLogo(Solo48):
    icon_id = 'ruby-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('ruby', 'gem', 'programming', 'language', 'logo', 'brand', 'diamond')

    def build(self):
        # Plan: Asymmetric cut gemstone with shared facet junctions. Lucide gem informs explicit crown/pavilion connections; preserve the source tilt.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        self.add_polyline('outline',(6,18),(14,8),(32,6),(42,14),(28,42),closed=True)
        center=(26,18)
        for j,p in enumerate([(6,18),(14,8),(32,6),(42,14),(28,42)]):
            self.add_line('facet-'+str(j),p,center)
            self.relate('connect','facet-'+str(j),'outline')
        for a in range(5):
            for b in range(a):self.relate('connect','facet-'+str(a),'facet-'+str(b))

