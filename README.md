# FakeInk
I bought Off-Brand Ink and now Lexmark asks to confirm every print job individually


This (Create a Shortcut to START.bat, set it to start minimized)
will click on any image specified in *targets* variable as soon as any ongoing print job is detected.

In *idle* it will consume 2% Cpu, this could be lowered by having a lower poll rate (last line)

The 25s delay in line 21 is to prevent the imagesearch while printing. Otherwise it would use 14% CPU during print as Image is continously searching
