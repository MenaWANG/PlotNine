from plotnine import *
import pandas as pd
from plotnine.data import *

mtcars.head()

(
    ggplot(mtcars, aes(x='factor(cyl)', fill='factor(cyl)'))
    + geom_bar()
    + geom_text(
        aes(label= after_stat('count')),
        stat = 'count',
        nudge_y = 0.125,
        va = 'bottom'
    )
    + theme_minimal()
    + scale_fill_brewer(type='qual', palette='Dark2')
)

