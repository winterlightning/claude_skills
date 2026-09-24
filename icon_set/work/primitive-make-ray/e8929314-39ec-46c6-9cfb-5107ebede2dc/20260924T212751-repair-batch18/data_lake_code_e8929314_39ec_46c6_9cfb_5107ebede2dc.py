"""Binary strings 10100 and 01100 above lake waves.
Symbol plan and construction: No useful local waves match found; source owns both literal binary strings and repeated wave form.
Keyshape: SQUARE balances both code rows above a water band after wide and tall alternatives.
Omissions: Two water rows reduced to one; numeral ones omit serifs; all ten digits retained.
Review: Blocked: digit gaps remain 4-5 units instead of 8, including the parallel one strokes. Vertical separation improved, but native-size binary remains crowded. Six candidates saved."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID='e8929314-39ec-46c6-9cfb-5107ebede2dc'
SOURCE_PATH = 'pictographic-primitives/programing/data lake code_e8929314-39ec-46c6-9cfb-5107ebede2dc.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='data-lake-code'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('data', 'lake', 'code')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        for row,(text,starts) in enumerate([('10100',(6,11,22,26,36)),('01100',(6,17,22,26,36))]):
            y=6+row*16
            for col,(digit,x) in enumerate(zip(text,starts)):
                n=f'digit-{row}-{col}'
                if digit=='1':self.add_line(n,(x,y),(x,y+6))
                else:
                    self.add_arc(n+'-top',(x,y+3),(x+6,y+3),radius_x=3,radius_y=3)
                    self.add_arc(n+'-bottom',(x+6,y+3),(x,y+3),radius_x=3,radius_y=3)
                    self.add_contour(n,n+'-top',n+'-bottom',closed=True)
        for row,y in enumerate((40,)):
            for col in range(2):
                x=6+18*col
                self.add_bezier(f'wave-{row}-{col}',(x,y),((x+3,y+2),(x+6,y+2),(x+9,y+2)),((x+12,y+2),(x+15,y+2),(x+18,y)))
            self.add_contour(f'water-{row}',f'wave-{row}-0',f'wave-{row}-1')
