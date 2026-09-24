'A right-facing alligator has a long blunt snout, raised eye ridge, and sawtooth bumps along its back. Short legs sit below the low body, and a curled tail turns around the left side.\nPlan: Low alligator with long snout, raised eye, back bumps, legs and curling tail. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: No useful direct Lucide match; coherent contours reconstructed from the inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '033c9d4f-a0ab-42dc-80b5-4f148935d09a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/alligator_033c9d4f-a0ab-42dc-80b5-4f148935d09a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'low-alligator-in-profile'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('low', 'alligator', 'in', 'profile')

    # Repair: Widen the snout to fit a mouth and simplify two near-side legs into one bent leg; preserve the curved tail, sawtooth back and eye ridge.
    # Repair: Build the eye ridge from two tangent curves sharing its exact top extreme.
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

        path('animal',(14,40),[('C',(4,26),(6,40),(4,34)),('C',(12,16),(4,20),(8,16)),('L',(16,12)),('L',(20,16)),('L',(24,12)),('L',(28,16)),('C',(32,8),(28,10),(30,8)),('C',(36,16),(34,8),(36,10)),('L',(44,16)),('L',(44,32)),('L',(34,32)),('L',(36,40)),('L',(28,40)),('L',(24,32)),('L',(16,32))])
        line('mouth',(36,24),(44,24));join('mouth','animal')
