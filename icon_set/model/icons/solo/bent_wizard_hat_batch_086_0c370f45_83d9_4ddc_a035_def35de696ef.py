"""bent-wizard-hat: independent batch-086 SOLO48 result.
Plan: One bent pointed crown with shared brim nodes; the right hook is intentionally asymmetric.
Reference construction: hat-glasses.
Reduction: Reduced brim to one closed low band; retained the bent crown without ornamental markings.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c370f45-83d9-4ddc-a035-def35de696ef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-06/magic defense ability_0c370f45-83d9-4ddc-a035-def35de696ef.svg'
AUTHOR = 'gpt-6'
REFERENCE_COPY = 'work/brief-exports/20260918-all-todo-batches-15/batches/batch-086/references/magic defense ability_0c370f45-83d9-4ddc-a035-def35de696ef.svg'

class Drawing(Solo48):
    icon_id = 'bent-wizard-hat-batch-086'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('bent', 'wizard', 'hat')

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


        path('hat',(4,40),[('L',(13,32)),('L',(20,11)),('C',(24,8),(21,8),(22,8)),('C',(32,16),(28,8),(30,12)),('L',(27,16)),('L',(35,32)),('L',(44,40)),('L',(4,40))],True)
        line('band',(13,32),(35,32));join('hat','band')
