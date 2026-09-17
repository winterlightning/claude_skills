from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '652c1f5c-1580-466f-b7a8-4d26a6efff34'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty back_652c1f5c-1580-466f-b7a8-4d26a6efff34.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'back-massage'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('back', 'massage')

    def build(self):
        # Plan: Therapist above reclining patient; HRECT_L (4,8)-(44,40). Shared full_body_ref.png. Therapist center(20,12),r4,neck(20,24): gap8 centerline. Patient center(40,36),r4,neck(28,36): gap8. Exactly 4 ink for both. Omit patient bent arm; actual hands meet back.
        self.circle('therapist-head',20,12,4)
        self.circle('patient-head',40,36,4)
        self.add_line('therapist-torso',(20,24),(20,28))
        self.path('arms',(12,36),[(12,30),((12,26),(16,24),(20,24)),((24,24),(28,26),(28,30)),(28,36)])
        self.add_polyline('patient-back',(4,36),(12,36),(28,36))
        self.relate('connect','arms','therapist-torso');self.relate('connect','arms','patient-back')
        self.mark_human_figure('therapist',head='therapist-head',torso='therapist-torso',torso_junction='start')
        self.mark_human_figure('patient',head='patient-head',torso='patient-back-2',torso_junction='end')

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
