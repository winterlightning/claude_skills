"""The 1 and 9 both have a 12-unit centerline height and the same 4-unit stroke. The 9 has a compact loop and straight descending stem.
Reference: Local Lucide arrow-down-0-1; user requested equal numeral size
Authored directly on SOLO48, with prior revision preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '774a187b-a625-438b-9b84-1427193ca713'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/arrange number_774a187b-a625-438b-9b84-1427193ca713.svg'
AUTHOR = 'gpt-6'

class ArrangeNumber(Solo48):
    icon_id = 'arrange-number'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ()
    keywords = ('arrange', 'number')

    def build(self):
        # Symbol plan: The 1 and 9 both have a 12-unit centerline height and the same 4-unit stroke. The 9 has a compact loop and straight descending stem.

        def path(n,start,commands,closed=False):
            here=start;members=[]
            for j,c in enumerate(commands):
                kind,end,*a=c;ident=f'{n}-{j}'
                if kind=='L':self.add_line(ident,here,end)
                elif kind=='A':self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C':self.add_bezier(ident,here,(a[0],a[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        poly('arrow',(8,36),(14,44),(20,36));line('shaft',(14,4),(14,44));join('shaft','arrow')
        poly('one',(32,10),(36,6),(36,18))
        path('nine',(40,32),[('A',(32,32),4,4,False),('A',(40,32),4,4,False),('L',(40,40))])
