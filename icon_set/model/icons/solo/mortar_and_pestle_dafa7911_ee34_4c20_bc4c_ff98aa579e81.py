"""Mortar and Pestle.
Plan: (4,8)-(44,40). Broad bowl and foot; diagonal solid pestle emerges from the shared rim. Rolled rim reduced to one stroke.
References: supplied original source; Lucide cup-soda: broad functional vessel; source diagonal tool and pedestal.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dafa7911-ee34-4c20-bc4c-ff98aa579e81'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/mortar pestle_dafa7911-ee34-4c20-bc4c-ff98aa579e81.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'mortar-and-pestle-dafa7911'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('mortar-and-pestle',)
    keywords = ('mortar', 'and', 'pestle')

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
        stroke("bowl",(6,22),[((22,38),16,16,False),((38,22),16,16,False)])
        self.add_polyline("rim",(4,22),(6,22),(26,22),(38,22),(40,22))
        self.relate("connect","rim","bowl")
        self.add_polyline("foot",(14,40),(22,38),(30,40));self.relate("connect","foot","bowl")
        self.add_line("pestle",(26,22),(44,8));self.relate("connect","pestle","rim")

