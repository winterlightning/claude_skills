"""Two open bone shafts with smooth uneven articular lobes and a clear joint space. VRECT_M centerlines (10,4)-(38,44). Preserve anatomical asymmetry; no detached head or body is present, so the human head gap does not apply. No omissions."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bae3cd4c-6954-5fed-9b94-9b4a7fbb195a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__knee-joint-bae3cd4c/20260924T100528Z-thuan-mac/reference/specialty knee_bae3cd4c-6954-5fed-9b94-9b4a7fbb195a.svg'
AUTHOR = 'gpt-6'
CONSTRUCTION_REFERENCE = 'bone; human_ref/user.svg and full_body_ref.png'
DESIGN_PLAN = 'Two open bone shafts with smooth uneven articular lobes and a clear joint space. VRECT_M centerlines (10,4)-(38,44). Preserve anatomical asymmetry; no detached head or body is present, so the human head gap does not apply. No omissions.'
class Drawing(Solo48):
    icon_id = 'knee-joint-bae3cd4c-solo'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('knee', 'joint', 'bae3cd4c')
    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            member=f'{name}-{i}'
            if kind=='L': self.add_line(member,start,end)
            elif kind=='A': self.add_arc(member,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(member,start,(args[0],args[1],end))
            members.append(member); start=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,cx,cy,r):
        self.path(name,(cx-r,cy),[('A',(cx,cy-r),r,r,True),('A',(cx+r,cy),r,r,True),('A',(cx,cy+r),r,r,True),('A',(cx-r,cy),r,r,True)],True)


    def build(self):
        self.path('femur',(14,4),[('L',(16,11)),('C',(10,17),(14,13),(10,13)),('C',(16,21),(10,20),(13,21)),('C',(24,19),(20,21),(20,19)),('C',(31,20),(28,19),(28,20)),('C',(38,15),(35,20),(38,19)),('C',(34,9),(38,12),(35,12)),('L',(32,4))])
        self.path('tibia',(14,44),[('C',(10,33),(14,36),(10,37)),('C',(16,30),(10,29),(13,30)),('C',(24,32),(20,30),(20,32)),('C',(32,30),(28,32),(28,30)),('C',(38,33),(35,29),(38,29)),('C',(32,44),(38,37),(32,36))])
