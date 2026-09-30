"""The rejected head was a plain diamond and lacked the reference striking caps. Rebuilt the diagonal gavel with projecting caps and a long handle above the sound block.
Plan: Lucide gavel: projecting end bars and diagonal handle. Keyshape SQUARE; shared contour nodes and dimensions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='e6835953-23ed-4f5c-913e-f32e21b6a5c4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__judge-gavel-above-small-sound-block/20260929T110722Z-thuan-mac/reference/mallet_e6835953-23ed-4f5c-913e-f32e21b6a5c4.svg'
AUTHOR="gpt-6"
class Drawing(Solo48):
    icon_id='judge-gavel-above-small-sound-block'
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

        poly('head',(18,14),(26,6),(42,22),(34,30),(26,22),(18,14))
        poly('cap-upper',(22,6),(26,6),(42,22),(42,26))
        poly('cap-lower',(14,14),(18,14),(34,30),(34,34))
        join('head','cap-upper');join('head','cap-lower')
        line('handle',(26,22),(6,42));join('handle','head');join('handle','cap-lower')
        line('block',(28,42),(42,42))
