"""book-close-2: next fifty AI review; original preserved."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '7025f460-1d25-427d-b645-3853db39a1d0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__book-close-2/20260927T152212Z-thuan-mac-1/reference/book close 2_7025f460-1d25-427d-b645-3853db39a1d0.svg'
AUTHOR = 'gpt-6'

class BookClose2(Solo48):
    icon_id = 'book-close-2'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'content'
    categories = ('primitives', 'content')
    aliases = ()
    keywords = ('book', 'close', 'content', 'solo-ai-next50')

    def build(self):
        # Square cover with a rolled top page and rounded lower corners.
        self.add_line('cover-top',(6,6),(42,6))
        self.add_line('cover-right-upper',(42,6),(42,20))
        self.add_line('cover-right',(42,20),(42,38))
        self.add_arc('corner-right',(42,38),(38,42),radius_x=4,sweep=True)
        self.add_line('cover-bottom',(38,42),(14,42))
        self.add_arc('corner-left',(14,42),(6,34),radius_x=8,sweep=True)
        self.add_line('cover-left-lower',(6,34),(6,16))
        self.add_line('cover-left-upper',(6,16),(6,6))
        self.add_contour('cover','cover-top','cover-right-upper','cover-right','corner-right','cover-bottom','corner-left','cover-left-lower','cover-left-upper',closed=True)
        self.add_bezier('page-roll',(6,16),((10,19),(12,20),(18,20)))
        self.add_line('page-edge',(18,20),(42,20))
        self.add_contour('pages','page-roll','page-edge')
        self.relate('connect','pages','cover')
