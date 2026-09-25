"""Three equal rings connected by three open circular sweeps. Preserve the source circle-of-friends topology with actual ring attachment points."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6bb643e-9b0a-4ab3-aa92-a600d496a07c'
SOURCE_PATH = 'pictographic-primitives/logos/ubuntu logo_e6bb643e-9b0a-4ab3-aa92-a600d496a07c.svg'
AUTHOR = 'gpt-6'

class UbuntuLogo(Solo48):
    icon_id = 'ubuntu-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('ubuntu', 'linux', 'operating-system', 'circle-of-friends', 'logo', 'brand', 'open-source')

    def build(self):
        # Plan: Three equal rings connected by three open circular sweeps. Preserve the source circle-of-friends topology with actual ring attachment points.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        for j,(x,y) in enumerate([(12,24),(36,12),(36,36)]):
            ns=[(x,y-6),(x+6,y),(x,y+6),(x-6,y)]
            for k,a in enumerate(ns):self.add_arc(f'node-{j}-{k}',a,ns[(k+1)%4],radius_x=6)
            self.add_contour('node-'+str(j),*[f'node-{j}-{k}' for k in range(4)],closed=True)
        for j,(a,b,r) in enumerate([((12,18),(30,12),20),((36,18),(36,30),12),((30,36),(12,30),20)]):
            self.add_arc('ring-'+str(j),a,b,radius_x=r)
        for j,pair in enumerate([(0,1),(1,2),(2,0)]):
            for k in pair:self.relate('connect','ring-'+str(j),'node-'+str(k))

