"""Shining Star Tree Topper.

Plan: Five-point star on mounting sleeve, mirrored about24. Bounds (6,6)-(42,42).
Construction: Lucide star five-point silhouette with coherent corners; source mounting sleeve.
Reduction: Three rays; mounting sleeve reduced to a stem stroke to preserve the five-point star.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '897c015d-700f-47cf-9c50-a63d4650bab6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/tree top star_897c015d-700f-47cf-9c50-a63d4650bab6.svg'
AUTHOR = 'gpt-6'


class IconShiningStarTreeTopper(Solo48):
    icon_id = 'shining-star-tree-topper'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('shining', 'star', 'tree', 'topper')

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
        path('star',(24,14),[('L',(29,23)),('L',(38,24)),('L',(31,31)),('L',(33,40)),('L',(24,35)),('L',(15,40)),('L',(17,31)),('L',(10,24)),('L',(19,23)),('L',(24,14))],True)
        self.add_line('mount',(24,35),(24,42));self.relate('connect','mount','star')
        self.add_line('ray-top',(24,6),(24,6));self.add_line('ray-left',(6,12),(8,14));self.add_line('ray-right',(42,12),(40,14))
