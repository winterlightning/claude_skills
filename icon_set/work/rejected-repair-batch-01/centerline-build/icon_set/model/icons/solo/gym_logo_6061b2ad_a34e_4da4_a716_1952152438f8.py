"""A large circle holds a smaller ring divided into four segments by short diagonal spokes, with an open horseshoe arc at its centre.

Plan: Two concentric rings at radii 20 and 11, joined by four cardinal spokes.
Keyshape: CIRCLE; exact SOLO48 envelope from the contract.
Construction reference: No useful exact brand match; concentric cardinal arc construction.
Simplification: Tiny central horseshoe omitted; spokes reoriented to cardinal nodes for exact joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6061b2ad-a34e-4da4-a716-1952152438f8'
SOURCE_PATH = 'pictographic-primitives/logos/gym logo_6061b2ad-a34e-4da4-a716-1952152438f8.svg'
AUTHOR = 'gpt-6'


class GymLogo(Solo48):
    icon_id = 'gym-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('gym', 'circle', 'target', 'logo', 'brand', 'rings', 'reinforcement-learning')

    def build(self):
        for name,r in [('outer',20),('inner',11)]:
            points=[(24,24-r),(24+r,24),(24,24+r),(24-r,24)]
            for i,(a,b) in enumerate(zip(points,points[1:]+points[:1])):
                self.add_arc(f'{name}-{i}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{i}' for i in range(4)),closed=True)
        for i,(dx,dy) in enumerate(((0,-1),(1,0),(0,1),(-1,0))):
            self.add_line(f'spoke-{i}',(24+11*dx,24+11*dy),(24+20*dx,24+20*dy))
            self.relate('connect','outer',f'spoke-{i}')
            self.relate('connect','inner',f'spoke-{i}')
