"""paired-handheld-controllers: independent batch-086 SOLO48 result.
Plan: Paired upright controllers with rounded outer edges, short interrupted inner rails and controls in opposite vertical positions.
Reference construction: gamepad-2.
Reduction: Reduced circular/plus controls to dots and opened each inner rail beside its control to retain legal clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e3096ae-38bf-5339-acc4-1c13cae704e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-07/nintendo switch controller_9e3096ae-38bf-5339-acc4-1c13cae704e7.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/nintendo switch controller_9e3096ae-38bf-5339-acc4-1c13cae704e7.svg'

class Drawing(Solo48):
    icon_id = 'paired-handheld-controllers-batch-086'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    aliases = ()
    keywords = ('paired', 'handheld', 'controllers')

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


        path('left',(20,9),[('L',(20,8)),('L',(12,8)),('A',(4,16),8,8,False),('L',(4,32)),('A',(12,40),8,8,False),('L',(20,40)),('L',(20,27))])
        path('right',(28,21),[('L',(28,8)),('L',(36,8)),('A',(44,16),8,8,True),('L',(44,32)),('A',(36,40),8,8,True),('L',(28,40)),('L',(28,39))])
        dot('left-control',(13,18));dot('right-control',(35,30))
