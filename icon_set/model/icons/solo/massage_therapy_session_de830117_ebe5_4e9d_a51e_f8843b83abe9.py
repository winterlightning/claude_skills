"""Massage Therapy Session.
Plan: (6,6)-(42,42). Therapist upper body leans toward prone patient; equal circular heads. Exact8 centerline head gaps; table stroke omitted.
References: supplied original source; human_ref/user.svg and full_body_ref.png: circular heads, detached shoulders, minimal gesture.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de830117-ebe5-4e9d-a51e-f8843b83abe9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/massage top_de830117-ebe5-4e9d-a51e-f8843b83abe9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'massage-therapy-session-de830117'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('massage-therapy-session',)
    keywords = ('massage', 'therapy', 'session')

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
        circle("therapist-head",12,10,4)
        self.add_line("therapist-torso",(12,22),(12,28))
        self.add_polyline("arm",(12,22),(22,26),(22,38));self.relate("connect","therapist-torso","arm")
        circle("patient-head",38,38,4)
        self.add_polyline("patient-torso",(26,38),(22,38),(6,38));self.relate("connect","arm","patient-torso")
        self.mark_human_figure("therapist",head="therapist-head",torso="therapist-torso",torso_junction="start")
        self.mark_human_figure("patient",head="patient-head",torso="patient-torso-1",torso_junction="start")

