"""Rounded square with two rotated interlocking diagonal L marks. Generate the pair by half-turn symmetry and split the rim at every attachment."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7886a695-5c36-499a-8df9-2b9217caa246'
SOURCE_PATH = 'pictographic-primitives/logos/temprano logo_7886a695-5c36-499a-8df9-2b9217caa246.svg'
AUTHOR = 'gpt-6'

class TempranoLogo(Solo48):
    icon_id = 'temprano-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('temprano', 'square', 'diagonal', 'logo', 'brand', 'rounded', 'frame')

    def build(self):
        # Plan: Rounded square with two rotated interlocking diagonal L marks. Generate the pair by half-turn symmetry and split the rim at every attachment.
        # Exact keyshape ink extremes are owned by Keyshape.SQUARE on SOLO48.

        nodes=[(10,6),(30,6),(38,6),(42,10),(42,30),(42,38),(38,42),(18,42),(10,42),(6,38),(6,18),(6,10)]
        corners={2,5,8,11}
        for j,a in enumerate(nodes):
            if j in corners:self.add_arc('rim-'+str(j),a,nodes[(j+1)%12],radius_x=4)
            else:self.add_line('rim-'+str(j),a,nodes[(j+1)%12])
        self.add_contour('rim',*[f'rim-{j}' for j in range(12)],closed=True)
        for j in range(2):
            def p(x,y):return (x,y) if j==0 else (48-x,48-y)
            self.add_polyline('branch-'+str(j),p(6,18),p(12,24),p(18,30))
            self.add_line('diagonal-'+str(j),p(30,6),p(12,24))
            self.relate('connect','branch-'+str(j),'diagonal-'+str(j));self.relate('connect','rim','branch-'+str(j));self.relate('connect','rim','diagonal-'+str(j))

