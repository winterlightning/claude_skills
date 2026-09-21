'A walking figure faces right with separated legs, a forward reaching arm, and a round featureless head. The trailing hand carries a rectangular briefcase with a handle and horizontal division.\nPlan: Walking commuter, case in trailing hand; simplified round-ended figure with exact head gap. Exact centerline extremes follow the declared SOLO48 keyshape.\nConstruction reference: Shared human_ref/full_body_ref.png: circular head and moving limbs; reduced case remains attached to trailing hand.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22bd302b-7cdc-4d13-8f4e-efe2bab54d50'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/coffee delivery_22bd302b-7cdc-4d13-8f4e-efe2bab54d50.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'walking-commuter-with-briefcase'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('walking', 'commuter', 'with', 'briefcase')

    # Repair: Raise the forward hand to clear the stepping leg; retain torso-axis head alignment and exact detached gap.
    # Repair: Use analytic semicircular head support and a smaller case clear of the trailing foot; head bottom16 to torso24 preserves exactly4 ink gap.
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

        self.add_arc('head-top',(23,11),(33,11),radius_x=5,sweep=True);self.add_arc('head-bottom',(33,11),(23,11),radius_x=5,sweep=True);self.add_contour('head','head-top','head-bottom',closed=True)
        line('torso',(28,24),(28,32));poly('legs',(22,42),(28,32),(38,42));join('torso','legs')
        poly('arm-front',(28,24),(38,24),(42,22));join('arm-front','torso')
        poly('arm-back',(28,24),(14,26),(10,30));join('arm-back','torso')
        poly('case',(6,30),(10,30),(14,30),(14,40),(6,40),(6,30));join('case','arm-back')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
