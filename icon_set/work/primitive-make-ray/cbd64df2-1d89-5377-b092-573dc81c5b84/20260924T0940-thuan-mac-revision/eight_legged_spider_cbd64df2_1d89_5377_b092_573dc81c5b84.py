"""Eight curved mirrored legs and distinct round head and abdomen.
Plan: named coherent contours; paired features derive from shared parameters.
Reference: supplied original plus rejected production SVG.
Lucide: dog (rounded animal contours), pipette (coherent diagonal tool construction).
Human parts: human_ref/full_body_ref.png; no detached human head in these subjects.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cbd64df2-1d89-5377-b092-573dc81c5b84'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__eight-legged-spider/20260924T093128Z-thuan-mac/reference/halloween spider_cbd64df2-1d89-5377-b092-573dc81c5b84.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='eight-legged-spider'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('halloween spider',)
    def build(self):
        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                k,end,*args=c; name=f'{n}-{j}'
                if k=='L': self.add_line(name,here,end)
                elif k=='A': self.add_arc(name,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif k=='C': self.add_bezier(name,here,(args[0],args[1],end))
                here=end; members.append(name)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        circle('head',24,16,8)
        path('abdomen',(24,24),[('A',(24,40),8,8,True),('A',(24,24),8,8,True)],True)
        join('head','abdomen')
        for s in (-1,1):
         def p(x,y):return (24+s*x,y)
         for j,(start,end,c1,c2) in enumerate([(p(8,16),p(12,8),p(12,16),p(12,12)),(p(8,16),p(20,16),p(14,19),p(18,19)),(p(8,32),p(20,32),p(14,29),p(18,29)),(p(8,32),p(12,40),p(12,32),p(12,36))]):
          path(f'leg-{s}-{j}',start,[('C',end,c1,c2)]);join(f'leg-{s}-{j}','head' if j<2 else 'abdomen')
         for a,b in [(0,1),(2,3)]:join(f'leg-{s}-{a}',f'leg-{s}-{b}')
