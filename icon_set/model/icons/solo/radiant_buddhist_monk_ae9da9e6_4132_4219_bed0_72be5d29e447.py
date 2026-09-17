"""Radiant Buddhist Monk.

Plan: Circular head (28,16), radius6; elliptical shoulders apex(28,26), robe fold, three rays. Centerlines (6,6)-(42,42).
Construction: human_ref/user.svg circular head and curved shoulders; source robe and radiance.
Reduction: Three rays and one robe fold; base omitted to keep the robe open.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'ae9da9e6-4132-4219-bed0-72be5d29e447'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/magha puja_ae9da9e6-4132-4219-bed0-72be5d29e447.svg'
AUTHOR = 'gpt-6'


class IconRadiantBuddhistMonk(Solo48):
    icon_id = 'radiant-buddhist-monk'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('radiant', 'buddhist', 'monk')
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
        circle('head',28,16,6)
        path('robe',(14,42),[('L',(14,34)),('A',(28,26),14,8,True),('A',(42,34),14,8,True),('L',(42,42))])
        self.relate('connect','head','robe')
        path('fold',(42,34),[('C',(14,42),(32,40),(24,42))]);self.relate('connect','fold','robe')
        self.add_line('ray-diagonal',(6,6),(9,9));self.add_line('ray-left',(6,22),(9,22));self.add_line('ray-right',(40,8),(42,6))
