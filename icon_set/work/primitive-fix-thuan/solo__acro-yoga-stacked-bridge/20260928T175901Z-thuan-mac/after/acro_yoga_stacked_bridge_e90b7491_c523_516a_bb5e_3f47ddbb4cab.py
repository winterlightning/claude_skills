"""Restore two detached heads, a shallow upper bridge, an arm and two lower supports.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The heads were attached to the limbs; the upper pose became a tall arch with no supporting arm.
Construction: human_ref/full_body_ref.png.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e90b7491-c523-516a-bb5e-3f47ddbb4cab'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__acro-yoga-stacked-bridge/20260928T175901Z-thuan-mac/reference/acro yoga pose_e90b7491-c523-516a-bb5e-3f47ddbb4cab.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'acro-yoga-stacked-bridge'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('acro', 'yoga', 'pose')

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

        circle('upper-head',10,13,4)
        circle('lower-head',10,31,4)
        path('upper-torso',(22,13),[C((31,6),(22,6),(27,6)),C((42,13),(36,6),(42,9))])
        line('upper-arm',(22,13),(22,23));join('upper-arm','upper-torso')
        line('upper-leg',(42,13),(42,31));join('upper-leg','upper-torso')
        line('lower-torso',(22,31),(42,31))
        line('lower-arm',(22,31),(22,42));join('lower-arm','lower-torso')
        line('lower-leg',(42,31),(42,42));join('lower-leg','lower-torso')
        join('upper-leg','lower-torso');join('upper-leg','lower-leg')
        self.mark_human_figure('upper',head='upper-head',torso='upper-torso-0',torso_junction='start')
        self.mark_human_figure('lower',head='lower-head',torso='lower-torso',torso_junction='start')
