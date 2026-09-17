"""Monk in Robe.

Plan: Round bald head center24,16 radius8 touches broad curved shoulders at y28. Robe crosses diagonally from right shoulder. Bounds (4,8)-(44,40).
Construction: human_ref/user.svg: circular head and curved shoulders; source diagonal robe fold.
Reduction: Removed ears and nose; one sweeping fold identifies the robe without crowding.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'a5df130c-736c-50a4-a363-25494841b316'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/figure_a5df130c-736c-50a4-a363-25494841b316.svg'
AUTHOR = 'gpt-6'


class IconMonkInRobe(Solo48):
    icon_id = 'monk-in-robe'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('monk', 'in', 'robe')
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
        circle('head',24,16,8)
        path('shoulders',(4,40),[('L',(4,38)),('A',(24,28),20,10,True),('A',(36,30),20,10,True),('A',(44,38),20,10,True),('L',(44,40))])
        self.relate('connect','head','shoulders')
        path('robe-fold',(36,30),[('C',(12,40),(30,35),(22,38))]);self.relate('connect','robe-fold','shoulders')
