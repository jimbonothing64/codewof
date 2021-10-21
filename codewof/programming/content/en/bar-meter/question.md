# Bar Meter
Write a function `def bar_meter(beats_per_bar, elapsed_beats)` that lets musicians preforming live know how many bars and beats they are into their song.
It should **return** a **string** with this information in this format `'{elapsed bars}.{beat in bar}'`.

- The elapsed bars are calculated as elapsed beats floor divided by beats per bar
- The current beat in the bar is calculated as elapsed beats modulo beats per bar

For example the following calls would return:

- `bar_meter(4, 1)` returns `'0.1'`
- `bar_meter(4, 4)` returns `'1.0'`
- `bar_meter(4, 5)` returns `'1.1'`
