# Blocker: geometric-shapes-in-rounded-square (610733a3)

Reference: a rounded-square frame holding three outlined shapes - a circle
(top right), a square (left middle) and a triangle (bottom right).

SOLO48 budget: the frame occupies the SQUARE centerline box (6..42); every inner
shape must stay 8 from the walls, which leaves a 20x20 region (14..34), and 8
between shapes.

- square outline: its own parallel sides must be 8 apart -> at least 8x8
  (a 6x6 square fails the parallel-edge MIC check, see validation.txt)
- circle: the exempt r3 ring is the smallest outlined circle (6 across); an arc
  exactly 8 from the frame comes back `review`, so 9 is needed
- triangle outline: needs a centerline inscribed radius of about 3.2 (at least
  12 wide x 10 tall); smaller triangles fail the hole gate (solid 6x4 attempt:
  "1 undersized holes; 1 pinches")

Any row or column holding two shapes needs 8 + 8 + 6 = 22 or more against the 20
available, and the triangle adds 10 more vertically. The shapes cannot keep 8
apart inside the frame. Dropping the frame or merging shapes into it would
change the subject.
