#!/usr/bin/env python
"""
Open a MIDI file and stores the Guitar37 data in the output folder. Each
tracks of the MIDI file are a seperate file.
Needs: Python 2.7
Run: python convert_midi_to_guitar37.py <filename> <speed_modifier>
Dependancies: mido
"""
import sys, os
from mido import MidiFile


filename = sys.argv[1]
speed_modifier = sys.argv[2]

midi_file = MidiFile(filename)

folder = "output"
print(folder)
if not os.path.exists(folder):
    os.mkdir(folder)

class Note:
    note = 0
    time = 0
    def __init__(self, note, time):
        self.note = note
        self.time = time

for i, track in enumerate(midi_file.tracks):
    with open('{dir}/{filename}_track_{track}.txt'.format(dir=folder, filename=filename, track=i), 'w+') as file:
        notes = []

        # given a note, change the duration from zero to something different
        def assignDurationToNote(noteparam, duration):
            for note in notes:
                if note.time == 0 and note.note == noteparam:
                    note.time = duration
                    return

        lowest_note = 127;
        highest_note = 0;

        for message in track:
            if message.type == 'note_on':
                if message.note < lowest_note:
                    lowest_note = message.note
                if message.note > highest_note:
                    highest_note = message.note
                aNote = Note(message.note, message.time)
                notes.append(aNote)
            elif message.type == 'note_off':
                assignDurationToNote(message.note, message.time)

        midi_mid = 127.0/2 # middle of the midi range
        percentage = (lowest_note - midi_mid) / 127 # the percentage of the gap between lowest note and midi mid value
        gap_delta = 37 * percentage # gap between middle of guitar37 and lowest note
        new_lowest_note = -6 + gap_delta # lowest note on the guitar range

        for note in notes:
            d = abs(lowest_note - note.note) + new_lowest_note
            file.write( str(int(round(d))) + "  " + str((note.time/float(1000))*float(speed_modifier)) + "\n" )
