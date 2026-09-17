"""Open Palm Hand.

Plan: Four round fingertips, shared finger radius4 and step8; left thumb and rounded palm. Bounds (4,8)-(44,40).
Construction: Lucide hand original and atomic-debug: rounded tips, continuous palm and separate finger creases. Human-reference simple rounded limb vocabulary.
Reduction: Shortened finger creases and widened fingers to the SOLO48 spacing budget. Identical reference subjects use the same construction under separate source UUIDs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'bc1a4fc0-cd35-423d-909c-bad3ddffd5c9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/hand_bc1a4fc0-cd35-423d-909c-bad3ddffd5c9.svg'
AUTHOR = 'gpt-6'


class IconOpenPalmHand(Solo48):
    icon_id = 'open-palm-hand-bc1a4fc0-cd35-423d-909c-bad3ddffd5c9'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('open', 'palm', 'hand')

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
        # The fingertip series owns the shared radius and spacing; heights preserve the hand's anatomy.
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
