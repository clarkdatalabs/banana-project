# Run and Setup R Project

## Build 
Read in the .csv file and attach;
```
bananas <- read.csv("FAOSTAT_data_10-25-2019.csv")
attach(bananas_clean)
```

Subset the dataset for the variables of interest; (optional)
```
bananas_clean <- bananas[,c("Area", 
                            "Item", 
                            "Year", 
                            "Unit",
                            "Value",
                            "Flag.Description")]
```

Belgium-Luxembourg exports divorce after 2000, so in order to extend data to account for post-2000, combine individual exports from Belgium and Luxemberg;
```
#2000
bananas_clean$Value[1] <- bananas_clean$Value[1] + bananas_clean$Value[92]
#2001
bananas_clean$Value[2] <- bananas_clean$Value[2] + bananas_clean$Value[93]
#2002
bananas_clean$Value[3] <- bananas_clean$Value[3] + bananas_clean$Value[94]
#2003
bananas_clean$Value[4] <- bananas_clean$Value[4] + bananas_clean$Value[95]
#2004
bananas_clean$Value[5] <- bananas_clean$Value[5] + bananas_clean$Value[96]
#2005
bananas_clean$Value[6] <- bananas_clean$Value[6] + bananas_clean$Value[97]
```

Rename Belgium to Belgium-Luxembourg, drop Luxembourg, and rearrange the rows to be in correct order;
```
bananas_clean[1:6,1] <- "Belgium-Luxembourg"
bananas_clean <- bananas_clean[-c(92:97),]

library(dplyr)
bananas_clean <- bananas_clean %>% arrange(Area, Year)
```

## Run
Install plotly;
```
install.packages("plotly")
library(plotly)
```

Assign the dependant and independant variables, use plot_ly() to create an interactive line chart;
``` 
x <- bananas_clean$Year
y <- bananas_clean$Value
data <- data.frame(x, y)

plot <- plot_ly(data, x = ~x, y = ~y, 
             color = bananas_clean$Area,
             type = 'scatter', mode = 'lines',
             line = list(width = 1)) %>%
        layout(title = "Export of Bananas by Tonne, 1994-2005",
             xaxis = list(title = "Year"),
             yaxis = list (title = "Tonnes Exported (1000 KG)"))

plot
```

## Export
1) Click "Export" above your graph
2) Opt to "Save as webpage..."
3) This will save a webpage as an html file to your computer. Clicking this will open a tab on your web browser with an interactive chart.

