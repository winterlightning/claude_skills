from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'deb7552b-4e6f-5145-b54b-4d4a85be40bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/thai massage elbow_deb7552b-4e6f-5145-b54b-4d4a85be40bf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'elbow-massage'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('elbow', 'massage')

    def build(self):
        # Plan: Therapist behind seated recipient, bent arm pressing shoulder; bounds (6,6)-(42,42). Shared human_ref/full_body_ref.png circular heads. Therapist head(34,11),r5 neck(34,24); patient(11,24),r5 neck(11,37), both exact8 centerline gaps. Reduced recipient to shoulders.
        self.circle('therapist-head',34,11,5)
        self.circle('patient-head',11,24,5)
        self.path('therapist-torso',(34,24),[((40,24),(42,28),(42,34)),(42,42)])
        self.add_polyline('arm',(24,20),(26,37),(34,24));self.relate('connect','arm','therapist-torso')
        self.path('patient-torso',(11,37),[((8,37),(6,39),(6,42))])
        self.path('shoulder',(11,37),[((17,37),(21,37),(26,37)),(26,42)]);self.relate('connect','shoulder','patient-torso');self.relate('connect','shoulder','arm')
        self.mark_human_figure('therapist',head='therapist-head',torso='therapist-torso-0',torso_junction='start')
        self.mark_human_figure('patient',head='patient-head',torso='patient-torso-0',torso_junction='start')

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
