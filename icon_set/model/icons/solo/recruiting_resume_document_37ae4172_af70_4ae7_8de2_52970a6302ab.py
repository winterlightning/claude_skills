"""A résumé document with a photo placeholder, text and an applicant silhouette.
Plan: SQUARE balances the open document with the right-side applicant. Visible ink bounds: (4, 4, 44, 44).
Reduction: Text reduced from two rows to one shorter row; document bottom shortened to clear the person.
Construction: Shared human user.svg: circular head and broad shoulders."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '37ae4172-af70-4ae7-8de2-52970a6302ab'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_32/recruiting resume document_37ae4172-af70-4ae7-8de2-52970a6302ab.svg'
AUTHOR = 'gpt-6'
PLAN = 'A résumé document with a photo placeholder, text and an applicant silhouette.'
OMISSIONS = 'Text reduced from two rows to one shorter row; document bottom shortened to clear the person.'
CONSTRUCTION_REFERENCES = 'Shared human user.svg: circular head and broad shoulders.'
KEYSHAPE_INK_BOUNDS = (4, 4, 44, 44)

class Drawing(Solo48):
    icon_id = 'recruiting-resume-document'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('recruiting', 'resume', 'document')

    def circle(self, n, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(n + '-a', (x - r, y), (x + r, y), radius_x=r, radius_y=ry)
        self.add_arc(n + '-b', (x + r, y), (x - r, y), radius_x=r, radius_y=ry)
        self.add_contour(n, n + '-a', n + '-b', closed=True)

    def build(self):
        self.add_polyline('document', (36, 6), (6, 6), (6, 42), (20, 42))
        self.add_polyline('photo', (14, 14), (22, 14), (22, 22), (14, 22), closed=True)
        for (i, y) in enumerate((30,)):
            self.add_line('text' + str(i), (14, y), (18, y))
        self.circle('head', 34, 18, 4)
        self.add_arc('shoulders', (26, 36), (42, 36), radius_x=8, radius_y=6)
        self.add_polyline('body', (42, 36), (39, 36), (38, 42), (30, 42), (29, 36), (26, 36))
        self.relate('connect', 'shoulders', 'body')
