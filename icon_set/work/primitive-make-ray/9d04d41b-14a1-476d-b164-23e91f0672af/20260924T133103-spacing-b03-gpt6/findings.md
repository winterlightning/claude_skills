# navigation smartphone message

Source: `pictographic-primitives/_uncategorized_28/navigation smartphone message_9d04d41b-14a1-476d-b164-23e91f0672af.svg`

Status: **blocked**. Keyshape: `VRECT_L`.

Blocked after five repair rounds. Final pointed pin remains recognizable, but bubble/pin separation at (24,12)-(24,20) is an uncertified exact8 gap. A flattened numeric-pass variant lost the location-pin shape and was rejected visually. Both themes reviewed.

Omissions: Home button and screen divider omitted; shared phone/bubble wall merged

Construction references: lucide/message-square original and atomic-debug: coherent bubble tail

Validation: review; 0 errors; 1 warnings.

```text
BUILD GATE FAIL (review, 0 errors, 1 warnings)
  warning: mic [bubble]: bubble and pin are 8 apart on centerlines nearest (24, 12)<->(24, 20); SOLO48 requires at least 8 (ink clearance 4) unless the contact is declared with a scoped `connect` relationship
```

5 repair rounds after the initial candidate. Attempts and gate overlays are retained locally.
