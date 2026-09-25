"""Enlarge the tape hub and lower the cutter deck so the dispenser reads as a roll on a weighted base.
Plan: named coherent contours; repeated elements share parameters.
Keyshape: HRECT_L for the subject's natural orientation.
Construction: No useful exact Lucide tape match; concentric roll and hub with a stepped connected housing.
Reduction: Fine cutting teeth omitted; roll, open hub and cutter deck retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '21247aa3-cf95-5bbc-8785-366de4dab5a7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__desktop-tape-dispenser/20260925T083122Z-thuan-mac/reference/office tape_21247aa3-cf95-5bbc-8785-366de4dab5a7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'desktop-tape-dispenser'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('office', 'tape')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=3):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        # Radius 13 roll and radius 5 hub give exactly 4px ink clearance analytically.
        path('roll',(6,21),[('A',(19,8),13,13,True),('A',(32,21),13,13,True),('A',(31,26),13,13,True),('A',(19,34),13,13,True),('A',(7,26),13,13,True),('A',(6,21),13,13,True)],True)
        circle('hub',19,21,5)
        poly('body',(7,26),(4,26),(4,42),(44,42),(44,26),(31,26));join('body','roll')
