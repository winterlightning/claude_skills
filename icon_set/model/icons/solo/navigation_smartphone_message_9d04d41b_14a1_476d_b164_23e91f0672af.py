"""A location-message bubble overlaps a smartphone.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 SQUARE; omissions: Small home-button tick omitted; phone divider retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='9d04d41b-14a1-476d-b164-23e91f0672af'
SOURCE_PATH='icon_set/work/todo-references/navigation smartphone message_9d04d41b-14a1-476d-b164-23e91f0672af.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='navigation-smartphone-message'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('navigation', 'smartphone', 'message')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):

        self.add_polyline('phone',(30,14),(30,6),(6,6),(6,34),(6,42),(30,42),(30,30))
        self.add_polyline('bubble',(16,14),(30,14),(42,14),(42,30),(30,30),(26,30),(20,36),(20,30),(16,30),closed=True)
        self.relate('connect','phone','bubble')
        self.add_arc('pin-head',(25,22),(33,22),radius_x=4)
        self.add_bezier('pin-tip',(33,22),((33,25),(29,28),(29,28)),((29,28),(25,25),(25,22)))
        self.add_contour('pin','pin-head','pin-tip',closed=True)

# Final visible bounds: (4, 4, 44, 44)
# Construction: One coherent phone enclosure; source message overlap retained.
# Final reductions: Small home-button tick and phone divider omitted because they crowd the overlapping message bubble.
# Visual review: Smartphone, message tail and location pin are all retained. Pin is crowded against bubble boundary and merges visually. MIC fails; not approved.
