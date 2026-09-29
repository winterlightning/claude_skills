from author_refine import *
SPECS[18]['body']=SPECS[18]['body'].replace('(14,33),(24,15),(34,15),(24,33)','(15,33),(24,15),(33,15),(24,33)')
SPECS[15]['body']='''
# Sun disk and cloud share actual endpoints at the occluded disk edge.
curve(self,'sun',(9,22),((3,16),(7,7),(14,7)),((18,7),(21,10),(22,14)))
self.add_line('ray-top',(14,2),(14,3))
self.add_line('ray-left',(2,14),(3,14))
self.add_line('ray-diagonal',(4,5),(5,6))
curve(self,'cloud',(22,37),((16,37),(8,38),(6,32)),((2,26),(5,22),(9,22)),((11,22),(12,22),(14,22)),((15,17),(18,14),(22,14)),((28,14),(31,17),(33,21)),((38,20),(41,22),(42,25)))
self.relate('connect','sun','cloud')
curve(self,'pin',(35,44),((31,39),(26,34),(26,30)),((26,18),(44,18),(44,30)),((44,34),(39,39),(35,44)),closed=True)
circle(self,'pin-hole',35,29,3)
'''
SPECS[17]['body']=SPECS[17]['body'].replace("self.add_polyline('tail',(9,34),(4,26),(9,27),(11,22),(13,27))\nself.relate('connect','tail','body')\n",'')+"\nself.add_dot('eye-left',(20,16));self.add_dot('eye-right',(28,16));self.add_dot('nose',(24,23))\n"
SPECS[17]['change']='Restored a smooth seal body, two outward flippers and paired whiskers, and added a minimal face to make the animal clear at UI size.'
SPECS[17]['omissions']=['Omitted the small side tail because it collided with the whiskers at 48px; front flippers, whiskers and a minimal face preserve seal recognition.']
SPECS[17]['exception']='Preserve the seal silhouette, whiskers, paired flippers and simple face at 48px. Compact contour/whisker spacing is intentional; the small side tail is omitted to avoid clutter.'
SPECS[19]['body']=SPECS[19]['body'].replace("self.add_polyline('charge',(26,29),(20,35),(24,35),(22,39),(28,33),(24,33),closed=True)","self.add_polyline('charge',(26,30),(21,35),(27,35),(22,39))")
if __name__=='__main__':
 for i in map(int,sys.argv[1:]):refine(i)
