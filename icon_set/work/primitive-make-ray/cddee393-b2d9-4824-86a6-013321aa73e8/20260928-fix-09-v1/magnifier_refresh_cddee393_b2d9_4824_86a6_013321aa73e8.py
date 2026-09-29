"""Rejected search-refresh has tilted bulky heads and a cramped upper gap. Restore circular counterclockwise arrows and a diagonal magnifier handle.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: refresh-ccw. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'cddee393-b2d9-4824-86a6-013321aa73e8'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__magnifier-refresh/20260928T165531Z-thuan-mac/reference/seo search_cddee393-b2d9-4824-86a6-013321aa73e8.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'magnifier-refresh'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('seo', 'search')
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        path('left',(23,6),[('C',(6,23),(13,6),(6,13)),('C',(10,33),(6,27),(7,30))])
        poly('left-head',(3,31),(10,33),(11,26));join('left','left-head')
        path('right',(21,40),[('C',(33,35),(26,40),(30,38)),('C',(40,23),(37,31),(40,28)),('C',(31,8),(40,17),(36,11))])
        poly('right-head',(32,15),(31,8),(38,10));join('right','right-head')
        line('handle',(33,35),(42,44));join('right','handle')


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

