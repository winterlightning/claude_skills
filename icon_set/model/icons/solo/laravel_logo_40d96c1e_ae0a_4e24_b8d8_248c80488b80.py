"""An isometric line construction of blocks forms an L: a tall column at the left joined by a slanted bar to a small cube at the right.

Symbol plan: Isometric L column and right cube sharing explicit nodes. Extremes (6,6)-(42,42).
Review notes: Lucide box informs isometric edge graph with real shared vertices. Reduces duplicate outline but keeps column and cube; shallow faces need spacing review.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '40d96c1e-ae0a-4e24-b8d8-248c80488b80'
SOURCE_PATH = 'pictographic-primitives/logos/laravel logo_40d96c1e-ae0a-4e24-b8d8-248c80488b80.svg'
AUTHOR = 'gpt-6'

class LaravelLogo(Solo48):
    icon_id = 'laravel-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('laravel', 'php', 'framework', 'cubes', 'logo', 'brand', 'developer')

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
        points={'a':(6,12),'b':(16,6),'c':(26,12),'d':(16,18),'e':(6,34),'f':(16,42),'g':(16,32),'h':(32,24),'i':(42,30),'j':(32,36),'k':(42,18),'l':(32,12),'m':(32,24),'n':(42,30)}
        edges=[('a','b'),('b','c'),('c','d'),('d','a'),('a','e'),('e','f'),('f','g'),('g','d'),('g','h'),('h','i'),('i','j'),('j','f'),('c','h'),('h','l'),('l','k'),('k','i')]
        for a,b in edges:self.add_line(a+b,points[a],points[b])
        for idx,(a,b) in enumerate(edges):
            for c,d in edges[idx+1:]:
                if set((a,b)) & set((c,d)):self.relate('connect',a+b,c+d)
