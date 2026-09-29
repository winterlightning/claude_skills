"""Rejected recycling loop has squeezed elliptical arcs and boxy heads. Restore the circular clockwise two-arrow motif of this reference.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: refresh-ccw. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '04c91a4b-2ad8-4cfb-8848-0a6d8807a4cb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__recycling/20260928T165531Z-thuan-mac/reference/recycling_04c91a4b-2ad8-4cfb-8848-0a6d8807a4cb.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'recycling'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('recycling',)
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        path('upper',(6,23),[('C',(24,6),(7,13),(15,6)),('C',(41,17),(32,6),(39,10))])
        poly('upper-head',(34,16),(41,17),(42,10));join('upper','upper-head')
        path('lower',(42,25),[('C',(24,42),(41,35),(33,42)),('C',(7,31),(16,42),(9,38))])
        poly('lower-head',(6,38),(7,31),(14,32));join('lower','lower-head')


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

