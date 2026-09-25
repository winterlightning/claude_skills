"""fish-facing-left: Horizontally swimming fish with mirrored upper and lower contours, a curved gill seam, and crescent tail.
Lucide construction: fish; original and atomic-debug inspected.
Omissions: Tiny eye omitted as in the original reference.
Keyshape HRECT_M: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '48c88512-d494-4400-aa6e-1031313b1bfb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fishery_48c88512-d494-4400-aa6e-1031313b1bfb.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'fish-facing-left'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('fish', 'facing', 'left')
    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,start,end)
                elif kind=='A': self.add_arc(ident,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,start,(args[0],args[1],end))
                members.append(ident);start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx,cy-ry),[('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True),('A',(cx,cy-ry),rx,ry,True)],True)
        def rect(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('body',(4,24),[('C',(16,10),(8,16),(11,10)),('C',(34,20),(23,10),(29,14)),('L',(44,10)),('C',(40,24),(43,16),(40,21)),('C',(44,38),(40,27),(43,32)),('L',(34,28)),('C',(16,38),(29,34),(23,38)),('C',(4,24),(11,38),(8,32))],True)
        path('gill',(16,10),[('C',(16,38),(25,18),(25,30))]);join('gill','body')
