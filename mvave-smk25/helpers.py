def print_event(event):
    print(
        f"handled:      {event.handled}\n"
        f"timestamp:    {event.timestamp}\n"
        f"status:       {event.status}\n"
        f"data1:        {event.data1}\n"
        f"data2:        {event.data2}\n"
        f"port:         {event.port}\n"
        f"note:         {event.note}\n"
        f"velocity:     {event.velocity}\n"
        f"pressure:     {event.pressure}\n"
        f"progNum:      {event.progNum}\n"
        f"controlNum:   {event.controlNum}\n"
        f"controlVal:   {event.controlVal}\n"
        f"pitchBend:    {event.pitchBend}\n"
        f"sysex:        {event.sysex}\n"
        f"isIncrement:  {event.isIncrement}\n"
        f"res:          {event.res}\n"
        f"inEv:         {event.inEv}\n"
        f"outEv:        {event.outEv}\n"
        f"midiId:       {event.midiId}\n"
        f"midiChan:     {event.midiChan}\n"
        f"midiChanEx:   {event.midiChanEx}\n"
    )


def on_btn_push(event, callback):
    if event.data2 == 127:
        callback()


def on_knob_rotation(event, callback, condition=True, limit=128):
    if event.data2 < limit and condition:
        callback(event.data2 / 127)
