"""medusa-head-with-snake-hair: independent batch-086 SOLO48 result.
Plan: Circular lower jaw and two mirrored curling snake locks form one continuous open outline; shared eyes retain the frontal portrait.
Reference construction: human_ref/user.svg.
Reduction: Reduced many small snake locks to two prominent curled snakes; omitted tiny brows and angular nose.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '153226c0-7d54-42d8-8fa9-2caf44b880cf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-07/meduza gorgon_153226c0-7d54-42d8-8fa9-2caf44b880cf.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/meduza gorgon_153226c0-7d54-42d8-8fa9-2caf44b880cf.svg'

class Drawing(Solo48):
    icon_id = 'medusa-head-with-snake-hair-batch-086'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('medusa', 'head', 'with', 'snake', 'hair')

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


        path('snake-hair-and-jaw',(8,10),[('L',(8,4)),('L',(12,4)),('A',(18,10),6,6,True),('L',(18,14)),('A',(10,22),8,8,True),('L',(10,30)),('A',(24,44),14,14,False),('A',(38,30),14,14,False),('L',(38,22)),('A',(30,14),8,8,True),('L',(30,10)),('A',(36,4),6,6,True),('L',(40,4)),('L',(40,10))])
        for x in (20,28):dot(f'eye-{x}',(x,28))
        dot('mouth',(24,35))
