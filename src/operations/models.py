from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData

metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("quantity", String),
    Column("figi", String),
    Column("instrument_type", String, nullable=True, default=None),
    Column("date", TIMESTAMP),
    Column("type", String),
)
