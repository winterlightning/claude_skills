"""The rejected beaver had a pointed muzzle and square forward foot. Rounded the muzzle into the chest and the forward foot while retaining the seated haunch, small ear and flat tail. Omitted tiny eye and claw lines.
Plan: No useful direct Lucide beaver match; source rounded muzzle and seated haunch. Keyshape HRECT_L; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='24e8edf5-d262-4f32-8f70-02bfa6503ce9'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__seated-beaver-with-flat-tail/20260929T112716Z-thuan-mac/reference/beaver_24e8edf5-d262-4f32-8f70-02bfa6503ce9.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='seated-beaver-with-flat-tail'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                members.append(member);here=end
            self.add_contour(name,*members,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*pts): self.add_polyline(name,*pts)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r): path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('beaver',(14,32),[('C',(10,21),(10,29),(10,24)),('C',(28,14),(10,11),(21,14)),('C',(32,8),(28,10),(29,8)),('C',(36,12),(35,8),(36,10)),('C',(44,20),(41,13),(44,16)),('C',(36,25),(44,24),(40,25)),('L',(36,32)),('L',(40,32)),('A',(40,40),4,4,True),('L',(22,40)),('C',(14,32),(18,40),(14,37))],True)
        path('tail',(14,32),[('L',(8,32)),('A',(8,40),4,4,False),('L',(22,40))]);join('tail','beaver')
