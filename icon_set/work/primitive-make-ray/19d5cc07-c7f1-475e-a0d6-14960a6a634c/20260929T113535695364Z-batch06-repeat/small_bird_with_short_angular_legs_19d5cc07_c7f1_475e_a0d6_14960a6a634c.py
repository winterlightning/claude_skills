"""The rejected bird had a flat belly, long rigid legs and a tiny hooked wing. Rounded the belly, shortened and bent the legs, and broadened the folded wing into a smooth curve. Omitted the tiny eye.
Plan: Lucide bird: rounded body and flowing folded-wing curve. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='19d5cc07-c7f1-475e-a0d6-14960a6a634c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__small-bird-with-short-angular-legs/20260929T112716Z-thuan-mac/reference/eaglet_19d5cc07-c7f1-475e-a0d6-14960a6a634c.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='small-bird-with-short-angular-legs'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="primitives-generate"
    def build(self):

        def path(name,start,steps,closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                member=f'{name}-{j}'
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                members.append(member);here=end
            self.add_contour(name,*members,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*pts): self.add_polyline(name,*pts)
        def join(a,b): self.relate('connect',a,b)
        def circle(name,x,y,r): path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

        path('bird',(6,15),[('L',(12,11)),('C',(21,6),(13,8),(17,6)),('C',(30,15),(27,6),(30,9)),('C',(42,27),(36,19),(42,20)),('C',(32,34),(42,32),(36,34)),('C',(18,34),(28,36),(22,36)),('C',(10,23),(12,33),(10,29)),('L',(10,18)),('L',(6,15))],True)
        path('wing',(20,20),[('C',(30,25),(20,25),(26,25))])
        poly('leg-left',(18,34),(18,40),(14,42));poly('leg-right',(32,34),(32,40),(28,42));join('leg-left','bird');join('leg-right','bird')
