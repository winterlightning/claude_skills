"""Open Mouth in Side Section.
Plan: (4,8)-(44,40). Side section of open mouth with upper lip/teeth and lower tongue/jaw. Two small teeth reduced to one broad dental edge.
References: supplied original source; no direct useful Lucide match; source side-section lips, dental edge, tongue and jaw.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '83188d0d-6fe1-57ec-8f6f-153a95690e91'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/mouthwash teeth_83188d0d-6fe1-57ec-8f6f-153a95690e91.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'open-mouth-in-side-section-83188d0d'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    aliases = ('open-mouth-in-side-section',)
    keywords = ('open', 'mouth', 'in', 'side', 'section')

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
        stroke("upper",(4,8),[((10,8),),((18,8),),((34,24),16,16,True)])
        stroke("tooth",(10,8),[((10,18),),((18,18),),((18,8),)])
        self.relate("connect","upper","tooth")
        stroke("lower-jaw",(34,24),[((22,30),12,6,True),((12,30),),((12,40),6,5,False),((36,40),),((44,32),8,8,False),((44,24),)])
        self.relate("connect","upper","lower-jaw")

