"""Sloping sleeves, rounded neckline and mirrored curved leg openings."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8ed514c7-2c36-54a9-8ae4-a874afb8b2f1'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__baby-onesie/20260925T060602Z-thuan-mac/reference/baby care clothes_8ed514c7-2c36-54a9-8ae4-a874afb8b2f1.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'baby-onesie'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('baby care clothes',)

    def build(self):
        # Symbol plan: Sloping sleeves, rounded neckline and mirrored curved leg openings.
        # Construction reference: Lucide shirt; original supplied subject controls meaning.

        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i,c in enumerate(commands):
                kind,end,*args=c
                if kind == 'L' and here==end: continue
                eid=f'{name}-{i}'
                if kind=='L': self.add_line(eid,here,end)
                elif kind=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(eid,here,(args[0],args[1],end))
                ids.append(eid);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('onesie',(18,6),[('A',(30,6),6,6,False),('L',(34,6)),('L',(42,12)),('L',(39,20)),('L',(34,18)),('L',(34,32)),('A',(28,42),10,10,False),('L',(20,42)),('A',(14,32),10,10,False),('L',(14,18)),('L',(9,20)),('L',(6,12)),('L',(14,6)),('L',(18,6))],True)
