from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d22466c-f3d2-483e-8d05-604dbca040ce'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/circle notch_9d22466c-f3d2-483e-8d05-604dbca040ce.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-loading-progress-indicator'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('circular', 'loading', 'progress', 'indicator')

    def build(self):
        # Single circular arc with centered top opening. Circle center(24,24), radius20 gives radial ink radius22. Integer Pythagorean endpoints(12,8)/(36,8) keep a true circle; opening widened to preserve exact geometry.
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def rect(n,l,t,r,b):
            self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True)
        def rounded(n,l,t,r,b,k):
            self.add_line(n+'-t',(l+k,t),(r-k,t))
            self.add_arc(n+'-tr',(r-k,t),(r,t+k),radius_x=k)
            self.add_line(n+'-r',(r,t+k),(r,b-k))
            self.add_arc(n+'-br',(r,b-k),(r-k,b),radius_x=k)
            self.add_line(n+'-b',(r-k,b),(l+k,b))
            self.add_arc(n+'-bl',(l+k,b),(l,b-k),radius_x=k)
            self.add_line(n+'-l',(l,b-k),(l,t+k))
            self.add_arc(n+'-tl',(l,t+k),(l+k,t),radius_x=k)
            self.add_contour(n,*[n+'-'+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)
        self.add_arc('ring',(12,8),(36,8),radius_x=20,large_arc=True,sweep=False)
