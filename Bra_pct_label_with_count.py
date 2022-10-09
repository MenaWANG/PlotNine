from plotnine import *
from plotnine.data import *
import pandas as pd

(
    ggplot(mtcars, aes('factor(cyl)', fill='factor(cyl)'))
    + geom_bar()
    + geom_text(
        aes(label=after_stat('count / sum(count) * 100')),
        stat='count',
        nudge_y = 0.125,
        va='bottom',
        format_string='{:.1f}%'
            )
    + theme_minimal()
)