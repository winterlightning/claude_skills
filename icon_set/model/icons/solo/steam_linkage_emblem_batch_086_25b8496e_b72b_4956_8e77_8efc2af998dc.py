"""steam-linkage-emblem: independent batch-086 SOLO48 result.
Plan: Three circular joints linked by two straight arms; each attachment uses a circle endpoint.
Reference construction: circle.
Reduction: Reduced the double-edged linkage arms to single strokes; retained all three pivots and the dominant upper ring.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '25b8496e-b72b-4956-8e77-8efc2af998dc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-06/logo steam_25b8496e-b72b-4956-8e77-8efc2af998dc.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/logo steam_25b8496e-b72b-4956-8e77-8efc2af998dc.svg'

class Drawing(Solo48):
    icon_id = 'steam-linkage-emblem-batch-086'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('steam', 'linkage', 'emblem')

    def build(self):
        # Exact envelope comes from Keyshape.HRECT_L.bounds_for(self.profile).

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

        path('upper-ring',(28,26),[('A',(24,18),10,10,True),('A',(34,8),10,10,True),('A',(44,18),10,10,True),('A',(34,28),10,10,True),('A',(28,26),10,10,True)],True)
        oval('lower-joint',18,36,4,4)
        oval('left-joint',7,20,3,3)
        line('rising-arm',(22,36),(28,26));join('rising-arm','upper-ring');join('rising-arm','lower-joint')
        line('short-arm',(10,20),(18,32));join('short-arm','left-joint');join('short-arm','lower-joint')
