"""A hook-handled serving ladle with deep bowl and two broad draped noodles. Envelope (6,6)-(42,42); shared noodle radius4.
Construction reference: Lucide utensils: rounded tool and coherent long handle.
Omissions: Three tiny noodle loops reduced to two."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='99c119c2-76a1-44f5-ac3b-6ec9c7fbf6b4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__spaghetti-serving-ladle/20260924T100518Z-thuan-mac/reference/ladle spaghetti_99c119c2-76a1-44f5-ac3b-6ec9c7fbf6b4.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='spaghetti-serving-ladle'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('ladle', 'spaghetti')
    def build(self):

        def path(name,start,commands,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('handle',(6,12),[('A',(18,12),6,6,True),('L',(18,26))])
        path('bowl',(18,26),[('L',(26,26)),('L',(34,26)),('L',(42,26)),('A',(30,38),12,12,True),('A',(18,26),12,12,True)],True);join('handle','bowl')
        path('noodle-a',(26,42),[('L',(26,22)),('A',(34,22),4,4,True),('L',(34,32))]);join('noodle-a','bowl')
        path('noodle-b',(34,22),[('A',(42,22),4,4,True),('L',(42,26))]);join('noodle-b','noodle-a');join('noodle-b','bowl')
