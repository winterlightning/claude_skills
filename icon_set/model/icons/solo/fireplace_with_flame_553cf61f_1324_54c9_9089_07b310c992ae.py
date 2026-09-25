from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '553cf61f-1324-54c9-9089-07b310c992ae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/furnitures/fireplace_553cf61f-1324-54c9-9089-07b310c992ae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fireplace-with-flame'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "furnitures"
    aliases = ()
    keywords = ('fireplace', 'with', 'flame')

    def build(self):
        # Plan: Open hearth under a broad mantel; one flame. HRECT_L (4,8)-(44,40) preserves wide architecture. Lucide heater informs simple framed heating appliance, source owns flame. Secondary mantel thickness omitted.
        self.add_polyline('mantel',(4,8),(8,8),(40,8),(44,8))
        for name,x in [('left',8),('right',40)]:
            self.add_line(name,(x,8),(x,40));self.relate('connect',name,'mantel')
        self.path('flame',(24,20),[((24,26),(18,27),(18,32)),((18,36),(20,40),(24,40)),((28,40),(30,36),(30,32)),((30,27),(27,23),(24,20))],True)

    def path(self, name, start, commands, closed=False):
        members=[]
        for i, command in enumerate(commands):
            tag=f"{name}-{i}"
            if len(command)==2:
                self.add_line(tag,start,command); start=command
            else:
                self.add_bezier(tag,start,command); start=command[2]
            members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
