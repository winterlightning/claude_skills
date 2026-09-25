"""Seated right-facing badger: smooth back, small round ear, pointed muzzle, concave chest and two feet. No useful exact local Lucide match. Shared tangents govern silhouette; preserve natural directional asymmetry. Omit tiny eye, restore leg crease.
Reviewer: clean centerlines and consistent stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "5bb2d73b-f3a4-43fd-add6-fac9786654ae"
SOURCE_PATH = "pictographic-primitives/_uncategorized_05/badger_5bb2d73b-f3a4-43fd-add6-fac9786654ae.svg"
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='seated-badger-in-right-profile'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="Uncategorized"
    aliases=()
    keywords=('seated', 'badger', 'in', 'right', 'profile')

    def build(self):
        self.add_polyline('rear-foot',(22,40),(18,40),(10,40))
        self.add_arc('rump',(10,40),(4,32),radius_x=6,radius_y=8)
        self.add_bezier('back',(4,32),((4,24),(10,18),(18,18)),((22,18),(26,16),(26,12)))
        self.add_arc('ear',(26,12),(34,12),radius_x=4)
        self.add_bezier('muzzle',(34,12),((34,16),(40,20),(44,22)))
        self.add_bezier('jaw',(44,22),((42,26),(38,26),(34,26)),((28,26),(26,30),(26,34)))
        self.add_arc('chest',(26,34),(32,40),radius_x=6,sweep=False)
        self.add_line('front-foot',(32,40),(36,40))
        self.contours.clear()
        self.add_contour('body','rear-foot-1','rear-foot-2','rump','back','ear','muzzle','jaw','chest','front-foot')
        self.add_line('hind-leg',(18,30),(18,40));self.relate('connect','hind-leg','body')

    def path(self, name, start, steps, closed=False):
        members=[]; here=start
        for j,step in enumerate(steps):
            eid=f'{name}-{j}'
            if len(step)==2:
                self.add_line(eid,here,step); end=step
            else:
                end,rx,ry,sweep=step
                self.add_arc(eid,here,end,radius_x=rx,radius_y=ry,sweep=sweep)
            members.append(eid);here=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)

