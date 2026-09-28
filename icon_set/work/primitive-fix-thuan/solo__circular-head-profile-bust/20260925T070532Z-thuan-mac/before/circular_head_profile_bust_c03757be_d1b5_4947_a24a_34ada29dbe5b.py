'A plain circular head floats above a broad shoulder shaped torso. The lower form has rounded upper corners, upright sides and a flat base, with no facial or clothing details.\nPlan: Circular head and broad circular shoulder arc; head bottom24 shoulder top28 gives zero ink gap. Normalize oval head to shared human proportions; open lower bust.\nConstruction reference: human_ref/user.svg and avatar specialization: circular face, rounded shoulders and zero painted gap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c03757be-d1b5-4947-a24a-34ada29dbe5b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bob_c03757be-d1b5-4947-a24a-34ada29dbe5b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-head-profile-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    aliases = ()
    keywords = ('circular', 'head', 'profile', 'bust')

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
        path('body',(8,40),[('A',(24,24),16,16,True),('A',(40,40),16,16,True),('L',(40,42)),('A',(38,44),2,2,True),('L',(10,44)),('A',(8,42),2,2,True),('L',(8,40))],True);join('head','body')
