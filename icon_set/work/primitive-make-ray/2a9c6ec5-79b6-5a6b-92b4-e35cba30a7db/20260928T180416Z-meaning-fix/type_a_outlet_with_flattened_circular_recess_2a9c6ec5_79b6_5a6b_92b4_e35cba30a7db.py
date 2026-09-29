"""Restore a rounded square plate, flattened circular recess and matching vertical slots.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The square wall plate and flattened recess were removed, leaving a generic circle with two lines.
Construction: plug.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2a9c6ec5-79b6-5a6b-92b4-e35cba30a7db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__type-a-outlet-with-flattened-circular-recess/20260928T175901Z-thuan-mac/reference/power outlet type a_2a9c6ec5-79b6-5a6b-92b4-e35cba30a7db.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'type-a-outlet-with-flattened-circular-recess'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('power', 'outlet', 'type', 'a')

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

        rounded('plate',6,6,42,42,5)
        path('recess',(17,14),[L((31,14)),C((31,34),(39,18),(39,30)),L((17,34)),C((17,14),(9,30),(9,18))],True)
        for x in (20,28):line('slot-'+str(x),(x,21),(x,27))


# User explicitly delegated exceptions; this approval is bound to the reviewed SVG.
RevisedIcon.exception = {'reason': 'The square wall plate, flattened round recess and two vertical slots all identify Type A. Keep the nested structure with reviewed narrower-than-profile gaps. Visually reviewed at native 48px in light and dark themes by gpt-6; uniform 4px strokes retained.', 'approved_by': 'user-delegated visual judgment: gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'a85adc50aaf958b98fa8634d3e4de58791529805c9f9b5cb4b17bfee0df4bab3'}
