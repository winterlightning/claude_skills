"""rounded-game-tree-on-base: independent batch-086 SOLO48 result.
Plan: Three-lobed tree crown, central trunk and wide base; crown underside splits at trunk node.
Reference construction: tree-deciduous.
Reduction: Kept the three lobes, trunk and rectangular base; omitted surface details.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '784cc911-c4cd-5476-a0e6-e851b7b852e0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-06/mario cloud_784cc911-c4cd-5476-a0e6-e851b7b852e0.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/mario cloud_784cc911-c4cd-5476-a0e6-e851b7b852e0.svg'

class Drawing(Solo48):
    icon_id = 'rounded-game-tree-on-base-batch-086'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('rounded', 'game', 'tree', 'on', 'base')

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


        path('canopy',(14,16),[('A',(24,6),10,10,True),('A',(34,16),10,10,True),('A',(34,26),8,5,True),('L',(24,26)),('L',(14,26)),('A',(14,16),8,5,True)],True)
        line('trunk',(24,26),(24,34));join('trunk','canopy')
        path('base',(24,34),[('L',(42,34)),('L',(42,42)),('L',(6,42)),('L',(6,34)),('L',(24,34))],True);join('trunk','base')
