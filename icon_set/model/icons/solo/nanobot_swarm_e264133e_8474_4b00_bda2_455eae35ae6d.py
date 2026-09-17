"""Nanobot Swarm.
Plan: (8,4)-(40,44). Five staggered hexagonal bots, each with a short attached lower stem. Tiny central eyes and curved appendages removed to keep each bot open and separated.
References: supplied original source; Lucide bot: repeated compact robot modules; source five-bot hexagonal cluster and stems.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e264133e-8474-4b00-bda2-455eae35ae6d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/nanobots_e264133e-8474-4b00-bda2-455eae35ae6d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'nanobot-swarm-e264133e'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('nanobot-swarm',)
    keywords = ('nanobot', 'swarm')

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
        for j,(x,y) in enumerate([(13,8),(35,8),(24,23),(13,38),(35,38)]):
            self.add_polyline(f"bot-{j}",(x-5,y),(x-3,y-4),(x+3,y-4),(x+5,y),(x+3,y+4),(x,y+4),(x-3,y+4),closed=True)
            self.add_line(f"stem-{j}",(x,y+4),(x,y+6));self.relate("connect",f"bot-{j}",f"stem-{j}")

