"""Restore three outlined skewed bars with alternating slant and staggered outer chevrons, preserving the source logo arrangement.
Reference comparison: The rejected emblem replaced three long outlined parallelograms with short dashes and aligned brackets incorrectly. Feedback asks to recover the original emblem.
Construction references: No useful Lucide logo match; supplied PureScript emblem controls the composition.
Omissions: No defining features omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '423ee93e-e3bf-4a17-8d43-6193ba22aba2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__purescript-chevron-emblem/20260929T051531Z-thuan-mac/reference/purescript logo_423ee93e-e3bf-4a17-8d43-6193ba22aba2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'purescript-chevron-emblem'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def path(self, name, start, *steps, closed=False):
        ids=[]; p=start
        for n,step in enumerate(steps):
            key=f"{name}-{n}"; end=step[1]
            if step[0]=='L': self.add_line(key,p,end)
            elif step[0]=='C': self.add_bezier(key,p,(step[2],step[3],end))
            else: self.add_arc(key,p,end,radius_x=step[2],radius_y=step[3],sweep=step[4],large_arc=step[5] if len(step)>5 else False)
            ids.append(key);p=end
        if closed and p!=start:
            key=f"{name}-close";self.add_line(key,p,start);ids.append(key)
        self.add_contour(name,*ids,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True),closed=True)

    def build(self):
        # Three equal-height outlined parallelogram bars alternate slant; brackets have the reference vertical stagger.
        self.add_polyline('left-bracket',(12,19),(4,27),(12,35))
        self.add_polyline('right-bracket',(36,7),(44,15),(36,23))
        self.add_polyline('bar-top',(15,9),(31,9),(35,14),(19,14),closed=True)
        self.add_polyline('bar-middle',(16,21),(32,21),(28,26),(12,26),closed=True)
        self.add_polyline('bar-bottom',(16,33),(32,33),(36,38),(20,38),closed=True)

Drawing.exception = {'reason': 'The emblem requires narrow outlined bands and compact staggered brackets; 4px strokes retain visible bar openings under user-authorized logo exception.', 'approved_by': 'user', 'approved_on': '2026-09-29', 'svg_sha256': 'b762d15be73d878f59551d3d08cf00e0361ca70b26e1bba4fe36d937a985d212'}
