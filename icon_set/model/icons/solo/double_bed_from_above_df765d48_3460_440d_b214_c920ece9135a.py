"""Double Bed from Above.

Plan: Rounded bed frame with two upper pillow panels and broad lower cover. Bounds (8,4)-(40,44).
Construction: Lucide bed-double paired upper partitions and rounded frame.
Reduction: Pillows share frame and blanket boundaries, narrow blanket band omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'df765d48-3460-440d-b214-c920ece9135a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/hotel double bed_df765d48-3460-440d-b214-c920ece9135a.svg'
AUTHOR = 'gpt-6'


class IconDoubleBedFromAbove(Solo48):
    icon_id = 'double-bed-from-above'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    aliases = ()
    keywords = ('double', 'bed', 'from', 'above')

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
        path('bed',(12,4),[('L',(24,4)),('L',(36,4)),('A',(40,8),4,4,True),('L',(40,20)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,20)),('L',(8,8)),('A',(12,4),4,4,True)],True)
        path('blanket',(8,20),[('L',(24,20)),('L',(40,20))]);self.relate('connect','blanket','bed')
        self.add_line('pillows',(24,4),(24,20));self.relate('connect','pillows','bed');self.relate('connect','pillows','blanket')
