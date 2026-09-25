'A uniformed cadet faces forward in a flat topped cap with a curved visor. A plain face sits above a round collar, central shirt seam and short chest mark.\nPlan: Uniform cap over circular jaw and touching circular shoulders; seam in open torso. Jaw bottom24 shoulder top28 gives zero ink gap.\nConstruction reference: human_ref/user.svg and avatar specialization: circular jaw, broad round shoulders and zero head/body ink gap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17c87c6c-d891-4d48-a3ca-6183386db6db'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_09/cadet_17c87c6c-d891-4d48-a3ca-6183386db6db.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'uniformed-cadet-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('uniformed', 'cadet', 'bust')

    # Repair: Give the central shirt seam9 units to curved shoulders.
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

        path('cap',(12,16),[('L',(12,10)),('A',(18,4),6,6,True),('L',(30,4)),('A',(36,10),6,6,True),('L',(36,16)),('L',(32,16)),('L',(16,16)),('L',(12,16))],True)

        self.add_arc('jaw',(16,16),(32,16),radius_x=8,radius_y=8,sweep=False);join('jaw','cap')
        path('body',(8,44),[('A',(24,28),16,16,True),('A',(40,44),16,16,True)]);join('jaw','body')
        line('shirt',(24,37),(24,44))
