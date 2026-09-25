"""IV Bag on Stand.
Plan: Centerlines (8,4)-(40,44); tall bent stand owns hook, bag hangs from stem; liquid divider and descending tube retained.
References: supplied original source; no direct useful Lucide IV match; source hanging assembly, shared rounded corners.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6bb77d0d-1d29-4750-b55c-c89fc478e932'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/transfusion bag hang_6bb77d0d-1d29-4750-b55c-c89fc478e932.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'iv-bag-on-stand-6bb77d0d'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('iv-bag-on-stand',)
    keywords = ('iv', 'bag', 'on', 'stand')

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
        stroke("stand",(16,10),[((16,8),),((20,4),4,4,True),((32,4),),((40,12),8,8,True),((40,44),)])
        self.add_line("hanger",(16,10),(16,16));self.relate("connect","stand","hanger")
        stroke("bag",(16,16),[((20,16),),((24,20),4,4,True),((24,24),),((24,30),),
            ((20,34),4,4,True),((16,34),),((12,34),),((8,30),4,4,True),
            ((8,24),),((8,20),),((12,16),4,4,True),((16,16),)],True)
        self.relate("connect","hanger","bag")
        self.add_line("level",(8,24),(24,24));self.relate("connect","bag","level")
        self.add_line("tube",(16,34),(16,44));self.relate("connect","bag","tube")

