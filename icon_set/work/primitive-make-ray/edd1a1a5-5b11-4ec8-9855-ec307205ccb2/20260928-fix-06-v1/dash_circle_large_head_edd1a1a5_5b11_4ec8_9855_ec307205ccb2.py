"""Rejected return loop is flattened and the large head collides visually with its curve. Restore a round clockwise loop and distinct upper-left break.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: rotate-ccw. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'edd1a1a5-5b11-4ec8-9855-ec307205ccb2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dash-circle-large-head/20260928T165531Z-thuan-mac/reference/dash circle large head_edd1a1a5-5b11-4ec8-9855-ec307205ccb2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'dash-circle-large-head'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('dash', 'circle', 'large', 'head')
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        path('orbit',(6,20),[('C',(24,6),(8,11),(15,6)),('A',(42,24),18,True),('A',(24,42),18,True),('C',(7,27),(14,42),(7,36))])
        poly('head',(2,33),(7,27),(13,33));join('orbit','head')


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

