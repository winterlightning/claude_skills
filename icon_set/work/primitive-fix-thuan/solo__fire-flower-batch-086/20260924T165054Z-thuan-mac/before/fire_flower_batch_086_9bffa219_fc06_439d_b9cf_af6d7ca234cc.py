"""fire-flower: independent batch-086 SOLO48 result.
Plan: Oval head, paired eyes and a central stem. Mirrored pointed open leaves share the bottom stem node.
Reference construction: flower-2.
Reduction: Omitted inner face ring and opened the leaves at their bases to preserve clear eyes and pointed leaf tips.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9bffa219-fc06-439d-b9cf-af6d7ca234cc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-06/mario flower_9bffa219-fc06-439d-b9cf-af6d7ca234cc.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/mario flower_9bffa219-fc06-439d-b9cf-af6d7ca234cc.svg'

class Drawing(Solo48):
    icon_id = 'fire-flower-batch-086'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('fire', 'flower')

    def build(self):
        # Exact envelope comes from Keyshape.VRECT_L.bounds_for(self.profile).

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


        oval('flower',24,15,16,11)
        for x in (20,28): line(f'eye-{x}',(x,14),(x,16))
        line('stem',(24,26),(24,44)); join('flower','stem')
        for side in (-1,1):
            name=f'leaf-{side}'
            path(name,(24+8*side,34),[('L',(24+16*side,34)),('C',(24,44),(24+14*side,42),(24+8*side,44))])
            join(name,'stem')
