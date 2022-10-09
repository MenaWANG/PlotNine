from plotnine import *
from plotnine.data import *
import pandas as pd

mtcars.head(5)

(
    ggplot(mtcars, aes(x='factor(cyl)', fill = 'factor(cyl)'))
    + geom_bar()
    + geom_text(
        aes(label = after_stat('count'/sum('count')),group=1),
        stat = 'count',
        nudge_y = 0.125,
        va = 'bottom',
        format_string = '{:.1f}%'
        )
    + theme_minimal()
)

