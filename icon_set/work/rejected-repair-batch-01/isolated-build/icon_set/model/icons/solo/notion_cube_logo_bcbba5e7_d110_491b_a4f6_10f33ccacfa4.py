"""An isometric block with a visible top and left face shows a serif capital N on its front face.

Symbol plan: Perspective block with top and left strips and frontal N; extremes (6,6)-(42,42).
Review notes: Preserves block perspective and N; removes the tiny serifs to fit the front face. Earlier Lucide square construction informs the shared face edges; perspective is intentionally asymmetric.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bcbba5e7-d110-491b-a4f6-10f33ccacfa4'
SOURCE_PATH = 'pictographic-primitives/logos/notion logo 1_bcbba5e7-d110-491b-a4f6-10f33ccacfa4.svg'
AUTHOR = 'gpt-6'

class NotionCubeLogo(Solo48):
    icon_id = 'notion-cube-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('notion', 'notes', 'letter-n', 'cube', 'logo', 'brand', 'productivity')

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
        self.add_polyline('outline',(6,6),(34,6),(42,14),(42,42),(14,42),(6,34),closed=True)
        self.add_polyline('front',(6,6),(14,14),(42,14))
        self.add_line('left-edge',(14,14),(14,42))
        for a,bs in [('front-1',['outline-1','outline-6']),('front-2',['outline-2','outline-3']),('left-edge',['front-1','front-2','outline-4','outline-5'])]:
         for b in bs:self.relate('connect',a,b)
        self.add_polyline('n',(23,33),(23,23),(33,33),(33,23))
