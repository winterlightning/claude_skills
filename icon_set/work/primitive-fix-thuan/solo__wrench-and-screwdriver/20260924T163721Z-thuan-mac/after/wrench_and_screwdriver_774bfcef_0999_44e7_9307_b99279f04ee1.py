'Parallel diagonal wrench and screwdriver with rounded wrench head and straight tool shafts.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: wrench: open jaw, curved head and coherent handle; pencil-ruler: diagonal geometry.\nOmissions: Fine handle grip details omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='774bfcef-0999-44e7-9307-b99279f04ee1'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__wrench-and-screwdriver/20260924T163721Z-thuan-mac/reference/tool organizer 1_774bfcef-0999-44e7-9307-b99279f04ee1.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='wrench-and-screwdriver'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('wrench', 'and', 'screwdriver')
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

        path('wrench',(6,30),[('L',(16,18)),('C',(24,6),(14,10),(18,6)),('L',(24,14)),('L',(32,14)),('C',(26,22),(31,18),(29,20)),('L',(12,36)),('L',(10,36)),('A',(6,32),4,4,True),('L',(6,30))],True)
        poly('handle',(24,36),(34,26),(37,29),(40,32),(30,42),(24,36))
        line('shaft',(37,29),(42,24));join('shaft','handle')
