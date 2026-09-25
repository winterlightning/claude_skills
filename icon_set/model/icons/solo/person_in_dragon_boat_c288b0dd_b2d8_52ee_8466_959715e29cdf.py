"""Person in Dragon Boat.

Plan: Left dragon prow and seated passenger over deep hull; centerlines (6,6)-(42,42).
Construction: Lucide sailboat rounded hull and human_ref detached circular head.
Reduction: Omitted eye and wave decoration; silhouette retains snout and crest.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'c288b0dd-b2d8-52ee-8466-959715e29cdf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/dragon boat festival_c288b0dd-b2d8-52ee-8466-959715e29cdf.svg'
AUTHOR = 'gpt-6'


class IconPersonInDragonBoat(Solo48):
    icon_id = 'person-in-dragon-boat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('person', 'in', 'dragon', 'boat')

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
        path('boat',(6,20),[('L',(6,16)),('L',(14,16)),('L',(18,10)),('L',(18,24)),('A',(26,32),8,8,False),('L',(31,32)),('L',(34,32)),('C',(42,24),(39,32),(42,30)),('C',(30,42),(42,38),(37,42)),('L',(22,42)),('C',(10,24),(12,42),(10,32)),('L',(6,24)),('L',(6,20))],True)
        circle('head',31,10,4)
        self.add_line('torso',(31,22),(31,32));self.relate('connect','torso','boat')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
