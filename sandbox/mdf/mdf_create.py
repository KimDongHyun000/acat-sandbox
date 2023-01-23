import numpy as np

from asammdf import MDF, Signal

cycles = 100
sigs = []

mdf = MDF()

t = np.arange(cycles, dtype=np.float64)

# no conversion
sig = Signal(
    np.ones(cycles, dtype=np.uint64),
    t,
    name="Channel_no_conversion",
    unit="s",
    conversion=None,
    comment="Unsigned 64 bit channel {}",
)
sigs.append(sig)

mdf.append(sigs, comment="single dimensional channels", common_timebase=True)
mdf.save("demo.mf4", overwrite=True)
