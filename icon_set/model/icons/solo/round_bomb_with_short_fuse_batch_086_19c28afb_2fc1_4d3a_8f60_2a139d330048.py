"""round-bomb-with-short-fuse: independent batch-086 SOLO48 result.
Plan: Circular bomb body with a shared upper-right fuse attachment and detached spark.
Reference construction: bomb.
Reduction: Reduced neck and fuse base to a single fuse attachment; retained the spherical body and lit spark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19c28afb-2fc1-4d3a-8f60-2a139d330048'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-06/mario bomb_19c28afb-2fc1-4d3a-8f60-2a139d330048.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/mario bomb_19c28afb-2fc1-4d3a-8f60-2a139d330048.svg'

class Drawing(Solo48):
    icon_id = 'round-bomb-with-short-fuse-batch-086'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('round', 'bomb', 'with', 'short', 'fuse')

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


        path('body',(30,15),[('A',(36,27),15,15,True),('A',(21,42),15,15,True),('A',(6,27),15,15,True),('A',(21,12),15,15,True),('A',(30,15),15,15,True)],True)
        path('fuse',(30,15),[('L',(36,9)),('L',(42,6))]);join('body','fuse')
        line('spark',(42,16),(42,17))
