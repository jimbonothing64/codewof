def bar_meter(beats_per_bar, elapsed_beats):
    bars = elapsed_beats // beats_per_bar
    beats = elapsed_beats % beats_per_bar
    return f"{bars}.{beats}"
