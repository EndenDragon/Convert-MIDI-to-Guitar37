# Convert MIDI to Guitar37
UW CSE 143 Guitar37 assignment.
Convert a MIDI file to be able to played on a Guitar37.

## Instructions
1. Install the required mido package from pypi
2. Make sure you are on Python 2.7 ish. Python 3 has not been tested.
3. Place a midi file in the directory of the python file
4. Run the following command `python convert_midi_to_guitar37.py <filename> <speed_modifier>` Replacing the midi file name and speed modifier. The speed modifier determines how fast/slow each notes are played. The higher, the slower. Default is at 1.
5. There should be an `output` folder. Open that and there are the extracted midi tracks.
6. Congrats, you can open up the `PlayThatTune.java` file and point to one of the .txt tracks to play!

## Limitations
Please understand the limitations that this converter imposes. There must be only one role of notes per track (eg no two or more notes must be playing at the same time). Also, the notes in the midi must be at a specific range of delta 37 from the highest to the lowest note. This is because that the guitar37 can only handle 37 notes.

## Contributions
I welcome those who want to contribute to this project. Get started by hitting me with pull requests or notifying me of problems by creating an issue. Remember, when creating an issue, please provide me a download of the midi file you have worked with so I may use that to debug the code. Also keep in mind that your Guitar37 class must be working. I cannot provide you the code for it myself, though here are the writeup that you should follow to create your guitar37 class. http://courses.cs.washington.edu/courses/cse143/17wi/handouts/03.html
