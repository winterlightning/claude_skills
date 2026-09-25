"""A large central circle holding a smaller ring and dot is joined by short links to a small ring on each side, in a horizontal row.

Symbol plan: Central ring with two side rings and two shared horizontal links. Radial centerline extreme 20 at the side rings.
Review notes: Retains the central and side rings; source has no central dot in its actual render. Lucide circle supplies ring construction. Circular keyshape admits the wide three-ring arrangement without distorting the central circle.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a32ba714-8a6d-4316-ac59-2187c28f1af2'
SOURCE_PATH = 'pictographic-primitives/logos/lineageos logo_a32ba714-8a6d-4316-ac59-2187c28f1af2.svg'
AUTHOR = 'gpt-6'

class LineageosLogo(Solo48):
    icon_id = 'lineageos-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('lineageos', 'android', 'operating-system', 'logo', 'brand', 'open-source', 'rom')

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
        # Central circle and side rings preserve the horizontal source proportions.
        self.add_arc('main-upper',(13,24),(35,24),radius_x=11)
        self.add_arc('main-lower',(35,24),(13,24),radius_x=11)
        self.add_contour('main','main-upper','main-lower',closed=True)
        for side,x,edge in [('left',7,13),('right',41,35)]:
            ring(side,x,24,3)
            start=(x+3,24) if side=='left' else (x-3,24)
            self.add_line(side+'-link',start,(edge,24))
            for part in ['top','bottom']:self.relate('connect',side+'-link',side+'-'+part)
            for part in ['upper','lower']:self.relate('connect',side+'-link','main-'+part)
        ring('core',24,24,2)
