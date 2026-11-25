# Crossed Threads — Changelog

All releases are tracked here. The live version is in `version.json`; the
running version is shown in the app under **Settings → About**.

## 1.5.0 — 2026-11-25

- **Factory default PIN changed from 1234 to 2202** for fresh installs and for
  data created by “Delete All App Data”.
- Existing installations keep their current PIN; the update does not change it.
- Default-PIN warnings now cover 2202 and 1234, with a reminder that the factory
  default is public and a personal 5–6 digit PIN is stronger.
- PIN recovery codes remain available and unchanged.

## 1.4.0 — 2026-11-25

- **PIN recovery code:** if the PIN is forgotten, the lock screen now has a
  **Forgot PIN?** option. A 16-character one-time code lets you set a new PIN
  without losing invoices or settings.
- Only a SHA-256 hash of the recovery code is stored; the code itself is never
  saved in the app.
- Recovery codes are shown once when created or when the PIN is changed, with
  Copy and Download options.
- Settings → Security & App Lock shows whether a recovery code is set and lets
  you create or replace it.
- The recovery code is rotated after every PIN recovery; the old code stops
  working immediately.

## 1.3.1 — 2026-11-25

- **Update tracking:** “Check for Updates” now reads `version.json` from the
  deployed site and compares it with the running app version.
- **Update alert:** when a newer release exists, Home → Needs Attention shows
  “Update available”, with release notes and a Reload & Update button.
- **What’s New:** release notes can be viewed in Settings → About.
- **Service worker:** cache bumped and page loads revalidate so a fresh deploy
  is picked up faster.

## 1.3.0 — 2026-11-25

- Two invoice templates: **Classic** (original) and **Modern** (navy & gold),
  selectable in Settings.
- Strictly **one-page A4 PDF** for Download PDF and sharing.
- Smaller, print-safe rubber stamp; fixed the stamp not appearing on paper.
- **Products & Services CRUD:** add, edit, archive, restore, delete forever.
- **PIN 4–6 digits** with strength warning and a Home alert while the default
  `1234` is still in use.
- **Project type** dropdown: Vehicle, Boat, Upholstery Project, Custom Interior,
  with dynamic field labels printed on invoices.
- Mobile item table made easier to use; invoice form totals now initialise
  correctly.

## 1.2.0 — 2026-11-24

- Home dashboard: period filters (Today / This Month / Last Month / This Year),
  KPI tiles, outstanding/overdue strip, Needs Attention queue and backup
  reminder.
- **Job stages:** New → Deposit → Materials → Workshop → Ready → Delivered,
  editable from the invoice and from Home.
- Share invoices/quotations as a real JPG image or PDF document through the
  device share sheet; plain-text sharing remains available.

## 1.1.0 — 2026-11-24

- Fixed invoice and quote deletion (confirmation callbacks now keep their
  scope).
- Delete actions on document cards and detail pages; customer deletion.
- Settings → Delete Data: clear invoices/quotes, customers, catalogue,
  expenses, or erase everything with typed confirmation.
- Add to Home Screen install flow for Android, iOS and desktop; new icon set.

## 1.0.0 — 2026-11-23

- Initial offline invoicing app with customers, invoices, quotes, payments,
  expenses, catalogue, PDF/print, settings, PIN lock and backups.
