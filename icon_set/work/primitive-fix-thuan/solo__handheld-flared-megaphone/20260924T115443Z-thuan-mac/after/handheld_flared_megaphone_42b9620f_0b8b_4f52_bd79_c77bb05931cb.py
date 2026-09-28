"""Flared megaphone with a rounded rear chamber, broad mouth rim and angled handgrip. Extrema 4,8,44,40.
Construction: megaphone: continuous horn and attached grip
Reduction: Small driver cap behind the mouth omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='42b9620f-0b8b-4f52-bd79-c77bb05931cb'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__handheld-flared-megaphone/20260924T115443Z-thuan-mac/reference/bullhorn_42b9620f-0b8b-4f52-bd79-c77bb05931cb.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='handheld-flared-megaphone'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('handheld', 'flared', 'megaphone')
    def build(self):

        def path(name,start,steps,closed=False):
            here=start;members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
                else:self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m);here=end
            self.add_contour(name,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*pts,closed=False):self.add_polyline(n,*pts,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('rear',(8,16),[('L',(16,16)),('L',(16,28)),('L',(8,28)),('A',(4,24),4,4,True),('L',(4,20)),('A',(8,16),4,4,True)],True)
        poly('horn',(16,16),(36,8),(36,32),(16,28));join('horn','rear')
        poly('rim',(36,8),(44,8),(44,32),(36,32));join('rim','horn')
        poly('grip',(8,28),(11,40),(21,40),(16,28));join('grip','rear');join('grip','horn')
