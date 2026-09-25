"""paired-rounded-emblem-bars: independent batch-086 SOLO48 result.
Plan: Two mirrored rounded bars with shared 6-unit cap radii, 10-unit centerline separation, and lower outer tapers.
Reference construction: none.
Reduction: Broadened the bar pair to SQUARE for clear tapered interiors.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6648abc5-9be3-43ac-8410-e09f3b1608b4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-06/logo starcraft_6648abc5-9be3-43ac-8410-e09f3b1608b4.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/logo starcraft_6648abc5-9be3-43ac-8410-e09f3b1608b4.svg'

class Drawing(Solo48):
    icon_id = 'paired-rounded-emblem-bars-batch-086'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('paired', 'rounded', 'emblem', 'bars')

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


        for side in (-1,1):
            def p(x,y):return (24+side*x,y)
            path(f'bar-{side}',p(5,12),[('A',p(11,6),6,6,side>0),('L',p(12,6)),('A',p(18,12),6,6,side>0),('L',p(18,30)),('L',p(13,40)),('C',p(9,42),p(12,42),p(11,42)),('C',p(5,38),p(7,42),p(5,40)),('L',p(5,12))],True)
