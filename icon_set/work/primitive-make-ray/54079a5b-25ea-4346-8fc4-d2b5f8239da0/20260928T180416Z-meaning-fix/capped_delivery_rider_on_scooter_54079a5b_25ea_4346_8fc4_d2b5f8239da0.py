"""Restore the capped head, bent riding arm and leg, rounded scooter shell, parcel box and two open wheels.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The rider became a disconnected head over an angular frame; the seated posture and scooter body were lost.
Construction: car + human_ref/full_body_ref.png.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '54079a5b-25ea-4346-8fc4-d2b5f8239da0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__capped-delivery-rider-on-scooter/20260928T175901Z-thuan-mac/reference/delivery person motorcycle_54079a5b-25ea-4346-8fc4-d2b5f8239da0.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'capped-delivery-rider-on-scooter'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('delivery', 'person', 'motorcycle')

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

        circle('head',26,8,4);line('cap-brim',(23,7),(34,7))
        line('torso',(26,20),(25,28))
        poly('arm',(26,20),(34,24),(38,24));join('torso','arm')
        poly('leg',(25,28),(31,30),(31,36));join('torso','leg')
        rounded('parcel',5,18,17,28,2)
        path('scooter',(4,35),[C((13,31),(4,32),(7,31)),L((25,31)),L((27,37)),L((38,37)),L((39,28))])
        line('steering',(38,24),(41,35))
        circle('wheel-back',11,40,4);circle('wheel-front',41,40,4)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
