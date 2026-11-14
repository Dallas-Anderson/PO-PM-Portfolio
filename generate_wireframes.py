#!/usr/bin/env python3
"""
Dev agent (prototype version): takes backlog items + the co-op MA dataset
and renders low-fi grayscale HTML wireframes - layout/structure only,
no real styling, no color. One wireframe per core screen.

This is hand-authored for the first end-to-end pass; the generalized dev
agent will do this same read -> render step via an LLM call per backlog
item, same as ledger_to_backlog.py does for the PO agent.
"""
import sqlite3
from pathlib import Path

DB_PATH = Path("/home/claude/dev_agent/coop_health.db")
OUT_DIR = Path("/home/claude/dev_agent/wireframes")
OUT_DIR.mkdir(exist_ok=True)

conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row

WIREFRAME_CSS = """
<style>
  * { box-sizing: border-box; }
  body { font-family: Arial, Helvetica, sans-serif; background: #fff; color: #000;
         margin: 0; padding: 24px; }
  .frame-label { font-size: 11px; color: #666; text-transform: uppercase;
                 letter-spacing: 0.05em; margin-bottom: 4px; }
  h1 { font-size: 18px; font-weight: bold; margin: 0 0 4px 0; }
  .subtitle { font-size: 12px; color: #666; margin-bottom: 20px; }
  .box { border: 1px solid #000; padding: 12px; margin-bottom: 12px; background: #f5f5f5; }
  .box-header { font-weight: bold; font-size: 13px; margin-bottom: 8px;
                border-bottom: 1px solid #999; padding-bottom: 4px; }
  .placeholder-block { border: 1px dashed #999; background: #eee; height: 14px;
                        margin: 4px 0; }
  .nav { border: 1px solid #000; padding: 8px 12px; margin-bottom: 16px;
         font-size: 12px; background: #ddd; display: flex; gap: 16px; }
  .nav span { border: 1px solid #999; padding: 2px 8px; background: #fff; }
  table { width: 100%; border-collapse: collapse; font-size: 12px; }
  th, td { border: 1px solid #999; padding: 6px 8px; text-align: left; }
  th { background: #ddd; font-weight: bold; }
  .tag { display: inline-block; border: 1px solid #666; padding: 1px 6px;
         font-size: 10px; background: #fff; }
  .tag-pending { background: #eee; }
  .tag-active, .tag-fulfilled, .tag-approved { background: #ccc; }
  .btn { display: inline-block; border: 1px solid #000; padding: 4px 10px;
         font-size: 12px; background: #ddd; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
  .footer-note { font-size: 10px; color: #999; margin-top: 24px; border-top: 1px solid #ccc;
                 padding-top: 8px; }
</style>
"""

NAV = '<div class="nav"><span>Member portal</span><span>Case management</span><span>Vendor network</span><span>Compliance</span></div>'


def page(title, subtitle, feature_ref, body_html):
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title}</title>{WIREFRAME_CSS}</head>
<body>
<div class="frame-label">Low-fi wireframe - layout only</div>
{NAV}
<h1>{title}</h1>
<div class="subtitle">{subtitle} &nbsp;|&nbsp; Backlog: {feature_ref}</div>
{body_html}
<div class="footer-note">Wireframe generated from coop_health.db - Morgan County co-op MA pilot dataset. Structure/layout only, not final visual design.</div>
</body></html>"""


# ---------- 1. Member benefits overview (F001) ----------
member = conn.execute("SELECT * FROM members WHERE member_id='M001'").fetchone()
benefits = conn.execute("SELECT * FROM lane1_benefits").fetchall()

rows = "".join(
    f'<tr><td>{b["name"]}</td><td>{b["category"]}</td><td><span class="tag tag-active">Included</span></td></tr>'
    for b in benefits
)
body = f"""
<div class="box">
  <div class="box-header">Member: {member['name']} (ID {member['member_id']})</div>
  <div class="grid-2">
    <div>Wellness stipend balance: <b>${member['wellness_stipend_balance']:.2f}</b></div>
    <div><span class="btn">Redeem stipend</span></div>
  </div>
</div>
<div class="box">
  <div class="box-header">Your Lane 1 benefits (included for every member)</div>
  <table><tr><th>Benefit</th><th>Category</th><th>Status</th></tr>{rows}</table>
</div>
"""
Path(OUT_DIR / "01_member_benefits_overview.html").write_text(
    page("Member benefits overview", "Lane 1 uniform supplemental benefits", "F001", body)
)


# ---------- 2. SSBCI case manager workflow (F002) ----------
requests = conn.execute("""
    SELECT r.*, m.name as member_name FROM ssbci_requests r
    JOIN members m ON m.member_id = r.member_id
