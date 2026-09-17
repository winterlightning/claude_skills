"""Person with Folded Heart Arms.
Plan: (8,4)-(40,44). Circular head above a heart-shaped embrace with two diagonal arm seams. Head bottom16 to neck24 is exact8 centerline /4 ink.
References: supplied original source; human_ref/user.svg and full_body_ref.png; Lucide heart: paired lobes and pointed lower silhouette.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3f398d6d-b575-40f5-b6ab-df8255b9c6c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/phone digital well being heart_3f398d6d-b575-40f5-b6ab-df8255b9c6c6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-with-folded-heart-arms-3f398d6d'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('person-with-folded-heart-arms',)
    keywords = ('person', 'with', 'folded', 'heart', 'arms')

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
        circle("head",24,10,6)
        self.add_line("torso",(24,24),(24,30))
        stroke("heart-body",(24,30),[((8,30),8,6,False),((16,37),),((24,44),),((32,37),),((40,30),),((24,30),8,6,False)],True)
        self.add_polyline("arms",(16,37),(24,30),(32,37));self.relate("connect","heart-body","arms");self.relate("connect","torso","heart-body");self.relate("connect","torso","arms")
        self.mark_human_figure("person",head="head",torso="torso",torso_junction="start")

