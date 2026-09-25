"""A large circle holds a smaller concentric circle, forming a thick ring.

Symbol plan: Two concentric circles, radii20 and10; radial extremes (4,4)-(44,44).
Review notes: Retains the complete concentric ring construction. Earlier Lucide circle informs two coherent semicircles per ring, with ten-unit centerline spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cef8ec87-12b5-43b9-919c-d0169112204b'
SOURCE_PATH = 'pictographic-primitives/logos/orkut logo_cef8ec87-12b5-43b9-919c-d0169112204b.svg'
AUTHOR = 'gpt-6'

class OrkutLogo(Solo48):
    icon_id = 'orkut-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('orkut', 'social', 'ring', 'logo', 'brand', 'google', 'network')

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
        for name,r in [('outer',20),('inner',10)]:ring(name,24,24,r)
