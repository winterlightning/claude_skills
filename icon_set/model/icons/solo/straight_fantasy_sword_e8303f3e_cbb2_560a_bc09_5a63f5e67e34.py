'A broad straight sword points diagonally toward the upper-right and ends in an angular tapered tip. A plain rectangular crossguard crosses the blade above a short rectangular grip.\nPlan: Diagonal broad blade, rectangular crossguard and grip share seam endpoints. Extrema6,6,42,42.\nConstruction reference: Lucide sword: diagonal blade, guard and grip; source rectangular crossguard retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e8303f3e-cbb2-560a-bc09-5a63f5e67e34'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/video-games/batch-12/video game sword_e8303f3e-cbb2-560a-bc09-5a63f5e67e34.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'straight-fantasy-sword'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video-games'
    categories = ('primitives', 'video-games')
    aliases = ()
    keywords = ('straight', 'fantasy', 'sword')

    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L':self.add_line(member,here,end)
                elif kind=='A':self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C':self.add_bezier(member,here,(args[0],args[1],end))
                here=end;members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b):self.add_line(name,a,b)
        def poly(name,*points):self.add_polyline(name,*points,closed=points[0]==points[-1])
        def join(a,b):self.relate('connect',a,b)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        def oval(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

        poly('guard',(36,30),(30,36),(24,30),(18,24),(12,18),(18,12),(24,18),(30,24),(36,30))
        poly('blade',(24,18),(36,6),(42,6),(42,12),(30,24));poly('grip',(24,30),(12,42),(6,36),(18,24));join('blade','guard');join('grip','guard')
