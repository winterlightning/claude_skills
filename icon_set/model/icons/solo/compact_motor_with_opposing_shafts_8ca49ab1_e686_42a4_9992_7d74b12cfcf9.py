"""An upright DC motor with opposed shafts. VRECT_M 10,4–38,44. The body owns a shared radius4 casing, seam nodes and two repeated vent dots. Source establishes opposing shafts and casing seam; Lucide cpu informs clean orthogonal terminal attachments. Omit curved vent brackets and shaft thickness."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ca49ab1-e686-42a4-9992-7d74b12cfcf9'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/electronics motor_8ca49ab1-e686-42a4-9992-7d74b12cfcf9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'compact-motor-with-opposing-shafts'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ('Electric DC Motor',)
    keywords = ('electric', 'dc', 'motor')
    def build(self):
        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,command in enumerate(commands):
                k=f"{name}-{i}"
                kind,end,*args=command
                if kind=="L": self.add_line(k,here,end)
                elif kind=="A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=="C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[("A",(x,y+r),r,r,True),("A",(x,y-r),r,r,True)],True)
        path("body",(24,12),[("L",(34,12)),("A",(38,16),4,4,True),("L",(38,20)),("L",(38,33)),("A",(34,37),4,4,True),("L",(24,37)),("L",(14,37)),("A",(10,33),4,4,True),("L",(10,20)),("L",(10,16)),("A",(14,12),4,4,True),("L",(24,12))],True)
        self.add_line("shaft-top",(24,4),(24,12))
        self.add_line("shaft-bottom",(24,37),(24,44))
        self.add_line("seam",(10,20),(38,20))
        for part in ("shaft-top","shaft-bottom","seam"):self.relate("connect",part,"body")
        for i,x in enumerate((20,28)):self.add_dot(f"vent-{i}",(x,28))

