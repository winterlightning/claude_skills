'A tall milk can has a rounded rectangular body, sloped shoulders, and a narrow neck beneath a domed lid. Short handles angle upward from both shoulders beside the horizontal upper body seam.\nPlan: Milk can shoulder slopes, separate domed lid at crown and rounded body; handles omitted for clarity.\nConstruction reference: No useful direct Lucide match; reconstructed from the inspected original silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6e17ac5-4fa7-466b-8fb9-4a1985a11ad7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/milk can_d6e17ac5-4fa7-466b-8fb9-4a1985a11ad7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lidded-dairy-milk-can'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('lidded', 'dairy', 'milk', 'can')

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

        path('can',(16,12),[('L',(32,12)),('L',(32,20)),('L',(40,28)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,28)),('L',(16,20)),('L',(16,12))],True)
        path('lid',(12,12),[('L',(12,10)),('A',(18,4),6,6,True),('L',(30,4)),('A',(36,10),6,6,True),('L',(36,12))]);join('lid','can')
