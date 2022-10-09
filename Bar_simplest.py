import pandas as pd
from plotnine import *
from plotnine.data import *


mpg.head()

(
    ggplot(mpg) 
    + geom_bar(aes(x='class'))
    + theme_minimal()
)
