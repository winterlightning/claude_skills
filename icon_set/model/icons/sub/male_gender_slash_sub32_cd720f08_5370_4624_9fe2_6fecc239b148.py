"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = 'cd720f08-5370-4624-9fe2-6fecc239b148'
SOURCE_PATH = 'pictographic-primitives/pets/male stablization_cd720f08-5370-4624-9fe2-6fecc239b148.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('lower-left circle', 'upper-right arrow with two-stroke head', 'diagonal upper-left to lower-right slash')

class Drawing(Sub32):
    icon_id = 'male-gender-slash-sub32'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    keywords = ('male', 'gender', 'symbol', 'with', 'slash')


    def build(self):
        # Circle contact is the exact 6-8-10 radius point, preserving its true join.
        self.circle('circle',12,20,10)
        self.add_line('shaft',(18,12),(30,2))
        self.add_polyline('arrowhead',(23,2),(30,2),(30,9))
        self.relate('connect','shaft','arrowhead-1','arrowhead-2')
        self.relate('connect','shaft','circle-top')
        self.add_line('slash',(2,10),(22,30))
        self.relate('connect','slash','circle-top')
        self.relate('connect','slash','circle-bottom')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)


# Outcome of /fix-icon-sub for the strict 32x32 gate; metadata only.
SUB32_FIX_RECORDS = {'male-gender-slash-sub32': {'status': 'fixed',
                             'date': '2026-09-24',
                             'author': 'gpt-6',
                             'source_icon_id': 'cd720f08-5370-4624-9fe2-6fecc239b148',
                             'failures_at_review': ['mic [circle]: circle and shaft are '
                                                    '0.000514467 apart on centerlines nearest '
                                                    '(17.9997, 12.0004)<->(18, 12); SUB32 requires '
                                                    'at least 6 (ink clearance 2) unless the '
                                                    'contact is declared with a scoped `connect` '
                                                    'relationship',
                                                    'mic [circle]: circle and slash are 0 apart on '
                                                    'centerlines nearest (4.92893, '
                                                    '12.9289)<->(4.92893, 12.9289); SUB32 requires '
                                                    'at least 6 (ink clearance 2) unless the '
                                                    'contact is declared with a scoped `connect` '
                                                    'relationship'],
                             'variant': 'male-gender-slash-sub32-clean',
                             'evidence': 'icon_set/work/side-subs-20260924/fix-25/cd720f08-5370-4624-9fe2-6fecc239b148'}}
