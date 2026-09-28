"""Certificate with lower-right round seal and single notched ribbon; extremes 6,6,42,42.
Construction: award: round seal with hanging notched ribbon
Reduction: One of two text rules omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '4ed91796-017e-538d-8c4d-6f874608ce4f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__certificate-ribbon-seal/20260924T111346Z-thuan-mac/reference/certified diploma_4ed91796-017e-538d-8c4d-6f874608ce4f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'certificate-ribbon-seal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('certificate', 'ribbon', 'seal')
    def build(self):

        def path(name, start, steps, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{name}-{j}'
                if kind=='L': self.add_line(m,here,end)
                else: self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2],large_arc=args[3] if len(args)>3 else False)
                members.append(m); here=end
            self.add_contour(name,*members,closed=closed)
        def poly(name,*pts,closed=False): self.add_polyline(name,*pts,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)

        poly('paper',(26,32),(6,32),(6,6),(42,6),(42,24))
        circle('seal',34,24,8);join('paper','seal')
        poly('ribbon',(26,24),(26,42),(34,38),(42,42),(42,24));join('ribbon','seal')
        line('text',(15,15),(19,15))
