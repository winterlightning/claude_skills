# monitoring bed

A reclining medical bed below a small heartbeat monitor.

Keyshape: HRECT_L — Wide reclining medical scene. Exact centerline extremes are recorded in the Python module.

Construction: Rounded reclining cushion on a pedestal, with an independent small screen at upper left. Preserve the two-part arrangement.

Visual review: Light/dark previews inspected at native and enlarged sizes. Reclining chair, pedestal and small ECG screen are preserved. Pulse crowds the monitor border and the cushion opening is narrow. Not visually approved.

Omissions and reductions: None.

References:
- icon_set/work/todo-references/monitoring bed_fd9ee582-67bc-480d-85e3-0fdc2982679b.svg
- icon_set/references/lucide/original/monitor.svg
- icon_set/references/lucide/atomic-debug/monitor.svg

```text
status: invalid
  ERROR  mic [monitor]: parallel straight edges monitor-0 and pulse-5 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [pulse]: parallel straight edges pulse-5 and monitor-4 are 7 apart on centerlines (ink gap 3); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [pulse]: parallel straight edges pulse-1 and monitor-4 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (overlap-fallback)
  ERROR  mic [monitor]: parallel straight edges monitor-4 and bed-top are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [bed]: parallel straight edges bed-top and bed-bottom-left, bed-bottom-right are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [bed]: parallel straight edges bed-bottom-left, bed-bottom-right and base-1, base-2 are 6 apart on centerlines (ink gap 2); requires at least 8 centerline / 4 ink (midpoint-normal)
  ERROR  mic [monitor]: monitor and bed are 6 apart on centerlines nearest (25, 22)<->(25, 28); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```
