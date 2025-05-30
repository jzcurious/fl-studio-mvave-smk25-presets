# name=M-VAVE SMK-25 (Preset 1)
# url=https://github.com/jzcurious/fl-studio-mvave-smk25-presets.git

from helpers import on_btn_push, on_knob_rotation
from transport import start, stop, record
from channels import setChannelVolume, channelCount

PLAY_BTN = 102
STOP_BTN = 103
REC_BTN = 104

KNOB1 = 20
KNOB2 = 21
KNOB3 = 22
KNOB4 = 23
KNOB5 = 24
KNOB6 = 25
KNOB7 = 26
KNOB8 = 27

ACTION_TABLE = {
    PLAY_BTN: lambda event: on_btn_push(event, start),
    STOP_BTN: lambda event: on_btn_push(event, stop),
    REC_BTN: lambda event: on_btn_push(event, record),
    KNOB1: lambda event: on_knob_rotation(
        event, lambda val: setChannelVolume(0, val), channelCount() >= 1
    ),
    KNOB2: lambda event: on_knob_rotation(
        event, lambda val: setChannelVolume(1, val), channelCount() >= 2
    ),
    KNOB3: lambda event: on_knob_rotation(
        event, lambda val: setChannelVolume(2, val), channelCount() >= 3
    ),
    KNOB4: lambda event: on_knob_rotation(
        event, lambda val: setChannelVolume(3, val), channelCount() >= 4
    ),
    KNOB5: lambda event: on_knob_rotation(
        event, lambda val: setChannelVolume(4, val), channelCount() >= 5
    ),
    KNOB6: lambda event: on_knob_rotation(
        event, lambda val: setChannelVolume(5, val), channelCount() >= 6
    ),
    KNOB7: lambda event: on_knob_rotation(
        event, lambda val: setChannelVolume(6, val), channelCount() >= 7
    ),
    KNOB8: lambda event: on_knob_rotation(
        event, lambda val: setChannelVolume(7, val), channelCount() >= 8
    ),
}


def OnMidiIn(event):
    action = ACTION_TABLE.get(event.data1)

    if action:
        action(event)

    event.handled = True
