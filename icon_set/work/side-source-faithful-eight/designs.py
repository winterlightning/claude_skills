SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/side-source-faithful-eight/batch.json'
AUTHOR='gpt-6'
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'side-repair-50-priority-10'))
from glyph_fit import fit
D={};GLYPHS={};TEXT={};TALL=set();DIMS={1:(32,44),2:(32,40),3:(32,48),4:(44,32),5:(44,32),8:(40,32)}
def plan(n,parts,body,shape='SQUARE'):D[n]=(shape,parts,'Original source composition; clean contour construction',body)
def dollar(cx,y):return f'from icon_set.typeface.reference_forms import draw_open_dollar\ndraw_open_dollar(self,{cx},{y})'
plan(1,'Restored oval Bitcoin speech bubble, lower-left tail, B bowls and both pairs of currency ticks.',"""
self.add_bezier('oval-tl',(16,2),((8,2),(2,10),(2,20)))
self.add_bezier('oval-bl',(2,20),((2,26),(4,30),(7,33)))
self.add_line('tail-a',(7,33),(4,42));self.add_line('tail-b',(4,42),(12,37))
self.add_bezier('oval-br',(12,37),((22,40),(30,32),(30,20)))
self.add_bezier('oval-tr',(30,20),((30,10),(24,2),(16,2)))
self.add_contour('bubble','oval-tl','oval-bl','tail-a','tail-b','oval-br','oval-tr')
from icon_set.typeface.sub32 import draw_bitcoin
draw_bitcoin(self)
""")
plan(2,'Rounded money speech bubble with the original long lower-left tail and open S-shaped dollar with short currency ticks.',"""
self.add_line('top',(6,2),(26,2));self.add_arc('tr',(26,2),(30,6),radius_x=4)
self.add_line('right',(30,6),(30,28));self.add_arc('br',(30,28),(26,32),radius_x=4)
self.add_line('tail-a',(26,32),(15,32));self.add_line('tail-b',(15,32),(8,38));self.add_line('tail-c',(8,38),(8,32));self.add_line('tail-d',(8,32),(6,32))
self.add_arc('bl',(6,32),(2,28),radius_x=4);self.add_line('left',(2,28),(2,6));self.add_arc('tl',(2,6),(6,2),radius_x=4)
self.add_contour('bubble','top','tr','right','br','tail-a','tail-b','tail-c','tail-d','bl','left','tl')
"""+dollar(16,10))
plan(3,'Complete closed shield with curved crown, pointed base and one five-point star fully inside.',"""
self.add_bezier('crown-l',(2,6),((7,4),(12,2),(16,2)))
self.add_bezier('crown-r',(16,2),((20,2),(25,4),(30,6)))
self.add_line('right',(30,6),(30,26))
self.add_bezier('lower-r',(30,26),((30,36),(24,42),(16,46)))
self.add_bezier('lower-l',(16,46),((8,42),(2,36),(2,26)))
self.add_line('left',(2,26),(2,6));self.add_contour('shield','crown-l','crown-r','right','lower-r','lower-l','left')
self.add_polyline('star',(16,12),(19,20),(24,20),(20,25),(22,32),(16,28),(10,32),(12,25),(8,20),(13,20),(16,12))
""")
page="""
self.add_line('top',(6,2),(32,2));self.add_line('corner-a',(32,2),(42,12));self.add_line('corner-b',(42,12),(42,26))
self.add_arc('br',(42,26),(38,30),radius_x=4);self.add_line('bottom',(38,30),(6,30));self.add_arc('bl',(6,30),(2,26),radius_x=4)
self.add_line('left',(2,26),(2,6));self.add_arc('tl',(2,6),(6,2),radius_x=4)
self.add_contour('page','top','corner-a','corner-b','br','bottom','bl','left','tl')
for n,y in [('line-one',16),('line-two',24)]:self.add_line(n,(29,y),(34,y))
"""
pound,_=fit('symbol-pound',14,14,17,'pound',width=44)
plan(4,'Pound invoice: rounded clipped-corner page, pound on the left and both right-hand text lines restored.',page+pound);GLYPHS[4]=('symbol-pound',)
plan(5,'Dollar document: rounded clipped-corner page, original open dollar on the left and both right-hand text lines restored.',page+dollar(14,10))
r,_=fit('letter-r-uppercase',16,16,16,'registered')
plan(6,'Registered trademark: complete circular outline, original R bowl, stem and long diagonal leg.',"circle(self,'ring',16,16,14)\n"+r,'CIRCLE');GLYPHS[6]=('letter-r-uppercase',)
plan(7,'Hryvnia: curved reverse S with rounded upper bowl, sweeping diagonal belly and two lower horizontal bars.',"""
from icon_set.typeface.reference_forms import draw_curved_hryvnia
draw_curved_hryvnia(self)
""")
plan(8,'Monitor: rounded screen, centered open dollar, attached vertical stem and full horizontal foot restored.',"""
box(self,'screen',2,2,38,24,4)
self.add_line('stem',(20,24),(20,30));self.add_line('foot',(14,30),(26,30));self.relate('connect','stem','screen');self.relate('connect','stem','foot')
"""+dollar(20,6))
GLYPHS.update({1:('symbol-bitcoin',),2:('symbol-dollar',),5:('symbol-dollar',),7:('symbol-hryvnia',),8:('symbol-dollar',)})
# Keep invoice orientation and full source layout; use compact shared text forms.
DIMS.update({4:(32,40),5:(32,40)})
page32="""
self.add_line('top',(6,2),(20,2));self.add_line('fold',(20,2),(30,12));self.add_line('right',(30,12),(30,34))
self.add_arc('br',(30,34),(26,38),radius_x=4);self.add_line('bottom',(26,38),(6,38));self.add_arc('bl',(6,38),(2,34),radius_x=4)
self.add_line('left',(2,34),(2,6));self.add_arc('tl',(2,6),(6,2),radius_x=4)
self.add_contour('page','top','fold','right','br','bottom','bl','left','tl')
for n,y in [('line-one',20),('line-two',28)]:self.add_line(n,(22,y),(24,y))
"""
pound,_=fit('symbol-pound',10,12,24,'pound',width=32)
D[4]=(*D[4][:3],page32+pound)
D[5]=(*D[5][:3],page32+'from icon_set.typeface.reference_forms import draw_small_open_dollar\ndraw_small_open_dollar(self,12,18)')
D[8]=(*D[8][:3],D[8][3].split('from icon_set.typeface.reference_forms')[0].replace('38,24','38,22').replace('(20,24)','(20,22)')+'from icon_set.typeface.reference_forms import draw_small_open_dollar\ndraw_small_open_dollar(self,20,8)')
D[3]=(*D[3][:3],D[3][3].replace('(24,20)','(23,20)').replace('(8,20)','(9,20)'))
r,_=fit('letter-r-uppercase',14,16,16,'registered')
D[6]=(*D[6][:3],"circle(self,'ring',16,16,14)\n"+r)
# Recenter the full Bitcoin inside the oval and keep breathing room below ticks.
D[1]=(*D[1][:3],D[1][3].replace('((2,26),(4,30),(7,33))','((2,28),(4,34),(7,36))').replace('(7,33)','(7,36)').replace('(12,37)','(12,39)').replace('((22,40),(30,32),(30,20))','((22,42),(30,32),(30,20))'))
DIMS[1]=(32,48)
D[1]=(*D[1][:3],D[1][3].replace('(4,42)','(4,46)').replace('(12,39)','(12,43)').replace('((22,42),(30,32),(30,20))','((24,46),(30,34),(30,20))'))
D[2]=(*D[2][:3],D[2][3].replace('draw_open_dollar(self,16,10)','draw_open_dollar(self,16,11)'))
DIMS[4]=(32,44)
D[4]=(*D[4][:3],page32.replace('(30,34)','(30,38)').replace('(26,38)','(26,42)').replace('(6,38)','(6,42)').replace('(2,34)','(2,38)').replace('(22,y),(24,y)','(22,y),(23,y)')+'from icon_set.typeface.reference_forms import draw_narrow_pound\ndraw_narrow_pound(self)')
D[5]=(*D[5][:3],D[5][3].replace('(22,y),(24,y)','(22,y),(23,y)'))
D[6]=(*D[6][:3],"circle(self,'ring',16,16,14)\nfrom icon_set.typeface.sub32 import draw_registered_r\ndraw_registered_r(self)")
DIMS[8]=(32,40)
D[8]=(*D[8][:3],"""
box(self,'screen',2,2,30,30,4)
self.add_line('stem',(16,30),(16,38));self.add_line('foot',(10,38),(22,38));self.relate('connect','stem','screen');self.relate('connect','stem','foot')
from icon_set.typeface.reference_forms import draw_small_open_dollar
draw_small_open_dollar(self,16,11)
""")
D[1]=(*D[1][:3],D[1][3].replace('(7,36)','(6,38)'))
DIMS[2]=(32,42)
D[2]=(*D[2][:3],D[2][3].replace('(30,28)','(30,30)').replace('(26,32)','(26,34)').replace('(15,32)','(15,34)').replace('(8,38)','(8,40)').replace('(8,32)','(8,34)').replace('(6,32)','(6,34)').replace('(2,28)','(2,30)'))
for n in (4,5):D[n]=(*D[n][:3],D[n][3].replace('(22,y),(23,y)','(21,y),(23,y)'))
D[5]=(*D[5][:3],D[5][3].replace('draw_small_open_dollar(self,12,18)','draw_small_open_dollar(self,12,16)'))
