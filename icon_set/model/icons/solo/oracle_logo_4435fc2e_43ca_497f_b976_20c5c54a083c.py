"""A wide rounded capsule outline holds a smaller concentric capsule outline.

Symbol plan: Two concentric horizontal capsules with ten-unit spacing; extremes (4,8)-(44,40).
Review notes: Keeps both nested capsules; exact shared center and ten-unit separation. Earlier Lucide rounded enclosures inform coherent tangent joins.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4435fc2e-43ca-497f-b976-20c5c54a083c'
SOURCE_PATH = 'pictographic-primitives/logos/oracle logo_4435fc2e-43ca-497f-b976-20c5c54a083c.svg'
AUTHOR = 'gpt-6'

class OracleLogo(Solo48):
    icon_id = 'oracle-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('oracle', 'database', 'capsule', 'logo', 'brand', 'enterprise', 'cloud')

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
        rounded('outer',4,8,44,40,16)
        rounded('inner',14,18,34,30,6)
