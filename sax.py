import argparse
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import mido

NOTE_WIDTH = 4
DOT_OPEN = "○"
DOT_CLOSED = "●"

FINGERINGS = {
    "C": [DOT_OPEN, DOT_OPEN, DOT_OPEN, DOT_CLOSED, DOT_OPEN, DOT_OPEN, DOT_OPEN],
    "D": [DOT_CLOSED, DOT_CLOSED, DOT_CLOSED, DOT_CLOSED, DOT_CLOSED, DOT_CLOSED, DOT_OPEN],
    "E": [DOT_CLOSED, DOT_CLOSED, DOT_CLOSED, DOT_OPEN, DOT_OPEN, DOT_OPEN, DOT_OPEN],
    "F": [DOT_CLOSED, DOT_CLOSED, DOT_CLOSED, DOT_OPEN, DOT_CLOSED, DOT_CLOSED, DOT_OPEN],
    "G": [DOT_CLOSED, DOT_CLOSED, DOT_OPEN, DOT_CLOSED, DOT_CLOSED, DOT_CLOSED, DOT_OPEN],
    "A": [DOT_CLOSED, DOT_CLOSED, DOT_OPEN, DOT_CLOSED, DOT_CLOSED, DOT_OPEN, DOT_OPEN],
    "B": [DOT_CLOSED, DOT_OPEN,  DOT_OPEN,  DOT_CLOSED, DOT_OPEN,  DOT_OPEN,  DOT_OPEN],
}

NOTE_NAMES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

def midi_to_notes(midi_path):
    midi = mido.MidiFile(midi_path)
    notes = []

    for msg in midi.tracks[0]:
        if msg.type == "note_on" and msg.velocity > 0:
            name = NOTE_NAMES[msg.note % 12].replace("#", "")
            notes.append(name)

    return notes

def write_skeleton(notes, path):
    notes_line = "".join(n.ljust(NOTE_WIDTH) for n in notes)
    lyrics_line = "".join("_".ljust(NOTE_WIDTH) for _ in notes)
    path.write_text(notes_line + "\n" + lyrics_line)

def read_text(path):
    lines = path.read_text().splitlines()
    return lines[0], lines[1]

def format_output(notes_line, lyrics_line, fingering=False):
    notes = [notes_line[i:i+NOTE_WIDTH].strip()
             for i in range(0, len(notes_line), NOTE_WIDTH)]

    rows = []

    if fingering:
        fingering_rows = [""] * 7
        for n in notes:
            if n in FINGERINGS:
                for i in range(7):
                    fingering_rows[i] += FINGERINGS[n][i].ljust(NOTE_WIDTH)
        rows.extend(fingering_rows)
        rows.append("")

    rows.append(notes_line)
    rows.append(lyrics_line)
    return rows

def write_pdf(lines, output):
    c = canvas.Canvas(str(output), pagesize=A4)
    c.setFont("Courier", 12)

    y = 800
    for line in lines:
        c.drawString(40, y, line)
        y -= 16
    c.save()

def main():
    parser = argparse.ArgumentParser("Sax Guide v2")
    parser.add_argument("input")
    parser.add_argument("--init", help="Create editable text from MIDI")
    parser.add_argument("--fingering", action="store_true")
    parser.add_argument("--pdf")

    args = parser.parse_args()
    path = Path(args.input)

    if path.suffix == ".mid":
        notes = midi_to_notes(path)
        write_skeleton(notes, Path(args.init))
        return

    notes_line, lyrics_line = read_text(path)
    lines = format_output(notes_line, lyrics_line, args.fingering)

    if args.pdf:
        write_pdf(lines, args.pdf)
    else:
        print("\n".join(lines))

if __name__ == "__main__":
    main()