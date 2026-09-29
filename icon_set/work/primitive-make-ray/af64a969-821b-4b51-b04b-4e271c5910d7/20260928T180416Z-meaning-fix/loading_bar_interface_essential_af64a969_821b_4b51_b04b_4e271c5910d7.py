"""Restore the long horizontal capsule proportions and a diagonal progress boundary.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The progress bar was nearly square, so it read as a prohibition or capsule symbol.
Construction: No useful exact Lucide match; rounded enclosure construction from panel-top..
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'af64a969-821b-4b51-b04b-4e271c5910d7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__loading-bar-interface-essential/20260928T175901Z-thuan-mac/reference/loading bar_af64a969-821b-4b51-b04b-4e271c5910d7.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'loading-bar-interface-essential'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('loading', 'bar')

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

        path('capsule',(12,16),[L((29,16)),L((36,16)),A((36,32),8,8,True),L((19,32)),L((12,32)),A((12,16),8,8,True)],True)
        line('progress',(29,16),(19,32));join('capsule','progress')


# User explicitly delegated exceptions; this approval is bound to the reviewed SVG.
RevisedIcon.exception = {'reason': 'A loading bar needs a slim horizontal capsule. Its reviewed 44x20 ink envelope preserves the source meaning; the standard HRECT_M height made the rejected drawing too squat. Visually reviewed at native 48px in light and dark themes by gpt-6; uniform 4px strokes retained.', 'approved_by': 'user-delegated visual judgment: gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '2f3a9974153de4661d3e743e971508ca696a0669f07d64912ec877cd78854dee'}
