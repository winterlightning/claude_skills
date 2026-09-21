'Two oval loquat fruits hang at different angles from a short forked stem. One long pointed leaf extends to the upper right, above the overlapping upper shoulders of the fruit.\nPlan: Paired oval fruit with joined fork and one pointed leaf; intentional asymmetry.\nConstruction reference: No useful direct Lucide match; rebuilt from inspected original.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6a017b65-7ad3-4134-b1fb-d247df4c5d75'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/loquat_6a017b65-7ad3-4134-b1fb-d247df4c5d75.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'paired-loquats-hanging-beneath-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('paired', 'loquats', 'hanging', 'beneath', 'leaf')

    # Repair: Separate oval fruits and move all stem attachments to the leaf node.
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

        path('left',(12,22),[('C',(6,32),(8,22),(6,26)),('C',(12,42),(6,38),(8,42)),('C',(18,32),(16,42),(18,38)),('C',(12,22),(18,26),(16,22))],True)
        path('right',(36,22),[('C',(30,32),(32,22),(30,26)),('C',(36,42),(30,38),(32,42)),('C',(42,32),(40,42),(42,38)),('C',(36,22),(42,26),(40,22))],True)
        line('stem',(24,6),(12,22));path('fork',(24,6),[('C',(36,22),(24,14),(30,18))]);join('stem','left');join('fork','right');join('stem','fork')
        path('leaf',(24,6),[('L',(42,6)),('C',(24,6),(40,16),(32,16))],True);join('leaf','stem');join('leaf','fork')
