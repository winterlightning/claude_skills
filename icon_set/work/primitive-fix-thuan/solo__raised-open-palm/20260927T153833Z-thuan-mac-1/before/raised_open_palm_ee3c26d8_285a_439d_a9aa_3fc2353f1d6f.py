"""Raised Open Palm.

Plan: Four round fingertips from shared radius4 and step8 series, left thumb, rounded palm. Bounds (4,8)-(44,40).
Construction: Lucide hand and human_ref limb construction. Byte-identical reference to previous open palm sources.
Reduction: Finger creases shortened for clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'ee3c26d8-285a-439d-a9aa-3fc2353f1d6f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/hand_ee3c26d8-285a-439d-a9aa-3fc2353f1d6f.svg'
AUTHOR = 'gpt-6'


class IconRaisedOpenPalm(Solo48):
    icon_id = 'raised-open-palm'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('raised', 'open', 'palm')

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
        first_x, radius = 12, 4
        step = 2 * radius
        heights = (14,12,14,20)
        commands=[]
        for i,y in enumerate(heights):
         x=first_x+i*step
         commands.extend([('L',(x,y)),('A',(x+step,y),radius,radius,True)])
        commands.extend([('L',(44,28)),('A',(32,40),12,12,True),('L',(24,40)),('C',(4,28),(16,40),(10,34)),('C',(12,28),(4,22),(8,22))])
        path('outline',(12,28),commands,True)
        for i,(name,end_y) in enumerate(zip(('index','middle','ring'),(24,24,26))):
         x=first_x+(i+1)*step
         start=(x,max(heights[i],heights[i+1]))
         self.add_line(name,start,(x,end_y));self.relate('connect',name,'outline')

# Additional source explicitly assigned to this existing concept by its brief.
SOURCE_REFERENCES = (('83c18653-4bbf-498c-80b3-a71d2a06335a', '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/labor hands_83c18653-4bbf-498c-80b3-a71d2a06335a.svg'),)
