//! Timestamps in the exact text form Python's `datetime.isoformat()` writes.
//!
//! Stored stamps are compared as text in SQL (`claimed_at <= ?`), so every stamp this crate
//! writes must sort the same way the Python server's stamps do.

use chrono::{DateTime, FixedOffset, NaiveDate, NaiveDateTime, TimeZone, Timelike, Utc};

/// `datetime.isoformat()` of an aware datetime: microseconds only when nonzero, `+HH:MM` offset.
pub fn iso<Tz: TimeZone>(when: &DateTime<Tz>) -> String
where
    Tz::Offset: std::fmt::Display,
{
    let fixed = when.fixed_offset();
    if fixed.nanosecond() / 1000 == 0 {
        fixed.format("%Y-%m-%dT%H:%M:%S%:z").to_string()
    } else {
        fixed.format("%Y-%m-%dT%H:%M:%S%.6f%:z").to_string()
    }
}

/// `datetime.now(timezone.utc).isoformat()` for a given instant.
pub fn iso_utc(when: DateTime<Utc>) -> String {
    // Python keeps microsecond precision; drop anything finer so stamps round-trip.
    let micros = when.timestamp_subsec_micros();
    let trimmed = when.with_nanosecond(micros * 1000).unwrap_or(when);
    iso(&trimmed)
}

/// `datetime.fromisoformat` for the stamps this system stores; naive stamps are UTC.
pub fn parse_time(stamp: &str) -> Option<DateTime<FixedOffset>> {
    let text = stamp.trim().replace('Z', "+00:00");
    if text.is_empty() {
        return None;
    }
    for format in ["%Y-%m-%dT%H:%M:%S%.f%:z", "%Y-%m-%d %H:%M:%S%.f%:z", "%Y-%m-%dT%H:%M%:z"] {
        if let Ok(when) = DateTime::parse_from_str(&text, format) {
            return Some(when);
        }
    }
    for format in ["%Y-%m-%dT%H:%M:%S%.f", "%Y-%m-%d %H:%M:%S%.f", "%Y-%m-%dT%H:%M"] {
        if let Ok(naive) = NaiveDateTime::parse_from_str(&text, format) {
            return Some(Utc.from_utc_datetime(&naive).fixed_offset());
        }
    }
    if let Ok(day) = NaiveDate::parse_from_str(&text, "%Y-%m-%d") {
        return Some(Utc.from_utc_datetime(&day.and_hms_opt(0, 0, 0)?).fixed_offset());
    }
    None
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn matches_python_isoformat() {
        let whole = Utc.with_ymd_and_hms(2026, 9, 25, 8, 1, 2).unwrap();
        assert_eq!(iso_utc(whole), "2026-09-25T08:01:02+00:00");
        let fraction = whole.with_nanosecond(123_456_789).unwrap();
        assert_eq!(iso_utc(fraction), "2026-09-25T08:01:02.123456+00:00");
    }

    #[test]
    fn parses_stored_forms() {
        assert!(parse_time("2026-09-17T08:12:31.123456+00:00").is_some());
        assert!(parse_time("2026-09-17T08:12:31Z").is_some());
        assert!(parse_time("2026-09-17 08:12:31").is_some());
        assert_eq!(parse_time("2026-09-17").unwrap().to_rfc3339(), "2026-09-17T00:00:00+00:00");
        assert!(parse_time("").is_none());
        assert!(parse_time("yesterday").is_none());
    }
}
