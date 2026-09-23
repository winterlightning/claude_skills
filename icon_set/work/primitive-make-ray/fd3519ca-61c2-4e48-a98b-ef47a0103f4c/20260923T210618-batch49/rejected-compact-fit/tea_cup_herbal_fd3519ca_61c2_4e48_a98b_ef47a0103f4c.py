"""Tea cup herbal, drawn from its complete supplied reference.
Symbol plan: preserve the subject, nested symbols, repeats and intentional overlaps.
Each repeated part and rounded rectangle owns its parameters and attachment nodes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='fd3519ca-61c2-4e48-a98b-ef47a0103f4c'
SOURCE_PATH='icon_set/work/todo-references/tea cup herbal_fd3519ca-61c2-4e48-a98b-ef47a0103f4c.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tea-cup-herbal'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('tea', 'cup', 'herbal')

    # Keyshape visible extremes: (2, 8, 46, 40); centerline extremes: (4, 10, 44, 38).
    def build(self):
        # Bowl-shaped cup, open handle, saucer line and complete leaf emblem.
        # HRECT_M centerlines (4,10)-(44,38).
        self.add_line('rim-1',(6,20),(6,10))
        self.add_line('rim-2',(6,10),(34,10))
        self.add_line('rim-3',(34,10),(34,12))
        self.add_line('rim-4',(34,12),(34,22))
        self.add_arc('bowl-right',(34,22),(20,38),radius_x=14,radius_y=16)
        self.add_arc('bowl-left',(20,38),(6,20),radius_x=14,radius_y=18)
        self.add_contour('cup','rim-1','rim-2','rim-3','rim-4','bowl-right','bowl-left',closed=True)
        self.path('handle',(34,12),[('L',(39,12)),('A',(44,17),5),('A',(39,22),5),('L',(34,22))])
        self.relate('connect','cup','handle')
        self.add_polyline('saucer',(4,38),(20,38),(36,38))
        self.relate('connect','cup','saucer')
        self.add_bezier('leaf-upper',(17,27),((16,22),(21,19),(25,19)))
        self.add_bezier('leaf-lower',(25,19),((25,24),(22,27),(17,27)))
        self.add_contour('leaf','leaf-upper','leaf-lower',closed=True)
        self.add_line('leaf-stem',(17,27),(22,22))
        self.relate('connect','leaf','leaf-stem')


    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)

    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        # One rounded rectangle owns paired radii, extents, and connection splits.
        seg=[('L',(x,t)) for x in sorted(set(top)) if l+k<x<r-k]
        seg += [('L',(r-k,t)),('A',(r,t+k),k)]
        seg += [('L',(r,y)) for y in sorted(set(right)) if t+k<y<b-k]
        seg += [('L',(r,b-k)),('A',(r-k,b),k)]
        seg += [('L',(x,b)) for x in sorted(set(bottom),reverse=True) if l+k<x<r-k]
        seg += [('L',(l+k,b)),('A',(l,b-k),k)]
        seg += [('L',(l,y)) for y in sorted(set(left),reverse=True) if t+k<y<b-k]
        seg += [('L',(l,t+k)),('A',(l+k,t),k)]
        self.path(n,(l+k,t),seg,True)

    def suitcase(self):
        # SQUARE: ink (4,4)-(44,44); centerlines (6,6)-(42,42).
        self.rect('case',6,14,42,42,4,top=(16,32))
        self.path('handle',(16,14),[('L',(16,10)),('A',(20,6),4),
            ('L',(28,6)),('A',(32,10),4),('L',(32,14))])
        self.relate('connect','case','handle')

    def check(self,n,x,y):
        self.add_polyline(n,(x,y),(x+3,y+3),(x+9,y-3))

