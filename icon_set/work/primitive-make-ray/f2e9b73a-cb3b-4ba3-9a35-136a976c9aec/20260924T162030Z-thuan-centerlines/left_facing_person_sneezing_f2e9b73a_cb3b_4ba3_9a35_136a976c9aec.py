'Continuous face profile with rounded skull, clear nose and mouth opening, smooth neck and three exhalation strokes.\nPlan: SQUARE exact SOLO48 envelope; coherent contours, shared parameters, 4-unit stroke.\nConstruction: human_ref/user.svg: head/shoulder proportions; source retains its continuous profile neck, so detached-head gap does not apply.\nOmissions: Small eye omitted.\nFeedback: smooth centerlines, no kinks or stray nodes; preserve concept.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f2e9b73a-cb3b-4ba3-9a35-136a976c9aec'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__left-facing-person-sneezing/20260924T162030Z-thuan-mac/reference/sneeze_f2e9b73a-cb3b-4ba3-9a35-136a976c9aec.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='left-facing-person-sneezing'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('left', 'facing', 'person', 'sneezing')
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

        path('profile',(42,42),[('C',(34,29),(38,36),(31,34)),('C',(40,17),(36,24),(40,23)),('C',(28,6),(40,10),(35,6)),('C',(18,17),(21,6),(18,10)),('L',(14,24)),('L',(20,24)),('C',(20,32),(26,24),(26,32)),('L',(20,35)),('C',(25,42),(20,38),(23,39))])
        line('breath-upper',(6,22),(6,22))
        line('breath-middle',(6,32),(10,32))
        line('breath-lower',(6,42),(10,40))
