'Raised finger, rounded thumb and closed palm beneath a smooth contact arc.\nPlan: VRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: pointer: extended index finger with semicircular fingertip and one coherent palm outline.\nOmissions: Folded finger seams omitted; palm closed.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7cd3d777-8324-4e1a-97bc-54f53f64ab25'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gesture tap 2_7cd3d777-8324-4e1a-97bc-54f53f64ab25.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tapping-hand-with-contact-arc'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases=()
    keywords=('tapping', 'hand', 'with', 'contact', 'arc')
    def build(self):

        def path(name,start,commands,closed=False):
            point=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                member=f'{name}-{i}'
                if kind=='L': self.add_line(member,point,end)
                elif kind=='A': self.add_arc(member,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,point,(args[0],args[1],end))
                point=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('hand',(18,29),[('L',(18,18)),('A',(26,18),4,4,True),('L',(26,28)),('L',(33,28)),('C',(40,34),(37,28),(40,30)),('L',(37,41)),('C',(33,44),(36,43),(35,44)),('L',(20,44)),('C',(16,41),(18,44),(17,43)),('L',(9,32)),('C',(8,29),(8,31),(8,30)),('C',(14,25),(8,24),(10,21)),('L',(18,29))],True)
        path('contact',(10,14),[('A',(34,14),12,10,True)])
