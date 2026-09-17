"""Vampire Mouth with Fangs.

Plan: Mirrored open lips and two descending fangs, axis24. Bounds (4,8)-(44,40).
Construction: Source mouth; human reference economy for facial parts. No exact Lucide vampire-mouth match.
Reduction: Single outer lip contour and open fang strokes replace doubled lip and tooth outlines.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '7076b131-f274-5265-b048-1b89c5cdfab1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/lips vampire_7076b131-f274-5265-b048-1b89c5cdfab1.svg'
AUTHOR = 'gpt-6'


class IconVampireMouthWithFangs(Solo48):
    icon_id = 'vampire-mouth-with-fangs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('vampire', 'mouth', 'with', 'fangs')

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
        path('mouth',(4,22),[('C',(16,8),(8,16),(11,8)),('C',(24,12),(20,8),(22,10)),('C',(32,8),(26,10),(28,8)),('C',(44,22),(37,8),(40,16)),('C',(24,40),(39,34),(33,40)),('C',(4,22),(15,40),(9,34))],True)
        path('upper',(4,22),[('C',(14,18),(8,22),(10,18)),('C',(34,18),(20,16),(28,16)),('C',(44,22),(38,18),(40,22))]);self.relate('connect','upper','mouth')
        for x in [14,34]:self.add_line('fang'+str(x),(x,18),(x,28));self.relate('connect','fang'+str(x),'upper')
