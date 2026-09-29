"""Rejected sync-search has blunt right-angle heads and a compressed loop. Restore directional slanted heads, round flow and tangent handle placement.
Symbol plan: coherent paths; repeated parts share parameters; actual attachments share nodes.
Lucide construction reference: refresh-ccw. Source determines semantic arrangement.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'df40480b-5166-4148-8ffb-4e38ec361c58'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__synchronize-arrows-search/20260928T165531Z-thuan-mac/reference/synchronize arrows search_df40480b-5166-4148-8ffb-4e38ec361c58.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    exception = {'reason': 'Keep the round synchronization/search loop, slanted heads and diagonal handle; natural bounds differ from the square keyshape but remain inside the canvas. User explicitly delegated exception decisions for UI/UX quality; reviewed at 48px in light and dark.', 'approved_by': 'user-delegated-gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '1ac170dfb7601e0a14ff53e1211e9fbb5e7d71c532d4fc12cf7957a0cb31a957'}
    icon_id = 'synchronize-arrows-search'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('synchronize', 'arrows', 'search')
    def build(self):
        line=self.add_line;poly=self.add_polyline;path=self.path;circle=self.circle
        join=lambda a,b:self.relate('connect',a,b)

        path('left',(23,6),[('C',(6,23),(13,6),(6,13)),('C',(10,33),(6,27),(7,30))])
        poly('left-head',(4,31),(10,33),(11,26));join('left','left-head')
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

