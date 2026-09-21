'A broad rounded travel bag has a large arched handle extending above its top. Two vertical lines continue from the handle down the front, joined by a horizontal seam across the central band.\nPlan: Round travel case with handle and two front bands; uncluttered central band.\nConstruction reference: Lucide briefcase original and atomic-debug: rounded case and attached handle.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e637c1f-743b-4604-87bf-b398f819673f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/overnighter_2e637c1f-743b-4604-87bf-b398f819673f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-travel-bag-band'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('rounded', 'travel', 'bag', 'band')

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

        path('bag',(12,20),[('L',(16,20)),('L',(32,20)),('L',(36,20)),('A',(44,28),8,8,True),('L',(44,32)),('A',(36,40),8,8,True),('L',(32,40)),('L',(16,40)),('L',(12,40)),('A',(4,32),8,8,True),('L',(4,28)),('A',(12,20),8,8,True)],True)
        path('handle',(16,20),[('L',(16,12)),('A',(20,8),4,4,True),('L',(28,8)),('A',(32,12),4,4,True),('L',(32,20))]);join('handle','bag')
        line('band1',(16,20),(16,40));line('band2',(32,20),(32,40));join('band1','bag');join('band2','bag');join('band1','handle');join('band2','handle')
