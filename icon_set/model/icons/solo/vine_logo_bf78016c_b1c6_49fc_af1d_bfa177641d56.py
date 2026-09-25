"""Five ring buds on one branching upright. Share bud radius and two branch levels; omit the small nested center dots."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf78016c-b1c6-49fc-af1d-bfa177641d56'
SOURCE_PATH = 'pictographic-primitives/logos/vine logo_bf78016c-b1c6-49fc-af1d-bfa177641d56.svg'
AUTHOR = 'gpt-6'

class VineLogo(Solo48):
    icon_id = 'vine-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    aliases = ()
    keywords = ('vine', 'video', 'branch', 'social', 'logo', 'brand', 'plant')

    def build(self):
        # Plan: Five ring buds on one branching upright. Share bud radius and two branch levels; omit the small nested center dots.
        # Exact keyshape ink extremes are owned by Keyshape.VRECT_L on SOLO48.

        self.add_polyline('stem',(24,10),(24,24),(24,39),(24,44))
        nodes=[(24,7,(24,10),(24,10)),(11,19,(14,19),(24,24)),(37,16,(34,16),(24,24)),(11,34,(14,34),(24,39)),(37,31,(34,31),(24,39))]
        for j,(x,y,a,b) in enumerate(nodes):
            c=(2*x-a[0],2*y-a[1]);self.add_arc(f'bud-{j}-a',a,c,radius_x=3);self.add_arc(f'bud-{j}-b',c,a,radius_x=3);self.add_contour('bud-'+str(j),f'bud-{j}-a',f'bud-{j}-b',closed=True)
            if j:
                self.add_line('twig-'+str(j),a,b);self.relate('connect','bud-'+str(j),'twig-'+str(j));self.relate('connect','twig-'+str(j),'stem')
            else:self.relate('connect','bud-0','stem')
        self.relate('connect','twig-1','twig-2');self.relate('connect','twig-3','twig-4')

