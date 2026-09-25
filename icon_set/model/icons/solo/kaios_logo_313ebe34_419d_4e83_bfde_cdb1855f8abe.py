"""An outlined capital K made of a tall rounded stem and two diagonal rounded bars meeting near its middle.

Symbol plan: Independent tall capsule and a right-facing pair of diagonal arms. Centerline extremes (8,4)-(40,44).
Review notes: The stem keeps its capsule; diagonal bars reduce to a coherent centerline chevron to open the gap. Lucide square supplies tangent rounded corners. Directional asymmetry belongs to K.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '313ebe34-419d-4e83-bfde-cdb1855f8abe'
SOURCE_PATH = 'pictographic-primitives/logos/kai os logo_313ebe34-419d-4e83-bfde-cdb1855f8abe.svg'
AUTHOR = 'gpt-6'

class KaiosLogo(Solo48):
    icon_id = 'kaios-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('kaios', 'mobile', 'letter-k', 'operating-system', 'logo', 'brand', 'feature-phone')

    def build(self):

        def chain(name, *points):
            for i,(start,end) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{i}',start,end)
        def ring(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def rounded(name, left, top, right, bottom, r):
            points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for i,start in enumerate(points):
                end=points[(i+1)%8]; ident=f'{name}-{i}'
                if start==end: continue
                if i%2:self.add_arc(ident,start,end,radius_x=r)
                else:self.add_line(ident,start,end)
                members.append(ident)
            self.add_contour(name,*members,closed=True)
        rounded('stem',8,4,16,44,4)
        self.add_polyline('arms',(40,4),(26,24),(40,44))
