from bokeh.models import HoverTool
import bokeh.plotting as bpl
from bokeh.palettes import d3
from bokeh.embed import file_html
from bokeh.io import save
import os
from datetime import date


currentDate = date.today()

def generateBokeh(result,titleList):

    data = titleList

    palette = d3['Category20'][20][:15]
    grey = palette[-1]
    palette = palette[:-1]

    result['title'] = data

    result['color'] = [
        palette[label % len(palette)]
        for label in result.labels.values
    ]

    result.loc[result.labels == -1, 'color'] = grey
    result = result[result.labels != -1]

    print(result.columns)
    source = bpl.ColumnDataSource(data=result)
    hover = HoverTool(tooltips=[('title', '@title'), ('topic', '@labels')])

    # title for the graph

    p = bpl.figure(title="Topic Modelling", plot_width=1800, plot_height=1100)

    # label on x-axis
    p.xaxis.axis_label = 'X'

    # label on y-axis
    p.yaxis.axis_label = 'Y'

    # plot each datapoint as a circle
    # with custom attributes.
    p.circle(x = 'x',
             y = 'y',
             color='color',
             #fill_alpha=0.3,
             size=3,
            source=source)


    #p.scatter(x='x', y='y', color='color', source=source)

    p.add_tools(hover)
    # you can save the output as an
    # interactive html file
    save(p,filename= (os.path.dirname(os.path.realpath(__file__)) + rf'\HTMLs\GeneralNewsDiscovery_{currentDate}.html'))

    #return (file_html(p, (None,None), title="General News Discovery"))
    #output_file(r"D:\TopicModellingElasticSearch\TopicModelling.html", title="General News Discovery")

    # display the generated plot of graph
    #bpl.show(p)