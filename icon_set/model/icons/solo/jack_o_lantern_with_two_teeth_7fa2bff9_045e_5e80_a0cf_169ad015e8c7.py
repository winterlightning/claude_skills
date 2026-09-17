"""Jack O Lantern with Two Teeth.

Plan: Rounded pumpkin around axis24 with eye marks and distinctive two tooth grin. Bounds (6,6)-(42,42).
Construction: Source pumpkin face; no useful local Lucide pumpkin match.
Reduction: Omitted small nose and facial cutout outlines; open marks preserve the named grin.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '7fa2bff9-045e-5e80-a0cf-169ad015e8c7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/halloween figure_7fa2bff9-045e-5e80-a0cf-169ad015e8c7.svg'
AUTHOR = 'gpt-6'


class IconJackOLanternWithTwoTeeth(Solo48):
    icon_id = 'jack-o-lantern-with-two-teeth'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('jack', 'o', 'lantern', 'with', 'two', 'teeth')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path('pumpkin',(24,12),[('C',(42,27),(38,8),(42,16)),('C',(24,42),(42,38),(35,42)),('C',(6,27),(13,42),(6,38)),('C',(24,12),(6,16),(10,8))],True)
        path('stem',(24,12),[('C',(30,6),(24,8),(26,6))]);self.relate('connect','stem','pumpkin')
        self.add_dot('eye-left',(16,22));self.add_dot('eye-right',(32,22))

        path('smile',(15,30),[('C',(20,33),(16,32),(18,33)),('L',(28,33)),('C',(33,30),(30,33),(32,32))])
        self.add_line('tooth-left',(20,33),(20,30));self.add_line('tooth-right',(28,33),(28,30))
        self.relate('connect','tooth-left','smile');self.relate('connect','tooth-right','smile')
