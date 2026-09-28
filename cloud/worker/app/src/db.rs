//! Thin D1 helpers: positional arguments, typed rows, change counts, atomic batches.

use pictographic_core::primitives::python_json;
use pictographic_core::time::iso_utc;
use serde::de::DeserializeOwned;
use serde_json::{Map, Value};
use worker::wasm_bindgen::JsValue;
use worker::{D1Database, D1PreparedStatement, D1Result, Result};

/// One bound SQL argument.
#[derive(Clone, Debug)]
pub enum Arg {
    Text(String),
    Int(i64),
    Real(f64),
    Null,
}

impl From<&str> for Arg {
    fn from(value: &str) -> Self { Arg::Text(value.to_string()) }
}
impl From<String> for Arg {
    fn from(value: String) -> Self { Arg::Text(value) }
}
impl From<&String> for Arg {
    fn from(value: &String) -> Self { Arg::Text(value.clone()) }
}
impl From<i64> for Arg {
    fn from(value: i64) -> Self { Arg::Int(value) }
}
impl From<bool> for Arg {
    fn from(value: bool) -> Self { Arg::Int(value as i64) }
}
impl From<f64> for Arg {
    fn from(value: f64) -> Self { Arg::Real(value) }
}
impl<T: Into<Arg>> From<Option<T>> for Arg {
    fn from(value: Option<T>) -> Self { value.map(Into::into).unwrap_or(Arg::Null) }
}

impl From<&Arg> for JsValue {
    fn from(value: &Arg) -> Self {
        match value {
            Arg::Text(text) => JsValue::from_str(text),
            Arg::Int(number) => JsValue::from_f64(*number as f64),
            Arg::Real(number) => JsValue::from_f64(*number),
            Arg::Null => JsValue::null(),
        }
    }
}

#[macro_export]
macro_rules! args {
    ($($value:expr),* $(,)?) => { vec![$($crate::db::Arg::from($value)),*] };
}

pub fn stmt(db: &D1Database, sql: &str, args: Vec<Arg>) -> Result<D1PreparedStatement> {
    let values: Vec<JsValue> = args.iter().map(JsValue::from).collect();
    db.prepare(sql).bind(&values)
}

pub async fn all<T: DeserializeOwned>(db: &D1Database, sql: &str, args: Vec<Arg>) -> Result<Vec<T>> {
    stmt(db, sql, args)?.all().await?.results::<T>()
}

pub async fn first<T: DeserializeOwned>(db: &D1Database, sql: &str, args: Vec<Arg>) -> Result<Option<T>> {
    Ok(all::<T>(db, sql, args).await?.into_iter().next())
}

/// Run one statement; returns the number of rows it changed.
pub async fn run(db: &D1Database, sql: &str, args: Vec<Arg>) -> Result<usize> {
    let result = stmt(db, sql, args)?.run().await?;
    Ok(changes(&result))
}

pub fn changes(result: &D1Result) -> usize {
    result.meta().ok().flatten().and_then(|meta| meta.changes).unwrap_or(0)
}

pub fn last_row_id(result: &D1Result) -> Option<i64> {
    result.meta().ok().flatten().and_then(|meta| meta.last_row_id)
}

/// Run statements in one transaction (all or nothing).
pub async fn batch(db: &D1Database, statements: Vec<D1PreparedStatement>) -> Result<Vec<D1Result>> {
    if statements.is_empty() {
        return Ok(Vec::new());
    }
    db.batch(statements).await
}

/// Ordered `**details` of deploy.py `record_activity`.
pub fn details(pairs: Vec<(&str, Value)>) -> Map<String, Value> {
    pairs.into_iter().map(|(key, value)| (key.to_string(), value)).collect()
}

const INSERT_ACTIVITY: &str = "INSERT INTO activity_log(username, action, icon, details, created_at) VALUES (?, ?, ?, ?, ?)";

/// `record_activity(connection, username, action, icon, **details)` as a statement for a batch.
pub fn activity(db: &D1Database, user: &str, action: &str, icon: Option<&str>, details: Map<String, Value>) -> Result<D1PreparedStatement> {
    stmt(db, INSERT_ACTIVITY, args![user, action, icon, python_json(&Value::Object(details)), iso_utc(chrono::Utc::now())])
}

/// Log only when the previous statement in the batch changed a row.
pub fn activity_if_changed(db: &D1Database, user: &str, action: &str, icon: Option<&str>, details: Map<String, Value>) -> Result<D1PreparedStatement> {
    stmt(db, "INSERT INTO activity_log(username, action, icon, details, created_at) SELECT ?, ?, ?, ?, ? WHERE changes() > 0",
         args![user, action, icon, python_json(&Value::Object(details)), iso_utc(chrono::Utc::now())])
}

/// Log with values only SQLite knows yet: `"__ROWID__"` becomes the previous insert's row id and
/// `"__CHANGES__"` the previous statement's change count. Logged only if that statement changed rows.
pub fn activity_with_placeholders(db: &D1Database, user: &str, action: &str, icon: Option<&str>, details: Map<String, Value>) -> Result<D1PreparedStatement> {
    stmt(db, "INSERT INTO activity_log(username, action, icon, details, created_at) \
              SELECT ?, ?, ?, replace(replace(?, '\"__ROWID__\"', last_insert_rowid()), '\"__CHANGES__\"', changes()), ? \
              WHERE changes() > 0",
         args![user, action, icon, python_json(&Value::Object(details)), iso_utc(chrono::Utc::now())])
}
