from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '146cf283-3304-46a9-8cae-29ee66a6a52f'
SOURCE_PATH = 'icon_set/work/todo-references/certificate_146cf283-3304-46a9-8cae-29ee66a6a52f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'certificate'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('certificate',)

    def build(self):
        # Wide rectangular certificate with four equal inward corner arcs. Extremes4/44 and8/40. Radius8 repeats mirror about24.

        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
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
        self.add_polyline('frame',(12,8),(36,8),(44,8),(44,16),(44,32),(44,40),(36,40),(12,40),(4,40),(4,32),(4,16),(4,8),closed=True)
        for n,a,b in [('tl',(12,8),(4,16)),('tr',(44,16),(36,8)),('br',(36,40),(44,32)),('bl',(4,32),(12,40))]:
            self.add_arc('corner-'+n,a,b,radius_x=8)
            self.relate('connect','frame','corner-'+n)
