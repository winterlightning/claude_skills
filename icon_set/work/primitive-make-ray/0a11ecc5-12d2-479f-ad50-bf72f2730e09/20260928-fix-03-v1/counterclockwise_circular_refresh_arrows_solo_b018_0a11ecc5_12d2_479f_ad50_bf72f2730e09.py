"""Rejected arrows form two compressed hooks rather than one circular cycle. Restore matching arcs of one circle and smaller opposing heads.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: refresh-ccw. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0a11ecc5-12d2-479f-ad50-bf72f2730e09'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__counterclockwise-circular-refresh-arrows-solo-b018/20260928T165531Z-thuan-mac/reference/repeat_0a11ecc5-12d2-479f-ad50-bf72f2730e09.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'counterclockwise-circular-refresh-arrows-solo-b018'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('repeat',)
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        path('upper',(39,14),[('C',(24,6),(35,9),(30,6)),('A',(6,24),18,False)])
        poly('upper-head',(2,19),(6,24),(11,20));join('upper','upper-head')
        path('lower',(9,34),[('C',(24,42),(13,39),(18,42)),('A',(42,24),18,False)])
        poly('lower-head',(37,28),(42,24),(46,29));join('lower','lower-head')


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

