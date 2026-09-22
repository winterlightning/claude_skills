"""A rounded server physically connected to a three-branch hexagonal network hub. VRECT_L 8,4–40,44. Repair of existing draft: enlarge hub opening and simplify indicator to a dot. Lucide server informs rounded casing and dot indicator. Shared center axis x24, receiving contours split at real connector nodes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '04dc2fcf-0f0c-4e8b-b40b-5ae745f490db'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/elemental live 1_04dc2fcf-0f0c-4e8b-b40b-5ae745f490db.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'rounded-server-connected-to-hexagonal-hub'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ('Live Video Encoding Server',)
    keywords = ('live', 'video', 'encoding', 'server')
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
        path("server",(12,4),[("L",(36,4)),("A",(40,8),4,4,True),("L",(40,20)),("A",(36,24),4,4,True),("L",(24,24)),("L",(12,24)),("A",(8,20),4,4,True),("L",(8,8)),("A",(12,4),4,4,True)],True)
        self.add_dot("indicator",(18,14))
        self.add_line("slot",(28,14),(31,14))
        self.add_polyline("hub",(24,32),(30,35),(30,37),(30,39),(24,42),(18,39),(18,37),(18,35),closed=True)
        self.add_line("stem",(24,24),(24,32))
        self.add_line("left",(8,37),(18,37))
        self.add_line("right",(30,37),(40,37))
        self.add_line("bottom",(24,42),(24,44))
        self.relate("connect","stem","server")
        for part in ("stem","left","right","bottom"):self.relate("connect",part,"hub")

