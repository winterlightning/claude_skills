"""Muslim Reader Holding Open Book.

Symbol plan: Capped reader behind a broad open book with a central fold. Simplify hanging side cloth and omit page text.
VRECT_L centerline extremes (8,4)-(40,44); exact envelope selected for the subject's proportions.
Construction reference: Lucide book-open: two broad pages with a shared fold; human_ref/user.svg: round head/shoulders. Jaw bottom20, bodytop24: current avatar zero ink gap.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3dbfbc82-fe7f-46ee-b193-539e5dd1a202'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__muslim-reader-holding-open-book/20260927T070927Z-thuan-mac-1/reference/muslim reading quraan_3dbfbc82-fe7f-46ee-b193-539e5dd1a202.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'muslim-reader-holding-open-book'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'avatars'
    categories = ('primitives', 'avatars')
    aliases = ()
    keywords = ('reading', 'book', 'muslim', 'person', 'headscarf', 'clothing', 'portrait', 'islam', 'community', 'people')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        arc('crown',(16,12),(32,12),8)
        arc('jaw',(32,12),(16,12),8)
        join('head','crown','jaw',closed=True)
        line('cap',(16,12),(32,12));connect('cap','head')
        # Scarf drapes fall behind the open pages instead of creating a box lid.
        path('scarf-left',(16,12),(12,24),(8,28))
        path('scarf-right',(32,12),(36,24),(40,28))
        connect('head','scarf-left');connect('head','scarf-right')
        path('book',(8,28),(24,32),(40,28),(40,40),(24,44),(8,40),(8,28),closed=True)
        line('fold',(24,32),(24,44));connect('fold','book');connect('scarf-left','book');connect('scarf-right','book')
