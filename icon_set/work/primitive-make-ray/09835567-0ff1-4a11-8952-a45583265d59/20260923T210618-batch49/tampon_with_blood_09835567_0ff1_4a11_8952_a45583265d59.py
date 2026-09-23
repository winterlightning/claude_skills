"""Tampon with blood, drawn from its complete supplied reference.
Symbol plan: preserve the subject, nested symbols, repeats and intentional overlaps.
Each repeated part and rounded rectangle owns its parameters and attachment nodes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='09835567-0ff1-4a11-8952-a45583265d59'
SOURCE_PATH='icon_set/work/todo-references/tampon with blood_09835567-0ff1-4a11-8952-a45583265d59.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tampon-with-blood'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('tampon', 'with', 'blood')

    # Keyshape visible extremes: (4, 4, 44, 44); centerline extremes: (6, 6, 42, 42).
    def build(self):
        # Diagonal tampon, lower connector, trailing string and separate blood drop.
        self.add_line('body-left',(14,22),(26,10))
        self.add_bezier('cap-left',(26,10),((28,8),(28,6),(30,6)))
        self.add_bezier('cap-right',(30,6),((36,6),(37,12),(33,16)))
        self.add_line('body-right',(33,16),(21,28))
        self.add_bezier('body-end',(21,28),((19,30),(12,24),(14,22)))
        self.add_contour('tampon','body-left','cap-left','cap-right','body-right','body-end',closed=True)
        self.add_polyline('connector',(14,22),(10,27),(13,30),(18,27))
        self.relate('connect','tampon','connector')
        self.add_bezier('string',(10,27),((4,32),(10,37),(6,42)))
        self.relate('connect','connector','string')
        self.add_bezier('drop-right',(37,25),((40,29),(42,33),(42,36)),((42,42),(30,42),(30,36)))
        self.add_bezier('drop-left',(30,36),((30,32),(34,28),(37,25)))
        self.add_contour('blood-drop','drop-right','drop-left',closed=True)


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

