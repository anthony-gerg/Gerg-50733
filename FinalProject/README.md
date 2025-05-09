This subdir contains three files, outlined following:
Final_Computational_Physics.pdf - This is my writeup needed for the project, it outlines everything you would get by running the code, and is preferable as the code takes an awfully long time to run.

Main.py - This is the main n-body sim. I left the Sun,Mercury,Venus, and Saturn initial values inside. It is runnable in it's current state, though it will take an awful long time to run.
If you do want to run, I recommend lowering the timeframe, and increasing time step, and commenting out the matplotlib.use('Agg'), and changing the array sizes. Depending on what you are looking
for, you may need to change uncomment some lines or code out.

ThreeBodySteadyState.py - This is the same algorithm except with new initial values in, initial values to make a figure-eight. Simple as.
