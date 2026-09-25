'Filter cartridge with two parallel smooth waves, three inlet strokes and a right-pointing outlet arrow.\nPlan: HRECT_L exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: No useful exact local Lucide match; smooth repeated wave tangents replace kinked arc junctions.\nOmissions: Fine cap thickness omitted; two waves preserve flowing air through the filter.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '32ea1e81-906d-440f-b0a0-6853ec1e4a95'
SOURCE_PATH = 'pictographic-primitives/transportation/engine air filter_32ea1e81-906d-440f-b0a0-6853ec1e4a95.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='engine-air-filter-flow'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/transportation"
    aliases=()
    keywords=('engine', 'air', 'filter', 'flow')
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

        for y in (8,40):poly(f'cap-{y}',(16,y),(18,y),(30,y),(32,y))
        for x in (18,30):
         path(f'pleat-{x}',(x,8),[('C',(x,24),(x-2,13),(x-2,19)),('C',(x,40),(x+2,29),(x+2,35))])
         for y in (8,40):join(f'pleat-{x}',f'cap-{y}')
        for i,y in enumerate((14,24,34)):line(f'inlet-{i}',(4,y),(8,24+(y-24)*4//5))
        poly('arrow',(40,20),(44,24),(40,28))