""").fetchall()

rows = ""
for r in requests:
    approved_tag = '<span class="tag tag-approved">CMS approved</span>' if r["cms_approved"] else '<span class="tag tag-pending">Pending CMS</span>'
    status_tag = f'<span class="tag tag-{r["status"].lower()}">{r["status"]}</span>'
    rows += f"""<tr>
      <td>{r['member_name']}</td>
      <td>{r['service_type']}</td>
      <td style="max-width:220px">{r['justification']}</td>
      <td>{approved_tag}</td>
      <td>{status_tag}</td>
      <td>{r['vendor_id'] or '-'}</td>
    </tr>"""

body = f"""
<div class="box">
  <div class="box-header">SSBCI eligibility assessment</div>
  <div class="placeholder-block" style="width:60%"></div>
  <div class="placeholder-block" style="width:40%"></div>
  <span class="btn">New assessment</span>
</div>
<div class="box">
  <div class="box-header">Targeted benefit requests</div>
  <table><tr><th>Member</th><th>Service</th><th>Justification</th><th>CMS status</th><th>Fulfillment</th><th>Vendor</th></tr>{rows}</table>
</div>
"""
Path(OUT_DIR / "02_ssbci_case_manager.html").write_text(
    page("SSBCI case manager workspace", "Lane 2 targeted chronic-illness benefits", "F002", body)
)


# ---------- 3. Vendor network (F003) ----------
vendors = conn.execute("SELECT * FROM vendors").fetchall()
rows = "".join(
    f'<tr><td>{v["name"]}</td><td>{v["service_category"]}</td>'
    f'<td><span class="tag tag-{"active" if v["status"]=="Active" else "pending"}">{v["status"]}</span></td></tr>'
    for v in vendors
)
body = f"""
<div class="box">
  <div class="box-header">Morgan County vendor & nonprofit network</div>
  <table><tr><th>Vendor</th><th>Service category</th><th>Status</th></tr>{rows}</table>
  <div style="margin-top:8px"><span class="btn">Onboard new vendor</span></div>
</div>
<div class="box">
  <div class="box-header">Match request to vendor</div>
  <div class="placeholder-block" style="width:50%"></div>
  <span class="btn">Assign vendor</span>
</div>
"""
Path(OUT_DIR / "03_vendor_network.html").write_text(
    page("Local vendor & nonprofit network", "Sourcing Lane 2 services locally", "F003", body)
)


# ---------- 4. Compliance / MLR dashboard (F004) ----------
mlr = conn.execute("SELECT * FROM mlr_tracking WHERE period='2026-Q2'").fetchone()
pending_filings = sum(1 for r in requests if not r["cms_approved"])
mlr_total = mlr["claims_pct"] + mlr["quality_improvement_pct"]
body = f"""
<div class="box">
  <div class="box-header">MLR compliance - {mlr['period']}</div>
  <table>
    <tr><th>Claims + quality improvement</th><td>{mlr_total:.1f}%</td></tr>
    <tr><th>Administration</th><td>{mlr['admin_pct']:.1f}%</td></tr>
    <tr><th>Reserves / margin</th><td>{mlr['margin_pct']:.1f}%</td></tr>
    <tr><th>85% regulatory floor</th><td>{'<span class="tag tag-active">Above floor</span>' if mlr_total >= 85 else '<span class="tag tag-pending">Below floor - alert</span>'}</td></tr>
  </table>
</div>
<div class="box">
  <div class="box-header">CMS filing status</div>
  <div>SSBCI benefit designs pending CMS approval: <b>{pending_filings}</b></div>
  <div class="placeholder-block" style="width:70%"></div>
  <span class="btn">View filing queue</span>
</div>
"""
Path(OUT_DIR / "04_compliance_mlr_dashboard.html").write_text(
    page("Compliance dashboard", "CMS filing tracker + real-time MLR monitoring", "F004", body)
)


# ---------- 5. Premium transparency (F005) ----------
changes = conn.execute("SELECT * FROM premium_changes WHERE member_id='M001'").fetchall()
rows = ""
for pc in changes:
    rows += f"""<div class="box">
      <div class="box-header">{pc['cost_driver']} &nbsp; <span class="tag">{pc['confidence']} confidence</span></div>
      <div>{pc['explanation']}</div>
      <div style="font-size:11px;color:#666;margin-top:4px">Source: {pc['source']}</div>
    </div>"""

body = f"""
<div class="box">
  <div class="box-header">Your premium change this year, explained</div>
  <div>Member: {member['name']}</div>
</div>
{rows}
"""
Path(OUT_DIR / "05_premium_transparency.html").write_text(
    page("Premium transparency notice", "Evidence Ledger-style member disclosure", "F005", body)
)

print(f"Wrote {len(list(OUT_DIR.glob('*.html')))} wireframes to {OUT_DIR}")
