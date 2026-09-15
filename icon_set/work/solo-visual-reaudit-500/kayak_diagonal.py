from repair import *
# Keep the previously checked horizontal alternatives for a side-by-side review.
for n in (15,16):
 r=next(r for r in records if r['number']==n);p=ROOT/r['file'];(W/f'kayak-horizontal-{n}.txt').write_text(p.read_text())
 hull="""# Paired cubic halves share exact diagonal attachment nodes.
self.add_bezier('hull-upper-left',(42,6),((28.6666666667,6),(19.6666666667,8.3333333333),(14,14)))
self.add_bezier('hull-lower-left',(14,14),((8.3333333333,19.6666666667),(6,28.6666666667),(6,42)))
self.add_bezier('hull-lower-right',(6,42),((19.3333333333,42),(28.3333333333,39.6666666667),(34,34)))
self.add_bezier('hull-upper-right',(34,34),((39.6666666667,28.3333333333),(42,19.3333333333),(42,6)))
self.add_contour('hull','hull-upper-left','hull-lower-left','hull-lower-right','hull-upper-right',closed=True)
# Rotated matching teardrop blades with real shaft receiver nodes.
self.add_arc('blade-nw',(14,10),(10,14),radius_x=4,large_arc=True,sweep=False)
self.add_line('blade-nw-base',(10,14),(14,14))
self.add_line('blade-nw-side',(14,14),(14,10))
self.add_contour('blade-left','blade-nw','blade-nw-base','blade-nw-side',closed=True)
self.add_arc('blade-se',(34,38),(38,34),radius_x=4,large_arc=True,sweep=False)
self.add_line('blade-se-base',(38,34),(34,34))
self.add_line('blade-se-side',(34,34),(34,38))
self.add_contour('blade-right','blade-se','blade-se-base','blade-se-side',closed=True)
self.relate('connect','hull','blade-left')
self.relate('connect','hull','blade-right')
"""
 if n==15:
  hull+="""k=0.5522847498307936
# Elliptical cockpit: major vector(6,-6), minor vector(4,4).
self.add_bezier('cockpit-ne',(20,20),((20+6*k,20-6*k),(30-4*k,18-4*k),(30,18)))
self.add_bezier('cockpit-se',(30,18),((30+4*k,18+4*k),(28+6*k,28-6*k),(28,28)))
self.add_bezier('cockpit-sw',(28,28),((28-6*k,28+6*k),(18+4*k,30+4*k),(18,30)))
self.add_bezier('cockpit-nw',(18,30),((18-4*k,30-4*k),(20-6*k,20+6*k),(20,20)))
self.add_contour('cockpit','cockpit-ne','cockpit-se','cockpit-sw','cockpit-nw',closed=True)
self.add_line('shaft-left',(14,14),(20,20))
self.add_line('shaft-right',(28,28),(34,34))
for name in ['shaft-left','shaft-right']:
    self.relate('connect',name,'hull')
    self.relate('connect',name,'cockpit')
self.relate('connect','shaft-left','blade-left')
self.relate('connect','shaft-right','blade-right')
"""
 else:
  hull+="""self.add_line('shaft',(14,14),(34,34))
self.relate('connect','shaft','hull')
self.relate('connect','shaft','blade-left')
self.relate('connect','shaft','blade-right')
"""
 save(n,hull,'Diagonal kayak and matching teardrop paddle blades reconstructed from the original source and the inspected Lucide kayak original/atomic-debug. Shared bow/stern and shaft nodes preserve exact contacts. The cockpit variant uses a larger elliptical opening and shows the shaft outside the raised cockpit rim; the center portion is occluded by the seat. Deliberate diagonal orientation fits the complete subject on SQUARE without broken paddle tips.','SQUARE')
