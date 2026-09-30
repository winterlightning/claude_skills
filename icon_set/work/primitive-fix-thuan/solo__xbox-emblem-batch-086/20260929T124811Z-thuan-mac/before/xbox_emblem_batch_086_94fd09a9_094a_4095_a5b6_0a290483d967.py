"""xbox-emblem: independent batch-086 SOLO48 result.
Plan: Four rounded panels face the shared center around broad diagonal gaps; each panel uses a smooth outer arc and a pointed inner edge.
Reference construction: circle.
Reduction: Rebalanced four panels into rounded sectors while preserving the diagonal cross opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94fd09a9-094a-4095-a5b6-0a290483d967'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-06/logo xbox_94fd09a9-094a-4095-a5b6-0a290483d967.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/logo xbox_94fd09a9-094a-4095-a5b6-0a290483d967.svg'

class Drawing(Solo48):
    icon_id = 'xbox-emblem-batch-086'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('xbox', 'emblem')

    def build(self):
        # Exact envelope comes from Keyshape.SQUARE.bounds_for(self.profile).

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{j}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)


        path('top',(14,8),[('A',(34,8),10,2,True),('L',(24,16)),('L',(14,8))],True)
        path('right',(40,14),[('A',(40,34),2,10,True),('L',(32,24)),('L',(40,14))],True)
        path('bottom',(34,40),[('A',(14,40),10,2,True),('L',(24,32)),('L',(34,40))],True)
        path('left',(8,34),[('A',(8,14),2,10,True),('L',(16,24)),('L',(8,34))],True)
