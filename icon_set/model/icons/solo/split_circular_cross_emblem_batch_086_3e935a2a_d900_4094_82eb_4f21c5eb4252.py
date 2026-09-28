"""split-circular-cross-emblem: independent batch-086 SOLO48 result.
Plan: Four curved sectors share 10-unit centerline gaps. Unequal left/right column widths preserve the offset cross.
Reference construction: circle.
Reduction: Rebalanced the four curved sectors for open cross gaps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e935a2a-d900-4094-82eb-4f21c5eb4252'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-06/logo smash bros_3e935a2a-d900-4094-82eb-4f21c5eb4252.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/logo smash bros_3e935a2a-d900-4094-82eb-4f21c5eb4252.svg'

class Drawing(Solo48):
    icon_id = 'split-circular-cross-emblem-batch-086'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('split', 'circular', 'cross', 'emblem')

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


        path('upper-left',(17,6),[('A',(6,19),11,13,False),('L',(17,19)),('L',(17,6))],True)
        path('upper-right',(27,6),[('A',(42,19),15,13,True),('L',(27,19)),('L',(27,6))],True)
        path('lower-left',(6,29),[('A',(17,42),11,13,False),('L',(17,29)),('L',(6,29))],True)
        path('lower-right',(42,29),[('A',(27,42),15,13,True),('L',(27,29)),('L',(42,29))],True)
