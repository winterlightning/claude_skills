"""all-might-head: independent batch-086 SOLO48 result.
Plan: Broad rounded jaw under two mirrored swept curved hair points. Shared eye spacing; head only.
Reference construction: human_ref/user.svg.
Reduction: Omitted tiny ears, side locks, mouth and crossing seam; retained broad face and exaggerated swept hair.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb435dbc-a51b-4359-a39d-23ed29b0bbb3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-07/my hero acadiamia allmight_bb435dbc-a51b-4359-a39d-23ed29b0bbb3.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/my hero acadiamia allmight_bb435dbc-a51b-4359-a39d-23ed29b0bbb3.svg'

class Drawing(Solo48):
    icon_id = 'all-might-head-batch-086'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('all', 'might', 'head')

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


        path('head',(10,4),[('C',(24,22),(10,16),(16,22)),('C',(38,4),(32,22),(38,16)),('L',(40,24)),('L',(40,32)),('A',(28,44),12,12,True),('L',(20,44)),('A',(8,32),12,12,True),('L',(8,24)),('L',(10,4))],True)
        for x in (20,28):dot(f'eye-{x}',(x,31))
