# news-image-01 — The World Today: Friday 13 November 2026

One image summing up the world's news of Friday 13 November 2026, drawn as
a newspaper front page: a header with the date, six illustrated stories in a
2×3 grid, each with a short bold caption, and an "Also today" strip with
three more stories. All six panels were generated fresh as text-free
illustrations after the competition opened; all wording was added afterwards
in crisp type so every label is spelled correctly and legible. The panel
showing the Gulf strikes was regenerated so the missile itself reads clearly
in the frame, not just a smoke trail.

## The six stories (top to bottom, left to right)

1. **Senate summons ex-Nvidia chief** — Nvidia founder Jensen Huang resigned
   as chief executive on Thursday after reports of an affair with a woman
   alleged to be a Chinese spy; shares fell about 16%. The US Senate
   summoned Huang and Commerce Secretary Lutnick to testify.
   Sources: BBC News, Al Jazeera, 13 Nov 2026.
2. **Europe joins peace talks** — After US envoys Witkoff and Kushner met
   Putin in Moscow and Zelenskyy near Dublin, Russia agreed to European
   participation in the next round of Ukraine negotiations, and the sides
   planned what was described as the war's largest prisoner exchange.
   Sources: AP, BBC News, Al Jazeera, 13 Nov 2026.
3. **Drone hits Russian warship** — Ukraine's security service said it struck
   the Baltic Fleet corvette Naro-Fominsk in the Gulf of Finland; Finland's
   defence forces confirmed detecting a strike on a Russian warship near
   Gogland island.
   Sources: BBC News, Reuters / Yle, 13 Nov 2026.
4. **Iran claims Gulf strikes** — Iran said it struck a US radar site in
   Bahrain, and reported an LNG tanker hitting a naval mine in the Strait of
   Hormuz; a separate projectile attack on a tanker was confirmed by UKMTO.
   Sources: Al Jazeera, 13 Nov 2026.
5. **Microsoft outage goes global** — Microsoft 365, Outlook, Teams and
   Copilot went down worldwide for hours, with outage reports peaking near
   140,000; users in the US, Japan, Australia and India were affected.
   Sources: BBC News, 13 Nov 2026.
6. **Strike hits Gaza hospital** — An Israeli strike on the al-Yasin surgical
   building at Nasser Hospital in Khan Younis killed six people, including a
   general surgeon, and wounded twenty.
   Sources: AP / health authorities, 13 Nov 2026.

## Also today (footer strip)

- FBI: North Korean hackers linked to a $400m crypto theft carried out
  through fake video calls (BBC News, 13 Nov 2026).
- US reports a record 483,200 deportations in 2026 (Al Jazeera, 13 Nov 2026).
- Indonesia's vice president Gibran Rakabuming Raka resigns to avoid
  impeachment after court rulings challenged his education credentials —
  the first VP resignation since 1998 (Reuters, 13 Nov 2026).

## How the program works

`main.py` (Python 3.13 standard library only) copies `entry.png`, held in
this repository, to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`).
It reads no network and writes the same bytes on every run, so two runs
produce byte-identical output. After copying, it verifies the copy by
comparing the SHA-256 digest of the source and the destination, and fails
loudly if they ever differ — so a truncated or corrupted copy can never
pass as the entry.
