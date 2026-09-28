"""Circular compass with a broad diagonal needle and four attached cardinal ticks. Mirror needle points about center and omit no identity-bearing parts."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f7c0978-852a-4422-b8c1-411a14d9ac20'
SOURCE_PATH = 'pictographic-primitives/logos/safari logo_8f7c0978-852a-4422-b8c1-411a14d9ac20.svg'
AUTHOR = 'gpt-6'

class SafariLogo(Solo48):
    icon_id = 'safari-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('safari', 'apple', 'browser', 'compass', 'logo', 'brand', 'web')

    def build(self):
        # Plan: Circular compass with a broad diagonal needle and four attached cardinal ticks. Mirror needle points about center and omit no identity-bearing parts.
        # Exact keyshape ink extremes are owned by Keyshape.CIRCLE on SOLO48.

        nodes=[(24,4),(44,24),(24,44),(4,24)]
        for j,p in enumerate(nodes):
            self.add_arc('rim-'+str(j),p,nodes[(j+1)%4],radius_x=20)
            end=(24+(p[0]-24)*4//5,24+(p[1]-24)*4//5)
            self.add_line('tick-'+str(j),p,end)
            self.relate('connect','tick-'+str(j),'rim-'+str(j))
            self.relate('connect','tick-'+str(j),'rim-'+str((j-1)%4))
        self.add_contour('rim',*[f'rim-{j}' for j in range(4)],closed=True)
        self.add_polyline('needle',(32,16),(28,28),(16,32),(20,20),closed=True)
        self.add_line('split',(20,20),(28,28))
        self.relate('connect','needle','split')

