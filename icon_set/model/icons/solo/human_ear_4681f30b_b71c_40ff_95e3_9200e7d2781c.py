"""Human Ear.
Plan: Centerline box (10,4)-(38,44); open outer rim and single open canal curl; retain broad lobe, omit tight upper-fold hook.
References: supplied original source; Lucide ear: open rim and coherent inner curl.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4681f30b-b71c-40ff-95e3-9200e7d2781c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/hearing aid ear_4681f30b-b71c-40ff-95e3-9200e7d2781c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'human-ear-4681f30b'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('human-ear',)
    keywords = ('human', 'ear')

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
        stroke("rim", (10,18), [((38,18),14,14,True), ((28,34),10,16,True),
            ((20,44),8,10,True), ((10,34),10,10,True)])
        stroke("fold",(20,16),[((26,22),6,6,True),((20,28),6,6,True)])
