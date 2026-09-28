'A xenomorph with a smooth elongated dome, recessed face and curled body and tail.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: shell: coherent curl; source-specific elongated skull.\nOmissions: Tiny dorsal spines, teeth and short inner chest return omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4cce42f7-9a4b-47ca-8564-c6162d026735'
SOURCE_PATH = 'pictographic-primitives/science/xenomorph_4cce42f7-9a4b-47ca-8564-c6162d026735.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='xenomorph-creature'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "science"
    categories = ("science", "primitives")
    aliases=()
    keywords=('xenomorph', 'creature')
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

        path('skull',(6,22),[('C',(30,6),(6,10),(20,6)),('A',(30,16),5,5,True),('C',(14,26),(22,16),(14,18)),('C',(6,22),(10,26),(6,26))],True)
        path('body',(30,16),[('C',(42,28),(38,16),(42,20)),('C',(28,42),(42,36),(36,42)),('C',(14,34),(21,42),(16,39)),('C',(29,32),(20,34),(26,34)),('C',(29,28),(30,31),(30,29))]);join('body','skull')
