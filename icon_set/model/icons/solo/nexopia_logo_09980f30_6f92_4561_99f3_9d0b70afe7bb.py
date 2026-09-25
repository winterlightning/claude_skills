"""A square frame with a rounded upper right corner holds two tall panels side by side, the right panel with a matching curved top.

Symbol plan: Square with large top-right round and two panel strokes; extremes (6,6)-(42,42).
Review notes: Keeps outer top-right curve and two vertical panel forms. The right inner panel reduces to one stroke to avoid a narrow curved counter. Lucide square informs the outer enclosure.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09980f30-6f92-4561-99f3-9d0b70afe7bb'
SOURCE_PATH = 'pictographic-primitives/logos/nexopia logo_09980f30-6f92-4561-99f3-9d0b70afe7bb.svg'
AUTHOR = 'gpt-6'

class NexopiaLogo(Solo48):
    icon_id = 'nexopia-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('nexopia', 'social', 'letter-n', 'logo', 'brand', 'community', 'panels')

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
        self.add_line('top',(6,6),(24,6));self.add_arc('corner',(24,6),(42,24),radius_x=18)
        self.add_polyline('walls',(42,24),(42,42),(6,42),(6,6))
        self.relate('connect','top','walls-3');self.relate('connect','corner','walls-1');self.relate('connect','top','corner')
        self.add_polyline('left-panel',(14,34),(14,14),(22,14),(22,34),closed=True)
        self.add_line('right-panel',(32,24),(32,34))
