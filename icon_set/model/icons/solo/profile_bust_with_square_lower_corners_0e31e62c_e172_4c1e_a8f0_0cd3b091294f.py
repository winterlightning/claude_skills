'A featureless round head sits above a broad shoulder outline with a flat base. The shoulders curve into straight upright sides, meeting the bottom edge at distinct square corners.\nPlan: Circular head and broad circular shoulder arc; head bottom24 shoulder top28 gives zero ink gap. Normalize oval head to shared human proportions; open lower bust.\nConstruction reference: human_ref/user.svg and avatar specialization: circular face, rounded shoulders and zero painted gap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e31e62c-e172-4c1e-a8f0-0cd3b091294f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/democrat_0e31e62c-e172-4c1e-a8f0-0cd3b091294f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'profile-bust-with-square-lower-corners'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('profile', 'bust', 'with', 'square', 'lower', 'corners')

    # Repair: Restore the source torso baseline and short sides. Circular head bottom20 and shoulder top24 give zero ink gap; preserve square lower corners only for source41.
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member='body-top' if name=='body' and j==0 else f'{name}-{j}'
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

        self.add_arc('head-top',(16,12),(32,12),radius_x=8,sweep=True)
        self.add_arc('head-bottom',(32,12),(16,12),radius_x=8,sweep=True)
        self.add_contour('head','head-top','head-bottom',closed=True)
        path('body',(8,40),[('A',(24,24),16,16,True),('A',(40,40),16,16,True),('L',(40,44)),('L',(8,44)),('L',(8,40))],True);join('head','body')
