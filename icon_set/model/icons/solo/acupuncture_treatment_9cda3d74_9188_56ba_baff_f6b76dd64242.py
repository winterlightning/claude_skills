from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9cda3d74-9188-56ba-baff-f6b76dd64242'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/acupuncture_9cda3d74-9188-56ba-baff-f6b76dd64242.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'acupuncture-treatment'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('acupuncture', 'treatment')

    def build(self):
        # Plan: Prone patient and two needles; HRECT_L (4,8)-(44,40). Shared human_ref/full_body_ref.png round head and bent arm. Head center (9,30), radius5; actual neck (22,30): 22-(9+5)=8 centerline, 4 ink. Lucide syringe informs minimal shafts; omit thick needle grips.
        self.circle('head',9,30,5)
        self.add_polyline('back',(22,30),(28,30),(36,30),(44,30))
        self.add_polyline('arm',(22,30),(22,40),(38,40));self.relate('connect','arm','back')
        self.add_line('needle-left',(28,8),(28,30));self.add_line('needle-right',(40,10),(36,30))
        self.relate('connect','needle-left','back');self.relate('connect','needle-right','back')
        self.mark_human_figure('patient',head='head',torso='back-1',torso_junction='start')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i, command in enumerate(commands):
            tag=f"{name}-{i}"
            if len(command)==2:
                self.add_line(tag,start,command); start=command
            else:
                self.add_bezier(tag,start,command); start=command[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
