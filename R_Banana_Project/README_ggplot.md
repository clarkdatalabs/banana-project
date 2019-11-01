# Create a linechart using ggplot

## Build

Getting the data in
```
bananas <- read.csv("FAOSTAT_w_Belgium_Lux_Post_2000.csv")
```

Subset for the columns of the data needed
```
bananas_clean <- bananas[, c("Area",
                            "Item",
                            "Year",
                            "Unit",
                            "Value",
                            "Flag.Description")]
```
 We have values in $1000 USD and tonnes, only want tonnes
```
bananas_clean = bananas_clean[bananas_clean$Unit == "tonnes",]
```
Check the data by hand to see if it matched up

## Run using ggplot2
Install ggplot2 to your device
```
library(ggplot2)
```
Create Line graphs using ggplot2
```
gbanana <- ggplot(data = bananas_clean, aes(x = Year, y = Value))+
            geom_line(aes(color = Area))+
            ggtitle("Export of Bananas by Tonne, 1994-2005")+ 
            theme(title = element_text(size = 15,
                                       face = "bold",
                                       margin = margin(10,0,10,0)))+ 
            labs(y = "Tonnes Exported (1000KG)")                  
                
gbanana
```
Note that line of Belgium-Luxembourg snapped at the year of 1999,
and there are two seperate lines of Belgium and Luxembourg since 2000.

It turned out that Belgium and Luxembourg export divorced since 2000.

So let's combine the data first, and then run the function again.
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

Then we want to rename Belguim to Belgium-Luxembourg and drop Luxembourg
```
bananas_clean[1:6,1] <- "Belgium-Luxembourg"

bananas_clean <- bananas_clean[-c(92:97),]
```

Swap row 1-6 with rows 7-13.
```
library(dplyr)

bananas_clean <- bananas_clean %>% 
                 arrange(Area, Year)
```
Then we redo the linechart.
```
gbanana <- ggplot(data = bananas_clean, aes(x = Year, y = Value))+
           geom_line(aes(color = Area))+
           ggtitle("Export of Bananas by Tonne, 1994-2005")+ 
           theme(title = element_text(size = 15,
                                      face = "bold",
                                      margin = margin(10,0,10,0)))+ 
                                      labs(y = "Tonnes Exported (1000KG)")                  

gbanana
```
Got it!

## Export
Click "Export" above your graph and save as Image/PDF

Done!
