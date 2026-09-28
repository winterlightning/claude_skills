"""Eight shallow rounded gear lobes encircle a monoline R. Shared polar series owns every lobe; reduce small teeth and thick double letter outlines."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c083083-7bb0-4121-abdf-2375e1c6da04'
SOURCE_PATH = 'pictographic-primitives/logos/rust logo_5c083083-7bb0-4121-abdf-2375e1c6da04.svg'
AUTHOR = 'gpt-6'

class RustLogo(Solo48):
    icon_id = 'rust-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('rust', 'programming', 'language', 'gear', 'logo', 'brand', 'developer')

    def build(self):
        # Plan: Eight shallow rounded gear lobes encircle a monoline R. Shared polar series owns every lobe; reduce small teeth and thick double letter outlines.
        # Exact keyshape ink extremes are owned by Keyshape.CIRCLE on SOLO48.

        import math
        points=[]
        for j in range(16):
            a=-math.pi/2+j*math.pi/8;r=20 if j%2==0 else 17
            points.append((round(24+r*math.cos(a)),round(24+r*math.sin(a))))
        members=[]
        for j,p in enumerate(points):
            k=(j+1)%16;q=points[k];a=-math.pi/2+j*math.pi/8;b=a+math.pi/8
            c1=(p[0]-2*math.sin(a),p[1]+2*math.cos(a));c2=(q[0]+2*math.sin(b),q[1]-2*math.cos(b))
            name='tooth-'+str(j);members.append(name);self.add_bezier(name,p,(c1,c2,q))
        self.add_contour('gear',*members,closed=True)
        self.add_polyline('stem',(20,17),(20,25),(20,31))
        self.add_arc('bowl',(20,17),(20,25),radius_x=8,radius_y=4)
        self.add_line('leg',(20,25),(28,31))
        for a,b in [('stem','bowl'),('stem','leg'),('bowl','leg')]:self.relate('connect',a,b)

