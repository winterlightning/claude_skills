"""Wooden Barrel.

Plan: Barrel with bulging mirrored sides and two hoop boundaries. Bounds (8,4)-(40,44).
Construction: Lucide barrel bulging silhouette and shared hoop levels.
Reduction: Single hoop boundary strokes replace narrow hoop bands; central staves stay blank.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'ad44b98b-daa8-4c39-8848-ed9ef090531c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/vaisakhi_ad44b98b-daa8-4c39-8848-ed9ef090531c.svg'
AUTHOR = 'gpt-6'


class IconWoodenBarrel(Solo48):
    icon_id = 'wooden-barrel'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'holidays'
    aliases = ()
    keywords = ('wooden', 'barrel')

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
        path('barrel',(12,4),[('L',(36,4)),('C',(39,14),(37,7),(38,10)),('C',(40,24),(40,18),(40,21)),('C',(39,34),(40,27),(40,30)),('C',(36,44),(38,38),(37,41)),('L',(12,44)),('C',(9,34),(11,41),(10,38)),('C',(8,24),(8,30),(8,27)),('C',(9,14),(8,21),(8,18)),('C',(12,4),(10,10),(11,7))],True)
        for y in [14,34]:self.add_line('hoop'+str(y),(9,y),(39,y));self.relate('connect','hoop'+str(y),'barrel')
