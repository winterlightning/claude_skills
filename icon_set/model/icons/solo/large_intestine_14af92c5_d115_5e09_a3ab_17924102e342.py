"""Large Intestine.
Plan: Centerline (6,6)-(42,42). Broad inverted-U colon with asymmetrical descending terminal and left appendix. Smooth wall bands replace crowded scallops.
References: supplied original source; no direct useful Lucide match; source silhouette and asymmetric terminals.
Human guidance: human_ref/user.svg and full_body_ref.png where applicable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14af92c5-d115-5e09-a3ab-17924102e342'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty intestine_14af92c5-d115-5e09-a3ab-17924102e342.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'large-intestine-14af92c5'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ('large-intestine',)
    keywords = ('large', 'intestine')

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
        stroke("colon",(6,32),[((6,16),),((16,6),10,10,True),((32,6),),((42,16),10,10,True),((42,30),),((34,38),8,8,True),((34,42),),((24,42),),((24,34),),((28,30),4,4,True),((32,26),4,4,False),((32,20),),((28,16),4,4,False),((20,16),),((16,20),4,4,False),((16,32),),((11,37),5,5,True),((6,32),5,5,True)],True)
        self.add_line("appendix",(11,37),(11,42));self.relate("connect","colon","appendix")

