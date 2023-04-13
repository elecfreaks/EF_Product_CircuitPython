import time
import board
import pwmio
import digitalio
import neopixel_write
import asyncio
from micropython import const

class WuKong2040:
    def __init__(self):
         self._ButtonA = digitalio.DigitalInOut(board.GP18)
         self._ButtonB = digitalio.DigitalInOut(board.GP19)
         
         self._M1A = pwmio.PWMOut(board.GP21, frequency=1000)
         self._M1B = pwmio.PWMOut(board.GP20, frequency=1000)
         
         self._M2A = pwmio.PWMOut(board.GP11, frequency=1000)
         self._M2B = pwmio.PWMOut(board.GP10, frequency=1000)
         
         self._M3A = pwmio.PWMOut(board.GP15, frequency=1000)
         self._M3B = pwmio.PWMOut(board.GP14, frequency=1000)
         
         self._M4A = pwmio.PWMOut(board.GP13, frequency=1000)
         self._M4B = pwmio.PWMOut(board.GP12, frequency=1000)
         
         self.neopixelpin = digitalio.DigitalInOut(board.GP22)
         self.neopixelpin.direction = digitalio.Direction.OUTPUT
         self.colorlist = [0, 0, 0, 0, 0, 0,]
         neopixel_write.neopixel_write(self.neopixelpin, bytearray(self.colorlist))
         
    def rainbow_led(self,num, red, green, blue):
        self.num = num
        self.red = red
        self.green = green
        self.blue = blue        
        if self.num == 0:
            self.colorlist[0] = self.green
            self.colorlist[1] = self.red
            self.colorlist[2] = self.blue 
            neopixel_write.neopixel_write(self.neopixelpin, bytearray(self.colorlist))
        if self.num == 1:
            self.colorlist[3] = self.green
            self.colorlist[4] = self.red
            self.colorlist[5] = self.blue 
            neopixel_write.neopixel_write(self.neopixelpin, bytearray(self.colorlist))
            
    def rainbow_all(self,red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
        self.colorlist[0] = self.green
        self.colorlist[1] = self.red
        self.colorlist[2] = self.blue
        self.colorlist[3] = self.green
        self.colorlist[4] = self.red
        self.colorlist[5] = self.blue 
        neopixel_write.neopixel_write(self.neopixelpin, bytearray(self.colorlist))

    def button_is_pressed(self, buttonName):
        self._buttonName = buttonName
        if self._buttonName == "ButtonA":
            if self._ButtonA.value == False:
                if self._ButtonB.value == True:
                    return True
        if self._buttonName == "ButtonB":
            if self._ButtonB.value == False:
                if self._ButtonA.value == True:
                    return True
        if self._buttonName == "ButtonAB":
            if self._ButtonA.value == False and self._ButtonB.value == False:
                time.sleep(0.1)
                if self._ButtonA.value == False and self._ButtonB.value == False:
                    return True
            
    def motor(self, motorNumber,speed):
        self._motorNumber = motorNumber
        self._speed = speed
        if self._motorNumber == "M1":
            if speed > 0:
                self._M1A.duty_cycle = speed * 655
                self._M1B.duty_cycle = 0
                
            if speed < 0:
                self._M1A.duty_cycle = 0
                self._M1B.duty_cycle = -speed * 655
                
            if speed == 0:
                self._M1A.duty_cycle = 0
                self._M1B.duty_cycle = 0
        
        if self._motorNumber == "M2":
            if speed > 0:
                self._M2A.duty_cycle = speed * 655
                self._M2B.duty_cycle = 0
                
            if speed < 0:
                self._M2A.duty_cycle = 0
                self._M2B.duty_cycle = -speed * 655
                
            if speed == 0:
                self._M2A.duty_cycle = 0
                self._M2B.duty_cycle = 0
        
        
        if self._motorNumber == "M3":
            if speed > 0:
                self._M3A.duty_cycle = speed * 655
                self._M3B.duty_cycle = 0
                
            if speed < 0:
                self._M3A.duty_cycle = 0
                self._M3B.duty_cycle = -speed * 655
                
            if speed == 0:
                self._M3A.duty_cycle = 0
                self._M3B.duty_cycle = 0
                
                
        if self._motorNumber == "M4":
            if speed > 0:
                self._M4A.duty_cycle = speed * 655
                self._M4B.duty_cycle = 0
                
            if speed < 0:
                self._M4A.duty_cycle = 0
                self._M4B.duty_cycle = -speed * 655
                
            if speed == 0:
                self._M4A.duty_cycle = 0
                self._M4B.duty_cycle = 0
                
    def motorStop(self, motorNumber):
        self._motorNumber = motorNumber
        if self._motorNumber == "M1":
            self._M1A.duty_cycle = 65535
            self._M1B.duty_cycle = 65535

        
        if self._motorNumber == "M2":
            self._M2A.duty_cycle = 65535
            self._M2B.duty_cycle = 65535
        
        
        if self._motorNumber == "M3":
            self._M3A.duty_cycle = 65535
            self._M3B.duty_cycle = 65535
                
                
        if self._motorNumber == "M4":
            self._M4A.duty_cycle = 65535
            self._M4B.duty_cycle = 65535


# SPDX-FileCopyrightText: Copyright ELECFREAKS
# SPDX-License-Identifier: MIT

"""
`Music`
====================================================
This is the `Music` class that you can use to play melodies through a buzzer
in CircuitPython. The library was inspired by the micro:bit `music` module.
"""




__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/elecfreaks/circuitpython_ef_music.git"


_ARTICULATION_MS = const(10)  # articulation between notes in milliseconds
_MIDDLE_FREQUENCIES = [
    const(440),
    const(494),
    const(262),
    const(294),
    const(330),
    const(349),
    const(392),
]
_MIDDLE_SHARPS_FREQUENCIES = [
    const(466),
    const(0),
    const(277),
    const(311),
    const(0),
    const(370),
    const(415),
]


class Music:
    """
    You can use the Music class to play melodies through a buzzer
    in CircuitPython.

    :param ~microcontroller.Pin pin: The buzzer pin.
    :param int ticks: A number of ticks constitute a beat. Defaults to 4.
    :param int bpm: Beats per minute. Defaults to 120.
    """

    DADADADUM = ["r4:2", "g", "g", "g", "eb:8", "r:2", "f", "f", "f", "d:8"]
    ENTERTAINER = [
        "d4:1", "d#", "e", "c5:2", "e4:1", "c5:2", "e4:1", "c5:3",
        "c:1", "d", "d#", "e", "c", "d", "e:2", "b4:1", "d5:2", "c:4"
    ]
    PRELUDE = [
        "c4:1", "e", "g", "c5", "e", "g4", "c5", "e", "c4", "e", "g", "c5",
        "e", "g4", "c5", "e", "c4", "d", "g", "d5", "f", "g4", "d5", "f",
        "c4", "d", "g", "d5", "f", "g4", "d5", "f", "b3", "d4", "g", "d5",
        "f", "g4", "d5", "f", "b3", "d4", "g", "d5", "f", "g4", "d5", "f",
        "c4", "e", "g", "c5", "e", "g4", "c5", "e", "c4", "e", "g", "c5",
        "e", "g4", "c5", "e"
    ]
    ODE = [
        "e4", "e", "f", "g", "g", "f", "e", "d", "c", "c", "d", "e",
        "e:6", "d:2", "d:8", "e:4", "e", "f", "g", "g", "f", "e",
        "d", "c", "c", "d", "e", "d:6", "c:2", "c:8"
    ]
    NYAN = [
        "f#5:2", "g#", "c#:1", "d#:2", "b4:1", "d5:1", "c#", "b4:2", "b",
        "c#5", "d", "d:1", "c#", "b4:1", "c#5:1", "d#", "f#", "g#", "d#",
        "f#", "c#", "d", "b4", "c#5", "b4", "d#5:2", "f#", "g#:1", "d#",
        "f#", "c#", "d#", "b4", "d5", "d#", "d", "c#", "b4", "c#5", "d:2",
        "b4:1", "c#5", "d#", "f#", "c#", "d", "c#", "b4", "c#5:2", "b4",
        "c#5", "b4", "f#:1", "g#", "b:2", "f#:1", "g#", "b", "c#5", "d#",
        "b4", "e5", "d#", "e", "f#", "b4:2", "b", "f#:1", "g#", "b", "f#",
        "e5", "d#", "c#", "b4", "f#", "d#", "e", "f#", "b:2", "f#:1", "g#",
        "b:2", "f#:1", "g#", "b", "b", "c#5", "d#", "b4", "f#", "g#", "f#",
        "b:2", "b:1", "a#", "b", "f#", "g#", "b", "e5", "d#", "e", "f#",
        "b4:2", "c#5"
    ]
    RINGTONE = [
        "c4:1", "d", "e:2", "g", "d:1", "e", "f:2", "a", "e:1", "f", "g:2",
        "b", "c5:4"
    ]
    FUNK = [
        "c2:2", "c", "d#", "c:1", "f:2", "c:1", "f:2", "f#", "g", "c", "c",
        "g", "c:1", "f#:2", "c:1", "f#:2", "f", "d#"
    ]
    BLUES = [
        "c2:2", "e", "g", "a", "a#", "a", "g", "e", "c2:2", "e", "g", "a",
        "a#", "a", "g", "e", "f", "a", "c3", "d", "d#", "d", "c", "a2",
        "c2:2", "e", "g", "a", "a#", "a", "g", "e", "g", "b", "d3", "f",
        "f2", "a", "c3", "d#", "c2:2", "e", "g", "e", "g", "f", "e", "d"
    ]
    BIRTHDAY = [
        "c4:3", "c:1", "d:4", "c:4", "f", "e:8", "c:3", "c:1", "d:4", "c:4",
        "g", "f:8", "c:3", "c:1", "c5:4", "a4", "f", "e", "d", "a#:3", "a#:1",
        "a:4", "f", "g", "f:8"
    ]
    WEDDING = [
        "c4:4", "f:3", "f:1", "f:8", "c:4", "g:3", "e:1", "f:8", "c:4", "f:3",
        "a:1", "c5:4", "a4:3", "f:1", "f:4", "e:3", "f:1", "g:8"
    ]
    FUNERAL = [
        "c3:4", "c:3", "c:1", "c:4", "d#:3", "d:1", "d:3", "c:1", "c:3",
        "b2:1", "c3:4"
    ]
    PUNCHLINE = [
        "c4:3", "g3:1", "f#", "g", "g#:3", "g", "r", "b", "c4"
    ]
    PYTHON = [
        "d5:1", "b4", "r", "b", "b", "a#", "b", "g5", "r", "d", "d", "r",
        "b4", "c5", "r", "c", "c", "r", "d", "e:5", "c:1", "a4", "r",
        "a", "a", "g#", "a", "f#5", "r", "e", "e", "r", "c", "b4", "r",
        "b", "b", "r", "c5", "d:5", "d:1", "b4", "r", "b", "b", "a#",
        "b", "b5", "r", "g", "g", "r", "d", "c#", "r", "a", "a", "r",
        "a", "a:5", "g:1", "f#:2", "a:1", "a", "g#", "a", "e:2", "a:1",
        "a", "g#", "a", "d", "r", "c#", "d", "r", "c#", "d:2", "r:3"
    ]
    BADDY = ["c3:3", "r", "d:2", "d#", "r", "c", "r", "f#:8"]
    CHASE = [
        "a4:1", "b", "c5", "b4", "a:2", "r", "a:1", "b", "c5", "b4",
        "a:2", "r", "a:2", "e5", "d#", "e", "f", "e", "d#", "e", "b4:1",
        "c5", "d", "c", "b4:2", "r", "b:1", "c5", "d", "c", "b4:2", "r",
        "b:2", "e5", "d#", "e", "f", "e", "d#", "e",
    ]
    BA_DING = ["b5:1", "e6:3"]
    WAWAWAWAA = ["e3:3", "r:1", "d#:3", "r:1", "d:4", "r:1", "c#:8"]
    JUMP_UP = ["c5:1", "d", "e", "f", "g"]
    JUMP_DOWN = ["g5:1", "f", "e", "d", "c"]
    POWER_UP = ["g4:1", "c5", "e", "g:2", "e:1", "g:3"]
    POWER_DOWN = ["g5:1", "d#", "c", "g4:2", "b:1", "c5:3"]

    def __init__(self, pin, ticks=4, bpm=120):
        self._ticks = ticks
        self._bpm = bpm
        self._octave = 4
        self._duration = 4
        self._pwm = pwmio.PWMOut(pin, frequency=1, variable_frequency=True)
        self._pwm.duty_cycle = 0
        self._playing = False

    def _tone(self, frequency):
        if frequency <= 0:
            self._pwm.duty_cycle = 0
        else:
            self._pwm.duty_cycle = 0x8000
            self._pwm.frequency = int(frequency)

    def _get_frequency_duration(self, note_str):
        note_split = note_str.lower().split(":")
        note = 'r'
        sharp = False
        note_index = 0

        if len(note_split) > 0:
            note = note_split[0]
        if len(note_split) > 1:
            try:
                self._duration = int(note_split[1])
            except ValueError as error:
                raise ValueError(
                    f"note '{note_str}' format is incorrect."
                ) from error

        # note(a, b, c, d, e, f, g, r), note_index(0, 1, 2, 3, 4, 5, 6, 17)
        note_index = ord(note[0]) - ord("a")
        if note_index < 0 or (note_index > 6 and note_index != 17):
            raise ValueError(f"note '{note_str}' format is incorrect.")

        # Like "c4", "c#" or "db"
        if len(note) == 2:
            try:
                # Like "c4"
                self._octave = int(note[1])
            except ValueError as error:
                # Like "c#" or "db"
                sharp = True
                if note[1] == "b" and note_index <= 6:
                    note_index -= 1
                elif note[1] != "#":
                    raise ValueError(
                        f"note '{note_str}' format is incorrect."
                    ) from error
        # Like "c#4"
        elif len(note) == 3:
            try:
                self._octave = int(note[2])
            except ValueError as error:
                raise ValueError(
                    f"note '{note_str}' format is incorrect."
                ) from error

            sharp = True
            if note[1] == "b" and note_index <= 6:
                note_index -= 1
            elif note[1] != "#":
                raise ValueError(f"note '{note_str}' format is incorrect.")
        elif len(note) != 1:
            raise ValueError(f"note '{note_str}' format is incorrect.")

        frequency = 0
        if note_index <= 6:
            shift_count = self._octave - 4
            if sharp:
                if shift_count > 0:
                    frequency = _MIDDLE_SHARPS_FREQUENCIES[note_index] \
                        << shift_count
                else:
                    frequency = _MIDDLE_SHARPS_FREQUENCIES[note_index] \
                        >> -shift_count
            else:
                if shift_count > 0:
                    frequency = _MIDDLE_FREQUENCIES[note_index] << shift_count
                else:
                    frequency = _MIDDLE_FREQUENCIES[note_index] >> -shift_count

        return [frequency, self._duration * (60000 / self._bpm / self._ticks)]

    def set_tempo(self, ticks=4, bpm=120):
        """Sets the approximate tempo for playback.

        :param int ticks: A number of ticks constitute a beat. Defaults to 4.
        :param int bpm: Beats per minute. Defaults to 120.
        """
        self._ticks = ticks
        self._bpm = bpm

    def get_tempo(self):
        """Gets the current tempo as a tuple of integers: (ticks, bpm).
        """
        return (self._ticks, self._bpm)

    def play(self, music):
        """Plays a melody.

        :param music: The musical DSL.
        """
        self._octave = 4
        self._duration = 4

        if not isinstance(music, (list, str)):
            raise TypeError("the music type must be a list or string.")

        if isinstance(music, str):
            frequency_duration = self._get_frequency_duration(music)
            self.pitch(frequency_duration[0], frequency_duration[1])
            return

        for note in music:
            if not isinstance(note, str):
                raise ValueError("the music contains unexpected element.")

            frequency_duration = self._get_frequency_duration(note)
            self.pitch(frequency_duration[0], frequency_duration[1])

    async def play_async(self, music):
        """Asynchronously plays a melody.

        :param music: The musical DSL.
        """
        self._octave = 4
        self._duration = 4
        self._playing = True

        if not isinstance(music, (list, str)):
            raise TypeError("the music type must be a list or string.")

        if isinstance(music, str):
            frequency_duration = self._get_frequency_duration(music)
            await self.pitch_async(
                frequency_duration[0], frequency_duration[1]
            )
            return

        for note in music:
            if not isinstance(note, str):
                raise ValueError("the music contains unexpected element.")

            if not self._playing:
                break

            frequency_duration = self._get_frequency_duration(note)
            await self.pitch_async(
                frequency_duration[0], frequency_duration[1]
            )

        self._playing = False

    def pitch(self, frequency, duration=-1):
        """Plays a pitch at the integer frequency given for the specified
        number of milliseconds.

        :param int frequency: The specified frequency.
        :param int duration: The specified duration.
        """
        self._tone(frequency)
        if duration >= 0:
            duration -= _ARTICULATION_MS
            if duration < 0:
                duration = 10
            time.sleep(duration / 1000)
            self._tone(0)
            time.sleep(_ARTICULATION_MS / 1000)

    async def pitch_async(self, frequency, duration=-1):
        """Asynchronously plays a pitch at the integer frequency given for the
        specified number of milliseconds.

        :param int frequency: The specified frequency.
        :param int duration: The specified duration.
        """
        self._tone(frequency)
        if duration >= 0:
            duration -= _ARTICULATION_MS
            if duration < 0:
                duration = 10
            await asyncio.sleep(duration / 1000)
            self._tone(0)
            await asyncio.sleep(_ARTICULATION_MS / 1000)

    def stop(self):
        """Stops the music playback.
        In fact, works only for `play_async(music)`.
        """
        self._playing = False

    def reset(self):
        """Resets to default state.
        """
        self._ticks = 4
        self._bpm = 120
        self._octave = 4
        self._duration = 4




music = Music(board.GP9)
       

