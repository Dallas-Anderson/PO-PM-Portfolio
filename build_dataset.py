#!/usr/bin/env python3
"""
Builds a small SQLite dataset for the co-op Medicare Advantage concept
(Morgan County pilot). Backs the low-fi wireframes for:
  F001 - Lane 1 uniform benefits
  F002 - Lane 2 SSBCI targeted benefits
  F003 - Local vendor network
  F004 - CMS filing / MLR compliance
  F005 - Premium transparency

Minimal but real relational structure so every wireframe pulls from the
same consistent dataset instead of one-off placeholder text per screen.
"""
import sqlite3
from pathlib import Path

DB_PATH = Path("/home/claude/dev_agent/coop_health.db")
if DB_PATH.exists():
    DB_PATH.unlink()

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

c.executescript("""
CREATE TABLE members (
    member_id TEXT PRIMARY KEY,
    name TEXT,
    age INTEGER,
    ssbci_eligible INTEGER,  -- 0/1
    wellness_stipend_balance REAL
);

CREATE TABLE lane1_benefits (
    benefit_id TEXT PRIMARY KEY,
    name TEXT,
    category TEXT
);

CREATE TABLE ssbci_requests (
    request_id TEXT PRIMARY KEY,
    member_id TEXT,
    service_type TEXT,
    justification TEXT,
    cms_approved INTEGER,  -- 0/1
    status TEXT,           -- Pending / Assigned / Fulfilled
    vendor_id TEXT,
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

CREATE TABLE vendors (
    vendor_id TEXT PRIMARY KEY,
    name TEXT,
    service_category TEXT,
    status TEXT   -- Active / Pending review
);

CREATE TABLE mlr_tracking (
    period TEXT PRIMARY KEY,
    claims_pct REAL,
    quality_improvement_pct REAL,
    admin_pct REAL,
    margin_pct REAL
);

CREATE TABLE premium_changes (
    member_id TEXT,
    cost_driver TEXT,
    explanation TEXT,
    source TEXT,
    confidence TEXT,  -- High / Medium / Low
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);
""")

c.executemany("INSERT INTO members VALUES (?,?,?,?,?)", [
    ("M001", "Dorothy Klein", 71, 1, 42.50),
    ("M002", "Raymond Ortiz", 68, 0, 65.00),
    ("M003", "Alice Meyer", 76, 1, 10.00),
    ("M004", "Harold Nguyen", 65, 0, 75.00),
    ("M005", "Ruth Palmer", 82, 1, 0.00),
])

c.executemany("INSERT INTO lane1_benefits VALUES (?,?,?)", [
    ("B01", "Dental cleaning & exams", "Dental"),
    ("B02", "Annual vision exam + $150 frames allowance", "Vision"),
    ("B03", "Hearing aid fitting", "Hearing"),
    ("B04", "Wellness stipend", "Wellness"),
    ("B05", "Transportation to appointments", "Transportation"),
    ("B06", "Telehealth visits", "Telehealth"),
])

c.executemany("INSERT INTO ssbci_requests VALUES (?,?,?,?,?,?,?)", [
    ("R001", "M001", "Home modification (grab bars, ramp)", "Fall risk with COPD; reduces hospitalization risk", 1, "Assigned", "V02"),
    ("R002", "M003", "Meal delivery", "Diabetes management; supports diet adherence", 1, "Fulfilled", "V01"),
    ("R003", "M005", "Non-medical transportation (grocery)", "CHF; limited mobility, lives alone", 0, "Pending", None),
    ("R004", "M001", "Pest control", "Asthma trigger reduction", 1, "Pending", "V03"),
])

c.executemany("INSERT INTO vendors VALUES (?,?,?,?)", [
    ("V01", "Morgan County Meals Cooperative", "Meal delivery", "Active"),
    ("V02", "Fort Morgan Home Access LLC", "Home modification", "Active"),
    ("V03", "Prairie Pest Solutions", "Pest control", "Active"),
    ("V04", "Eastern Plains Rides", "Non-medical transportation", "Pending review"),
])

c.execute("INSERT INTO mlr_tracking VALUES (?,?,?,?,?)",
    ("2026-Q2", 82.5, 3.1, 10.4, 4.0))

c.executemany("INSERT INTO premium_changes VALUES (?,?,?,?,?)", [
    ("M001", "Claims trend", "Local claims costs rose slightly this year, mainly outpatient visits.", "Plan actuarial filing", "High"),
    ("M001", "SSBCI program funding", "A small share of your premium funds home/meal/transport support for members with qualifying chronic conditions.", "CMS SSBCI filing", "High"),
    ("M001", "Administrative costs", "Costs to run the plan at our current member size are estimated, not yet fully finalized.", "Internal estimate", "Medium"),
])

conn.commit()
conn.close()
print(f"Built {DB_PATH} with sample Morgan County co-op MA data")
