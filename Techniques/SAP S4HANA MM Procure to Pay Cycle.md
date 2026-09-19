---
tags:
  - Technique
  - SAP
areas:
  - "[[Career Pivot - SAP S4HANA MM & MBA Logistics]]"
last updated: 2026-09-19
---

# SAP S/4HANA MM — Procure to Pay (P2P) Cycle

> [!info] Core Enterprise Process
> The end-to-end procurement process in SAP S/4HANA Materials Management, from initial demand determination to invoice settlement.

## The 8 P2P Steps

```
[Determination of Requirements]
              ↓
  [Source Determination (RFQ)]
              ↓
     [Vendor Selection]
              ↓
    [Purchase Order (PO)]
              ↓
     [PO Monitoring]
              ↓
  [Goods Receipt (MIGO)]
              ↓
[Invoice Verification (MIRO)]
              ↓
      [Payment Processing]
```

### 1. Purchase Requisition (PR)
- Internal request to purchase goods or services.
- T-Codes: `ME51N` (Create), `ME52N` (Change), `ME53N` (Display).

### 2. Purchase Order (PO)
- Legally binding contract sent to the external vendor specifying quantity, price, delivery terms, and plant.
- T-Codes: `ME21N` (Create), `ME22N` (Change), `ME23N` (Display).

### 3. Goods Receipt (GR)
- Physical arrival of materials at plant/warehouse.
- T-Code: `MIGO`.
- Movement Type: `101` (Goods receipt into warehouse). Updates inventory quantity and stock valuation in real-time.

### 4. Invoice Verification (LIV)
- Three-way match: PO vs. Goods Receipt vs. Vendor Invoice.
- T-Code: `MIRO`.
- Checks for discrepancies in quantities and price before releasing for payment.

## Related Notes
- Career Goal: [[Career Pivot - SAP S4HANA MM & MBA Logistics]]
- Profile: [[About Dhruv - Identity & Career]]
