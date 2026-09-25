"""The lowercase wordmark max in rounded geometric letters.

Symbol plan: Diagonal max wordmark drawn directly on integer nodes; shared 45-degree baseline. Extremes (6,6)-(42,42).
Review notes: The horizontal attempt crowded the m/a and a/x gaps. This separately constructed diagonal layout opens those gaps while retaining max. The m central leg is omitted and the x is narrow. Intentional 45-degree rotation follows the skill fit-repair ladder; no other family is scaled.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '01b975f9-a58c-49ce-b9fc-e0416bd47480'
SOURCE_PATH = 'pictographic-primitives/logos/max logo_01b975f9-a58c-49ce-b9fc-e0416bd47480.svg'
AUTHOR = 'gpt-6'

class MaxLogo(Solo48):
    icon_id = 'max-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('max', 'hbo-max', 'streaming', 'wordmark', 'logo', 'brand', 'tv')

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
        def p(x,y):return (6+x+y,36-x+y)
        # The m keeps two humps and two outer stems; omit its short central leg.
        self.add_line('m-upper',p(0,0),p(0,2))
        self.add_line('m-left',p(0,2),p(0,6))
        self.add_bezier('m-humps',p(0,2),(p(0,0),p(5,0),p(5,2)),(p(5,0),p(10,0),p(10,2)))
        self.add_line('m-right',p(10,2),p(10,6))
        self.add_contour('m-shoulder','m-humps','m-right')
        for a,b in [('m-upper','m-left'),('m-upper','m-humps'),('m-left','m-humps')]:self.relate('connect',a,b)
        self.add_bezier('a-bowl',p(22,3),(p(22,1),p(21,0),p(19,0)),(p(17,0),p(16,1),p(16,3)),(p(16,5),p(17,6),p(19,6)),(p(21,6),p(22,5),p(22,3)))
        self.add_contour('a','a-bowl',closed=True)
        self.add_line('a-upper',p(22,0),p(22,3));self.add_line('a-lower',p(22,3),p(22,6))
        self.add_contour('a-stem','a-upper','a-lower')
        for member in ['a-upper','a-lower']:self.relate('connect',member,'a-bowl')
        j=p(29,3)
        for name,start,end in [('x-ul',p(28,0),j),('x-lr',j,p(30,6)),('x-ll',p(28,6),j),('x-ur',j,p(30,0))]:self.add_line(name,start,end)
        parts=['x-ul','x-lr','x-ll','x-ur']
        for i,a in enumerate(parts):
            for b in parts[i+1:]:self.relate('connect',a,b)
