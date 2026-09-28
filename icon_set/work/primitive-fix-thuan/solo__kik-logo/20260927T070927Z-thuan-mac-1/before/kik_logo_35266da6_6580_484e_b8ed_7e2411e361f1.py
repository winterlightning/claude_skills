"""An oval speech bubble with its tail at the lower right holds a bold lowercase k.

Symbol plan: One bubble outline with lower-right tail; one centered lowercase k with shared junction. Extremes (4,8)-(44,40).
Review notes: Lucide message-circle informs coherent bubble/tail contour. Letter outline reduced to strokes. Tail retains source direction. Tight internal spacing is retained as a blocker if it cannot certify.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '35266da6-6580-484e-b8ed-7e2411e361f1'
SOURCE_PATH = 'pictographic-primitives/logos/kik logo 1_35266da6-6580-484e-b8ed-7e2411e361f1.svg'
AUTHOR = 'gpt-6'

class KikLogo(Solo48):
    icon_id = 'kik-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('kik', 'messenger', 'chat', 'letter-k', 'logo', 'brand', 'speech-bubble')

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
        self.add_arc('bubble-top',(4,22),(44,22),radius_x=20,radius_y=14)
        self.add_arc('bubble-right',(44,22),(40,30),radius_x=10)
        chain('bubble-tail',(40,30),(42,40),(30,36),(18,36))
        self.add_arc('bubble-left',(18,36),(4,22),radius_x=14)
        self.add_contour('bubble','bubble-top','bubble-right','bubble-tail-1','bubble-tail-2','bubble-tail-3','bubble-left',closed=True)

        j=(18,23)
        self.add_line('k-upper',(18,17),j)
        self.add_line('k-lower',j,(18,27))
        self.add_line('k-arm',j,(28,20))
        self.add_line('k-leg',j,(28,27))
        parts=['k-upper','k-lower','k-arm','k-leg']
        for i,a in enumerate(parts):
            for b in parts[i+1:]:self.relate('connect',a,b)
