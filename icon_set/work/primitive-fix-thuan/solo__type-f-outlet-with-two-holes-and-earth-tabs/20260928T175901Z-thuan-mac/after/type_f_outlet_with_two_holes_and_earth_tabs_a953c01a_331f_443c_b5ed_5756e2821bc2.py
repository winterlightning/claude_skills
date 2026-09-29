"""Restore the square wall plate and two circular pin openings inside the grounded round recess.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The wall plate disappeared and the pin holes were rendered as filled dots.
Construction: plug.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a953c01a-331f-443c-b5ed-5756e2821bc2'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__type-f-outlet-with-two-holes-and-earth-tabs/20260928T175901Z-thuan-mac/reference/power outlet type f_a953c01a-331f-443c-b5ed-5756e2821bc2.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'type-f-outlet-with-two-holes-and-earth-tabs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('power', 'outlet', 'type', 'f')

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

        rounded('plate',4,4,44,44,5)
        circle('recess',24,24,14)
        circle('pin-left',18,24,3);circle('pin-right',30,24,3)
        line('earth-top',(24,10),(24,15));line('earth-bottom',(24,33),(24,38))


# User explicitly delegated exceptions; this approval is bound to the reviewed SVG.
RevisedIcon.exception = {'reason': 'The square plate, circular recess, open pin holes and upper/lower earth tabs identify Type F. Preserve these layers and small round apertures with compact but visible gaps. Visually reviewed at native 48px in light and dark themes by gpt-6; uniform 4px strokes retained.', 'approved_by': 'user-delegated visual judgment: gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': 'd7afc1106fb8d7328ed1196ba24b15be3b986fefa361407be2e21f950b3a76e0'}
