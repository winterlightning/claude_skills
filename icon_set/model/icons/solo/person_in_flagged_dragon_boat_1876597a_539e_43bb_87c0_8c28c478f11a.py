"""Person in Flagged Dragon Boat.

Plan: Dragon prow, passenger, flag and deep hull; centerlines (4,8)-(44,40).
Construction: Lucide sailboat rounded hull and human_ref detached circular head.
Reduction: Omitted eye and repeated waves; widened flag and hull openings.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '1876597a-539e-43bb-87c0-8c28c478f11a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/dragon boat festival person_1876597a-539e-43bb-87c0-8c28c478f11a.svg'
AUTHOR = 'gpt-6'


class IconPersonInFlaggedDragonBoat(Solo48):
    icon_id = 'person-in-flagged-dragon-boat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    aliases = ()
    keywords = ('person', 'in', 'flagged', 'dragon', 'boat')

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
        path('boat',(4,20),[('L',(10,20)),('L',(12,14)),('L',(14,24)),('C',(23,28),(15,28),(18,28)),('L',(24,28)),('L',(36,28)),('C',(44,26),(40,28),(44,29)),('C',(30,40),(44,40),(38,40)),('L',(20,40)),('C',(4,28),(10,40),(4,34)),('L',(4,20))],True)
        circle('head',24,12,3)
        self.add_line('torso',(24,23),(24,28));self.relate('connect','torso','boat');self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
        path('flag',(36,28),[('L',(36,16)),('L',(36,8)),('L',(44,8)),('L',(44,16)),('L',(36,16))]);self.relate('connect','flag','boat')
