from plotnine import *
from plotnine.data import *
import pandas as pd

def combine(counts, percentages):
    fmt = '{} ({:.1f}%)'.format
    return [fmt(c, p) for c, p in zip(counts, percentages)]

(
    ggplot(mtcars, aes('factor(cyl)', fill='factor(cyl)'))
    + geom_bar()
    + geom_text(
        aes(label=after_stat('combine(count, prop*100)'), group=1),
        stat='count',
        nudge_y=0.125,
        va='bottom',
        size=9
    )
    + facet_wrap('am')
)