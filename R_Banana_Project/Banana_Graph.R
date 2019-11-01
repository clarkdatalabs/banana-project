####################################################################
##################### Banana Graph, R Team #########################
##################### Amanda West, Oct. 23rd 2019 ##################
rm(list=ls())
getwd()
setwd("/Users/amandaAmanda/desktop/VizCon")
bananas <- read.csv("FAOSTAT_data_10-25-2019.csv")

#### 
# subset for the columns of data you want
bananas_clean <- bananas[,c("Area", 
                          "Item", 
                          "Year", 
                          "Unit",
                          "Value",
                          "Flag.Description")]

# we have values in $1000 USD and tonnes / etc, only want tonnes
attach(bananas_clean)
bananas_clean = bananas_clean[Unit == "tonnes",]

#### 
# next, Belgium-Luxembourg exports divorce after 2000,
# so in order to extend our data to account for post-2000,
# we combine the individual exports Belgium and Luxemberg 

# combine quantities exported
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

#### 
# rename Belgium to Belgium-Luxembourg and drop Luxembourg 

bananas_clean$Area <- gsub("Belgium", "Belgium-Luxembourg", bananas_clean$Area)
bananas_clean$Area <- gsub("Belgium-Luxembourg-Luxembourg", "Belgium-Luxembourg", bananas_clean$Area)

bananas_clean <- bananas_clean[-c(92,93,94,95,96,97),]

####
# swap row 1-6 with rows 7-13.

bananas_clean <- bananas_clean %>% arrange(Area, Year)

#### 
# next, checked the data by hand to see if it matched up:
# checked Ecuador, USA, United Arab Emirates, Belgium-Luxemberg, 
# Costa Rica
# all numbers approximately matched up (we don't haveexact numbers
# for the graph but it was pretty spot on)
###

####
# next, time to play with plot.ly 

# install plotly to your device
# install.packages("plotly")
#packageVersion('plotly') # ‘4.9.0’
library(plotly)

# https://plot.ly/r/line-charts/

# Create Line Graphs using Plot.ly

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

# Create a shareable link to your chart
# Set up API credentials: https://plot.ly/r/getting-started
chart_link = api_create(p, filename="line-basic")
chart_link

