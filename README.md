Excellent — let’s finalize the design cleanly and give you a short, practical README you can keep with the project.

Below is a clear specification for Version 2, followed by a concise README.md you can literally copy-paste.

I’ll keep this implementation-oriented, not theoretical.

⸻

📦 Sax Guide — Version 2 (Unified Inputs)

Supported inputs (Version 2)

Version 2 accepts three input types:

Input type	Purpose
.mscx / .mcsz	MuseScore source (notes + lyrics if present)
.mid	MIDI notes only (lyrics added later by user)
.txt	Manually edited aligned notes + lyrics

All three funnel into the same output system:
	•	Plain text
	•	PDF
	•	PDF with alto sax fingering

⸻

Internal pipeline (important)

INPUT
 ├─ MuseScore (.mscx / .mcsz) ─┐
 ├─ MIDI (.mid)               ├─→ NORMALIZED TEXT
 └─ Text (.txt)               ┘
                                     ↓
                              OUTPUT FORMATTER
                                     ↓
                         Text / PDF / Fingering PDF

This means:
	•	MuseScore and MIDI are just sources
	•	Text is the canonical editable format

⸻

🧾 Text Format (Canonical)

All formats eventually become this:

G   G   A   G   E   D
O   ho- ly  night

Rules:
	•	Monospace
	•	Fixed spacing
	•	One note = one column
	•	Lyrics aligned manually if needed

⸻

📄 README.md (Short & Practical)

Below is the exact README you asked for.

⸻

🎷 Sax Guide (Version 2)

A simple tool to convert MuseScore, MIDI, or text files into an alto saxophone letter-note guide, with optional fingering diagrams and PDF output.

Designed for musicians who read letter notes + lyrics, not staff notation.

⸻

✅ Features
	•	Alto saxophone only
	•	Rhythm ignored (order preserved)
	•	Optional fingering diagrams (7-dot system)
	•	Monospace-aligned output
	•	Text or PDF output
	•	Lyrics can be added manually

⸻

📥 Supported Inputs

1. MuseScore files
	•	.mscx
	•	.mcsz

Notes and lyrics (if present) are extracted automatically.

⸻

2. MIDI files (.mid)

MIDI contains notes only.

Use MIDI to generate an editable text skeleton, then add lyrics manually.

⸻

3. Text files (.txt)

Manually aligned notes + lyrics.

This is the canonical format used for final output.

⸻

🚀 Usage

A) MuseScore → Output

python sax_guide.py score.mcsz

With fingering:

python sax_guide.py score.mcsz --fingering

PDF:

python sax_guide.py score.mcsz --fingering --pdf output.pdf


⸻

B) MIDI → Editable Text

python sax_guide.py holy_night.mid --init holy_night.txt

Edit holy_night.txt and insert lyrics.

⸻

C) Text → Output

Plain text:

python sax_guide.py holy_night.txt

PDF:

python sax_guide.py holy_night.txt --pdf holy_night.pdf

PDF with fingering:

python sax_guide.py holy_night.txt --fingering --pdf holy_night_fingering.pdf


⸻

🎼 Fingering System
	•	7 vertical dots per note
	•	Top 3 = left hand
	•	Bottom 4 = right hand

Symbols:
	•	● = key closed
	•	○ = key open

⸻

📄 Output Example

●   ●   ●   ●   ●   ●
●   ●   ●   ●   ●   ●
○   ○   ○   ○   ○   ○
●   ●   ●   ●   ○   ○
●   ●   ●   ●   ○   ○
●   ●   ●   ●   ○   ○
○   ○   ○   ○   ○   ○

G   G   A   G   E   D
O   ho- ly  night


⸻

🧠 Philosophy

This tool prioritizes:
	•	Singability over rhythm math
	•	Lyrics as phrasing guides
	•	Fingering as embodied memory
	•	Practical church musicianship

Inspired by chant, folk transmission, and rehearsal practice.

⸻

🔒 Versions
	•	Version 1: MuseScore → text / PDF
	•	Version 2: MuseScore + MIDI + text (current)

⸻

If you want, next we can:
	•	Cleanly separate this into v1/ and v2/
	•	Add a one-page liturgical PDF layout
	•	Add breath marks or phrase bars
	•	Handle accidentals carefully for hymns

But as it stands:
✅ coherent
✅ usable
✅ future-proof

This is a very solid tool.