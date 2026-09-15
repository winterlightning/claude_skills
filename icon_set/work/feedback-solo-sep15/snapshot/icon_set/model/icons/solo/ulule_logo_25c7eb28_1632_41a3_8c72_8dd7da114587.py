"""Large paired owl eyes with pupils, a curved forehead and a descending beak. Retain the identifying ringed eyes; omit the lower head enclosure and small ear tufts to provide space."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25c7eb28-1632-41a3-8c72-8dd7da114587'
SOURCE_PATH = 'pictographic-primitives/logos/ulule logo_25c7eb28-1632-41a3-8c72-8dd7da114587.svg'
AUTHOR = 'gpt-6'

class UluleLogo(Solo48):
    icon_id = 'ulule-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('ulule', 'crowdfunding', 'owl', 'logo', 'brand', 'campaign', 'eyes')

    def build(self):
        # Plan: Large paired owl eyes with pupils, a curved forehead and a descending beak. Retain the identifying ringed eyes; omit the lower head enclosure and small ear tufts to provide space.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        for j,x in enumerate((15,33)):
            ns=[(x,19),(x+9,28),(x,37),(x-9,28)]
            for k,a in enumerate(ns):self.add_arc(f'eye-{j}-{k}',a,ns[(k+1)%4],radius_x=9)
            self.add_contour('eye-'+str(j),*[f'eye-{j}-{k}' for k in range(4)],closed=True)
            self.add_dot('pupil-'+str(j),(x,28))
        self.relate('connect','eye-0','eye-1')
        self.add_bezier('forehead',(15,19),((15,12),(18,6),(24,6)),((30,6),(33,12),(33,19)))
        self.add_line('beak',(24,28),(24,42))
        for n in ('forehead','beak'):
            for j in range(2):self.relate('connect',n,'eye-'+str(j))

