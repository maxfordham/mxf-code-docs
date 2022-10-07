# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + Collapsed="false"

# https://plotly.com/python/waterfall-charts/#setting-marker-size-and-color
import plotly.graph_objects as go
di = {
    'name':'Energy Use',
    'orientation':"v",
    'measure' : ["relative", "relative", "relative", "relative", "relative","relative", "total"],
    'x':['Report0', 'Report1', 'Report2', 'Report3', 'Report4', 'Report5', 'Report6'],
    'text' : ["Systems on<br> but not<br> commissioned",
           "Hot water<br>pipework<br>re-lagged",
           "Lighting<br> controls<br> optimised",
           "Kill switches<br> enabled",
           "Entrance doors<br> auto-close",
           "Occupant zoning",
           "Optimized<br> Building<br> Performance"],
    'decreasing' : {"marker":{"color":"lightyellow", "line":{"color":"grey", "width":0.5}}},
    'increasing' : {"marker":{"color":"tomato"}},
    'totals' : {"marker":{"color":"springgreen", "line":{"color":"grey", "width":0.5}}},
    'textposition' : "outside",#outside"top"
    'textfont_size':14,
    'y' : [40, -8, -6, -4,-5, -3, 14],

    'connector' : {"line":{"color":"rgb(63, 63, 63)"}},
}
fig = go.Figure(go.Waterfall(**di))

fig.update_layout(
    title = "DataDriven Commissioning and PoE period",
    showlegend = True,
    autosize=False,
    width=1000,
    height=600,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4),
    yaxis=dict(range=[0, 50]),
    yaxis_title="estimated energy use (kwhr/m2.yr)",
    paper_bgcolor="white",
    template='plotly_white'
)
fig.update_traces(textfont_size=24)


# add benchmark lines

#  passivhaus
bmark_val = 15
bmark_nm = 'Passivhaus<br> min'
fig.add_shape(
        # Line Horizontal
            type="line",
            x0=-1,
            y0=bmark_val,
            x1=7,
            y1=bmark_val,
            line=dict(
                color="grey",
                width=2,
                dash="dashdot",
            ),
    )
fig.add_trace(go.Scatter(
    x=['benchmarks'],
    y=[bmark_val],
    mode="lines+markers+text",
    name=bmark_nm,
    text=[bmark_nm],
    textposition="top center",
    marker=dict(
        color='grey',
        size=6,
        line=dict(
            color='grey',
            width=2
        ))
))

#  TM54
bmark_val = 12
bmark_nm = 'MF TM54<br> prediction'
fig.add_shape(
        # Line Horizontal
            type="line",
            x0=-1,
            y0=bmark_val,
            x1=7,
            y1=bmark_val,
            line=dict(
                color="grey",
                width=2,
                dash="dashdot",
            ),
    )
fig.add_trace(go.Scatter(
    x=['benchmarks'],
    y=[bmark_val],
    mode="lines+markers+text",
    name=bmark_nm,
    text=[bmark_nm],
    textposition="bottom center",
    marker=dict(
        color='grey',
        size=6,
        line=dict(
            color='grey',
            width=2
        ))
))

#  Part L
bmark_val = 27
bmark_nm = 'Part L'
fig.add_shape(
        # Line Horizontal
            type="line",
            x0=-1,
            y0=bmark_val,
            x1=7,
            y1=bmark_val,
            line=dict(
                color="grey",
                width=2,
                dash="dashdot",
            ),
    )
fig.add_trace(go.Scatter(
    x=['benchmarks'],
    y=[bmark_val],
    mode="lines+markers+text",
    name=bmark_nm,
    text=[bmark_nm],
    textposition="bottom center",
    marker=dict(
        color='grey',
        size=6,
        line=dict(
            color='grey',
            width=2
        ))
))



fig.show()
fig.write_json('BMSDataDrivenWaterfall.plotly')
# -

import plotly.io as pio
pio.read_json('BMSDataDrivenWaterfall.plotly')
