"""Laboratory Microscope.
Plan: Centerlines (8,4)-(40,44); diagonal optical tube, curved supporting arm, short specimen stage and broad base. Omit tiny eyepiece/ocular collars.
References: supplied original source; Lucide microscope: curved arm, diagonal optics, separate stage and horizontal base.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '101aaf57-5431-5ae4-a7e5-f05c16647c10'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/microscope_101aaf57-5431-5ae4-a7e5-f05c16647c10.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'laboratory-microscope-101aaf57'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('laboratory-microscope',)
    keywords = ('laboratory', 'microscope')

    def build(self):

        def stroke(name, start, segments, closed=False):
            members=[]
            for j,s in enumerate(segments):
                member=f"{name}-{j}"
                if len(s)==1: self.add_line(member,start,s[0])
                else: self.add_arc(member,start,s[0],radius_x=s[1],radius_y=s[2],sweep=s[3],large_arc=s[4] if len(s)>4 else False)
                members.append(member);start=s[0]
            self.add_contour(name,*members,closed=closed)
        def circle(name,cx,cy,r):
            stroke(name,(cx-r,cy),[((cx+r,cy),r,r,True),((cx-r,cy),r,r,True)],True)
        self.add_polyline("optics",(20,4),(28,10),(20,24),(12,18),closed=True)
        stroke("arm",(28,10),[((40,26),12,16,True),((28,36),12,10,True),((28,44),)])
        self.relate("connect","optics","arm")
        self.add_line("stage",(8,32),(20,32))
        self.add_polyline("base",(8,44),(28,44),(40,44));self.relate("connect","arm","base")

