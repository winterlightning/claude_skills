'An oval sweet tilts from lower left to upper right, with a flared wrapper end projecting from each narrow end. Both wrapper ends have softly folded, uneven outer edges.\nPlan: Rounded candy center and two diagonally opposed wrapper ends; keep open wrapper pockets. Extrema6,6,42,42.\nConstruction reference: Lucide candy: diagonal sweet and flared wrapper contours; internal decoration omitted.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'daa51e2e-0a6c-43fa-aa42-d53c968856c3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/confectionery_daa51e2e-0a6c-43fa-aa42-d53c968856c3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'oval-twist-wrapped-sweet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('oval', 'twist', 'wrapped', 'sweet')

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

        path('sweet',(26,16),[('C',(31,17),(28,16),(30,16)),('C',(32,22),(32,18),(32,20)),('C',(28,28),(32,24),(30,26)),('C',(22,32),(26,30),(24,32)),('C',(17,31),(20,32),(18,32)),('C',(16,26),(16,30),(16,28)),('C',(20,20),(16,24),(18,22)),('C',(26,16),(22,18),(24,16))],True)
        path('upper-wrapper',(26,16),[('L',(30,6)),('C',(36,8),(30,7),(32,8)),('C',(42,14),(40,8),(42,10)),('L',(32,22))])
        path('lower-wrapper',(16,26),[('L',(6,30)),('C',(8,36),(7,30),(8,32)),('C',(14,42),(8,40),(10,42)),('L',(22,32))]);join('sweet','upper-wrapper');join('sweet','lower-wrapper')
