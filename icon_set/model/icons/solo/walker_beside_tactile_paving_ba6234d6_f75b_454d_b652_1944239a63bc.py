'A walking person strides to the right beside three vertical rows of paving marks. The figure has a round detached head, bent arms and two widely separated legs.\nPlan: Walking figure next to three paving strokes; head center follows upper torso axis, 4 ink units detached. Paving dashes reduced to three runs.\nConstruction reference: human_ref/full_body_ref.png: outlined circle and round-ended limbs.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ba6234d6-f75b-454d-b652-1944239a63bc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blind walk path_ba6234d6-f75b-454d-b652-1944239a63bc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'walker-beside-tactile-paving'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('walker', 'beside', 'tactile', 'paving')

    # Repair: Two long paving runs replace three densely dashed rows; arm moved one unit for legal clearance. Exact detached torso/head ink gap remains 4.
    # Repair: Lower hip and raised forward arm open the torso/limb gaps while preserving a rightward walking pose.
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

        circle('head',29,10,4)
        line('torso',(29,22),(29,34))
        poly('arms',(22,29),(29,22),(37,24),(42,24));join('torso','arms')
        poly('legs',(23,42),(29,34),(39,42));join('torso','legs')
        self.mark_human_figure('walker',head='head',torso='torso',torso_junction='start')
        for x in (6,14): line(f'paving-{x}',(x,6),(x,42))
