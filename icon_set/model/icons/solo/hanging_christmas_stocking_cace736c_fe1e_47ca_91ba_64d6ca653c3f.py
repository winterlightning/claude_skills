"""Hanging Christmas Stocking.

Plan: Slanted stocking shaft, leftward rounded foot and hanging line. Bounds (8,4)-(40,44).
Construction: Source stocking silhouette and curved toe seam; no useful exact Lucide stocking match.
Reduction: Removed toe and heel seams to leave the rounded foot and ankle open.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'cace736c-fe1e-47ca-91ba-64d6ca653c3f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/holidays/sock_cace736c-fe1e-47ca-91ba-64d6ca653c3f.svg'
AUTHOR = 'gpt-6'


class IconHangingChristmasStocking(Solo48):
    icon_id = 'hanging-christmas-stocking'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "holidays"
    categories = ("primitives", "holidays")
    aliases = ()
    keywords = ('hanging', 'christmas', 'stocking')

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
        path('stocking',(20,12),[('L',(40,8)),('L',(40,30)),('A',(26,44),14,14,True),('L',(18,44)),('A',(8,34),10,10,True),('C',(24,28),(8,27),(22,32)),('L',(20,12))],True)
        self.add_line('hanger',(40,8),(40,4));self.relate('connect','hanger','stocking')
        # The rounded toe is kept unsegmented so it remains generous and smooth.
