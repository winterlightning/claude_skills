"""Woman in Draped Attire.

Plan: Circular face with top bun, curved shoulders and diagonal drape. Bounds (6,6)-(42,42).
Construction: icon-avatar and human_ref/user.svg touching head/body construction.
Reduction: Bun and diagonal drape retained; tiny ears and parted hair removed for clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'cc95eb24-a835-44c4-8b2f-8722e687ddef'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/gokul ashtami_cc95eb24-a835-44c4-8b2f-8722e687ddef.svg'
AUTHOR = 'gpt-6'


class IconWomanInDrapedAttire(Solo48):
    icon_id = 'woman-in-draped-attire'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('woman', 'in', 'draped', 'attire')
    human_construction = "bust"

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
        circle('head',24,18,8)
        path('bun',(24,10),[('A',(24,6),2,2,True),('A',(24,10),2,2,True)],True);self.relate('connect','head','bun')
        path('shoulders',(6,42),[('L',(6,40)),('C',(12,32),(6,36),(8,34)),('A',(24,30),20,10,True),('A',(36,32),20,10,True),('C',(42,40),(40,34),(42,36)),('L',(42,42))]);self.relate('connect','head','shoulders')
        path('drape',(36,32),[('C',(16,42),(30,38),(22,40))]);self.relate('connect','drape','shoulders')
