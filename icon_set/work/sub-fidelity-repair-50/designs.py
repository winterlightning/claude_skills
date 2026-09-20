SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/sub-fidelity-repair-50/batch.json'
AUTHOR='gpt-6'
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'side-repair-50-priority-10'))
from glyph_native import fit
D={};GLYPHS={};DIMS={}
def plan(n,w,h,parts,body):D[n]=('SQUARE',parts,'Complete original composition; existing shared glyph geometry',body);DIMS[n]=(w,h)
def ring(size):return f"circle(self,'frame',{size//2},{size//2},{size//2-2})\n"
plan(21,48,48,'Rounded image frame, small sun mark and both mountains connected to the lower-left and right frame.',"""
box(self,'frame',2,2,46,46,5)
self.add_dot('sun',(15,15))
self.add_polyline('mountains',(5,45),(17,30),(23,35),(34,19),(46,36))
self.relate('connect','mountains','frame')
""")
plan(29,48,40,'Open triangular sand pile with exactly three original grains.',"""
self.add_polyline('pile',(2,38),(24,2),(46,38))
self.add_dot('grain-left',(15,32));self.add_dot('grain-right',(33,32));self.add_dot('grain-top',(24,22))
""")
plan(39,48,48,'Complete outer circle and the original vertically oval zero.',ring(48)+"""
self.add_arc('zero-left',(24,10),(24,38),radius_x=8,radius_y=14,sweep=False)
self.add_arc('zero-right',(24,38),(24,10),radius_x=8,radius_y=14,sweep=False)
self.add_contour('zero','zero-left','zero-right',closed=True)
""")
plan(40,44,48,'Five waveform bars with the original unequal heights, in their original order.',"""
for i,(x,t,b) in enumerate([(2,18,30),(12,10,38),(22,2,46),(32,14,34),(42,22,26)]):
 self.add_line(f'bar-{i}',(x,t),(x,b))
""")
plan(41,64,64,'Outer circle and descending zigzag arrow retaining its intermediate upward step and lower-right head.',ring(64)+"""
self.add_polyline('shaft',(14,22),(27,35),(35,27),(48,42))
self.add_polyline('head',(48,32),(48,42),(38,42));self.relate('connect','head','shaft')
""")
plan(42,48,48,'Three ascending vertical bars and shared baseline, inside the complete circle.',ring(48)+"""
self.add_line('baseline',(14,34),(34,34))
for n,x,y in [('small',16,26),('medium',24,20),('large',32,14)]:
 self.add_line(n,(x,y),(x,34));self.relate('connect',n,'baseline')
""")
a,_=fit('letter-a-uppercase',32,30,48,'a',width=96);b,_=fit('letter-b-uppercase',32,65,48,'b',width=96)
plan(43,96,96,'Complete circle enclosing the original uppercase AB in order, reusing shared letters.',ring(96)+a+'\n'+b);GLYPHS[43]=('letter-a-uppercase','letter-b-uppercase')
for n,g in [(44,'letter-a-uppercase'),(45,'letter-b-uppercase'),(46,'letter-p-uppercase'),(47,'letter-r-uppercase')]:
 body,_=fit(g,28,32,32,'glyph',width=64)
 plan(n,64,64,'Complete source circle and uppercase '+g.split('-')[1].upper()+', retaining the shared typeface.',ring(64)+body);GLYPHS[n]=(g,)
plan(48,64,64,'Complete circular outline and house with projecting roof, side walls and rounded doorway.',ring(64)+"""
self.add_polyline('roof',(12,30),(32,10),(52,30))
self.add_polyline('left',(18,24),(18,46),(26,46),(26,38))
self.add_arc('door',(26,38),(38,38),radius_x=6,sweep=True)
self.add_polyline('right',(38,38),(38,46),(46,46),(46,24))
self.relate('connect','roof','left');self.relate('connect','roof','right');self.relate('connect','left','door');self.relate('connect','right','door')
""")
plan(49,64,64,'Original circled information symbol: detached dot, upper left serif, stem and lower foot.',ring(64)+"from icon_set.typeface.framed_source_forms import draw_information_serif\ndraw_information_serif(self)");GLYPHS[49]=('letter-i',)
plan(50,64,64,'Original circled text-tool T, retaining its two hanging top serifs and bottom foot.',ring(64)+"from icon_set.typeface.framed_source_forms import draw_text_tool_t\ndraw_text_tool_t(self)");GLYPHS[50]=('letter-t-uppercase',)
D[21]=(*D[21][:3],D[21][3].replace('(5,45),(17,30)','(10,39),(17,30)'))
plan(8,32,32,'Bell with the original rounded top bump, flared lower rim and detached clapper.',"""
self.add_bezier('bell-left',(2,22),((6,18),(6,17),(6,12)))
self.add_bezier('shoulder-left',(6,12),((6,8),(9,6),(12,6)))
self.add_arc('rounded-top',(12,6),(20,6),radius_x=4,sweep=True)
self.add_bezier('shoulder-right',(20,6),((23,6),(26,8),(26,12)))
self.add_bezier('bell-right',(26,12),((26,17),(26,18),(30,22)))
self.add_line('rim',(30,22),(2,22));self.add_contour('bell','bell-left','shoulder-left','rounded-top','shoulder-right','bell-right','rim')
self.add_line('clapper',(14,30),(18,30))
""")
