"""Use a taller paired-lobe outline and two short inward folds while retaining an undivided centre.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The flattened scalloped outline read as a cloud or flower, with no anatomical folds.
Construction: brain.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '505cc1d4-dec0-4492-aadd-1c3ba0a9d545'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__brain-with-undivided-centre/20260928T175901Z-thuan-mac/reference/brain 1_505cc1d4-dec0-4492-aadd-1c3ba0a9d545.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'brain-with-undivided-centre'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('brain', '1')

    def build(self):

        def path(name,start,commands,closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(commands):
                if end==here and kind=='L':continue
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A':self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C':self.add_bezier(ident,here,(a[0],a[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        L=lambda end:('L',end)
        C=lambda end,c1,c2:('C',end,c1,c2)
        A=lambda end,rx,ry,sweep:('A',end,rx,ry,sweep)
        line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        for side in (-1,1):
         p=lambda x,y:(24+side*x,y)
         path('lobe-'+str(side),p(0,11),[C(p(8,6),p(2,4),p(7,4)),C(p(13,13),p(12,6),p(14,9)),C(p(18,23),p(20,13),p(21,19)),C(p(17,33),p(22,27),p(21,32)),C(p(9,41),p(20,39),p(15,44)),C(p(0,38),p(4,44),p(1,43))])
         path('fold-'+str(side),p(13,13),[C(p(10,19),p(14,16),p(12,19))]);join('lobe-'+str(side),'fold-'+str(side))
        join('lobe--1','lobe-1')


# User explicitly delegated exceptions; this approval is bound to the reviewed SVG.
RevisedIcon.exception = {'reason': 'Use the natural rounded brain perimeter instead of flattening its lobes to the keyshape. Two inward folds clarify the brain without dividing the centre. Visually reviewed at native 48px in light and dark themes by gpt-6; uniform 4px strokes retained.', 'approved_by': 'user-delegated visual judgment: gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'aa2b5bc9556f9534acc7f2252984d388c665cd1612bb09817fcaa25f4ca95f49'}
