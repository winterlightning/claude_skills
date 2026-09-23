"""Sync location, drawn from its complete supplied reference.
Symbol plan: preserve the subject, nested symbols, repeats and intentional overlaps.
Each repeated part and rounded rectangle owns its parameters and attachment nodes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b62fe36e-70fb-47b1-b517-27cad2a2b72b'
SOURCE_PATH='icon_set/work/todo-references/sync location_b62fe36e-70fb-47b1-b517-27cad2a2b72b.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='sync-location'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('sync', 'location')

    def build(self):
        # Pin above a split orbit, with the lower-left orbit ending in an arrow.
        self.add_arc('pin-crown',(12,18),(36,18),radius_x=12)
        self.add_bezier('pin-right',(36,18),((36,22),(28,32),(24,35)))
        self.add_bezier('pin-left',(24,35),((20,32),(12,22),(12,18)))
        self.add_contour('pin','pin-crown','pin-right','pin-left',closed=True)
        self.circle('pin-center',24,18,3)
        self.add_bezier('orbit-left-top',(10,29),((7,30),(6,32),(6,34)))
        self.add_arc('orbit-left-bottom',(6,34),(24,42),radius_x=18,radius_y=8,sweep=False)
        self.add_contour('orbit-left','orbit-left-top','orbit-left-bottom')
        self.add_polyline('orbit-arrow',(20,38),(24,42),(20,46))
        self.relate('connect','orbit-left','orbit-arrow')
        self.add_bezier('orbit-right-top',(38,29),((41,30),(42,32),(42,34)))
        self.add_arc('orbit-right-bottom',(42,34),(30,42),radius_x=18,radius_y=8)
        self.add_contour('orbit-right','orbit-right-top','orbit-right-bottom')


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

