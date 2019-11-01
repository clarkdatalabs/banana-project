import plotly.express as px
import plotly.express as px


#X year
#Y Tons

#each line is a year
gapminder = px.data.gapminder().query("continent=='Europe'")
fig = px.line_3d(gapminder, x="gdpPercap", y="pop", z="year", color='country')
fig.show()