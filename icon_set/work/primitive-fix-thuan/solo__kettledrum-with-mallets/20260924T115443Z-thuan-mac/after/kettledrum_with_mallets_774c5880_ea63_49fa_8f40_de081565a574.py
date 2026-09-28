"""Kettledrum with an elliptical bowl, three splayed supports and two sloping mallets. Extrema 4,8,44,40.
Construction: drum: smooth elliptical body and diagonal mallets
Reduction: Drumhead rear ellipse omitted for spacing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='774c5880-ea63-49fa-8f40-de081565a574'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__kettledrum-with-mallets/20260924T115443Z-thuan-mac/reference/kettledrum_774c5880-ea63-49fa-8f40-de081565a574.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='kettledrum-with-mallets'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('kettledrum', 'with', 'mallets')
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

        path('bowl',(4,23),[('L',(44,23)),('A',(36,31),20,10,True),('A',(24,33),20,10,True),('A',(12,31),20,10,True),('A',(4,23),20,10,True)],True)
        for n,a,b in [('left',(12,31),(9,40)),('centre',(24,33),(24,40)),('right',(36,31),(39,40))]:line('leg-'+n,a,b);join('leg-'+n,'bowl')
        circle('mallet-left',14,11,3);circle('mallet-right',34,11,3)
        line('handle-left',(4,8),(11,11));line('handle-right',(44,8),(37,11));join('handle-left','mallet-left');join('handle-right','mallet-right')
