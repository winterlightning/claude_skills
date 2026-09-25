'Three symmetric wireless signal arcs with progressively smaller spans and smooth centered crests.\nPlan: HRECT_M exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: wifi: concentric-looking centered arcs and shared symmetry.\nOmissions: No dot added; the original contains exactly three waves.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e84a88d0-3ca7-4537-a4d9-b98932585c2f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/other/electric waves_e84a88d0-3ca7-4537-a4d9-b98932585c2f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='wireless-signal-waves-batch-033'
    keyshape=Keyshape.HRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/other"
    aliases=()
    keywords=('wireless', 'signal', 'waves', 'batch', '033')
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

        for i,(left,right,top,end) in enumerate(((4,44,10,18),(12,36,23,29),(18,30,35,38))):
         half=(right-left)//2
         path(f'wave-{i}',(left,end),[('C',(24,top),(left+half//3,end-(end-top)*2//3),(24-half//3,top)),('C',(right,end),(24+half//3,top),(right-half//3,end-(end-top)*2//3))])
