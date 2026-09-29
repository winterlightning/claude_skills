"""Rejected sync arrows have narrow elliptical arcs and large heads. Rebuild a shared round cycle with equal opposing arrowheads.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: refresh-ccw. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bafc5d96-6820-5892-a08b-927ab58a96ff'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__counterclockwise-synchronize-arrows/20260928T165531Z-thuan-mac/reference/synchronize arrows_bafc5d96-6820-5892-a08b-927ab58a96ff.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'counterclockwise-synchronize-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('synchronize', 'arrows')
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

