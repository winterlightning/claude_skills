"""A diagonal wood saw with a rounded closed handle and circular grip aperture. Bounds (6,6)-(42,42); broad blade has two smooth tooth scallops.
Construction reference: Lucide wrench: diagonal tool balance; source waved blade and handle opening.
Omissions: Small oblong handle opening simplified to a circular aperture; fine teeth reduced to two scallops."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='cca0b3cb-f738-5bd1-a400-e64072c4b7b1'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__wavy-tooth-wood-saw/20260924T101756Z-thuan-mac/reference/tools wood saw_cca0b3cb-f738-5bd1-a400-e64072c4b7b1.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='wavy-tooth-wood-saw'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('tools', 'wood', 'saw')
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
        path('handle',(10,24),[('L',(17,21)),('L',(26,30)),('L',(24,38)),('A',(20,42),4,4,True),('L',(17,42)),('C',(6,31),(13,42),(6,35)),('L',(6,28)),('A',(10,24),4,4,True)],True)
        path('blade',(17,21),[('L',(34,6)),('L',(42,13)),('L',(38,16)),('C',(34,22),(38,20),(38,22)),('C',(30,28),(34,26),(34,28)),('L',(26,30))]);join('blade','handle')
        path('opening',(14,28),[('L',(19,33)),('L',(16,36)),('L',(11,31)),('L',(14,28))],True)
