'A domed patio umbrella has curved panel seams above a long central pole. A short tabletop crosses the pole below the canopy, with two simple stools positioned on either side.\nPlan: Domed umbrella above table and two stools. All furniture retained, canopy panel seams removed. Bilateral construction.\nConstruction reference: umbrella: dome and straight underside; source furniture remains.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6edc1ccb-99fb-4eb2-81b0-8a6de2975288'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/patio_6edc1ccb-99fb-4eb2-81b0-8a6de2975288.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'patio-umbrella-table-stools'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('patio', 'umbrella', 'table', 'stools')

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

        path('canopy',(6,20),[('A',(42,20),18,14,True),('L',(24,20)),('L',(6,20))],True)
        poly('pole',(24,20),(24,30),(24,42));join('canopy','pole')
        poly('table',(16,30),(24,30),(32,30));join('table','pole')
        for x in (8,40):
         poly(f'seat-{x}',(x-2,38),(x,38),(x+2,38))
         line(f'leg-{x}',(x,38),(x,42));join(f'seat-{x}',f'leg-{x}')
