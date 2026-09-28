"""smiling-tree-trunk: independent batch-086 SOLO48 result.
Plan: Scalloped upper bark, tall trunk and mirrored flared roots form one silhouette; shared eye spacing and curved smile.
Reference construction: tree-deciduous.
Reduction: Reduced cropped branches to the scalloped upper trunk outline; retained eyes, smile and flared roots.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e2497bc-6381-4694-8d17-9da0fe023c2e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-07/mario tree_0e2497bc-6381-4694-8d17-9da0fe023c2e.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/mario tree_0e2497bc-6381-4694-8d17-9da0fe023c2e.svg'

class Drawing(Solo48):
    icon_id = 'smiling-tree-trunk-batch-086'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('smiling', 'tree', 'trunk')

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


        path('trunk',(10,6),[('C',(24,6),(14,12),(20,12)),('C',(38,6),(28,12),(34,12)),('L',(38,34)),('C',(42,42),(38,39),(40,42)),('L',(6,42)),('C',(10,34),(8,42),(10,39)),('L',(10,6))],True)
        for x in (20,28):dot(f'eye-{x}',(x,19))
        path('smile',(20,28),[('A',(28,28),4,3,False)])
