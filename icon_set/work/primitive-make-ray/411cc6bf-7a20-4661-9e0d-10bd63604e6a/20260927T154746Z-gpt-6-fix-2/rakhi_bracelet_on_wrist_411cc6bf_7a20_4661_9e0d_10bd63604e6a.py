"""Fresh revision of rakhi-bracelet-on-wrist.

Original and rejected SVG compared before drawing. The clasped hand was reduced to an empty loop; restored the three knuckle lobes and bracelet at the wrist.
"""
"""Rakhi Bracelet on Wrist.

Plan: Downward diagonal hand with circular rakhi at wrist; centerlines (6,6)-(42,42).
Construction: Lucide hand curved anatomy; source downward diagonal wrist.
Reduction: One finger crease; loop reduced to circular ornament and short cord.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '411cc6bf-7a20-4661-9e0d-10bd63604e6a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/work/primitive-fix-thuan/solo__rakhi-bracelet-on-wrist/20260927T153833Z-thuan-mac-1/reference/raksha bandhan_411cc6bf-7a20-4661-9e0d-10bd63604e6a.svg'
AUTHOR = 'gpt-6'


class IconRakhiBraceletOnWrist(Solo48):
    icon_id = 'rakhi-bracelet-on-wrist'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('rakhi', 'bracelet', 'on', 'wrist')

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
        path('hand',(28,14),[('L',(42,24)),('L',(36,34)),('C',(22,42),(30,40),(28,42)),('C',(14,38),(18,42),(16,40)),('C',(6,28),(10,34),(6,32)),('C',(8,22),(6,26),(6,24)),('L',(20,10))])
        circle('rakhi',24,10,4);self.relate('connect','rakhi','hand')
        self.add_line('cord',(28,10),(32,6));self.relate('connect','cord','rakhi')
        self.add_line('crease',(14,38),(18,30));self.relate('connect','crease','hand')
