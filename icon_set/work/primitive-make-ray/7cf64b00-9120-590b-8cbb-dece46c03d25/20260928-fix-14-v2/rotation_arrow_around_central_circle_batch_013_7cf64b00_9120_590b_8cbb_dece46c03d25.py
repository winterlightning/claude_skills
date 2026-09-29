"""Rejected central orbit is oval, with an overly small center ring. Restore a concentric circle inside a round three-quarter arrow.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: rotate-ccw. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7cf64b00-9120-590b-8cbb-dece46c03d25'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rotation-arrow-around-central-circle-batch-013/20260928T165531Z-thuan-mac/reference/synchronize arrow 2_7cf64b00-9120-590b-8cbb-dece46c03d25.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'rotation-arrow-around-central-circle-batch-013'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('synchronize', 'arrow', '2')
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        path('orbit',(24,42),[('A',(42,24),18,False),('A',(24,6),18,False),('A',(6,24),18,False)])
        poly('head',(2,19),(6,24),(11,20));join('head','orbit')
        circle('hub',24,24,5)


    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)

