import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, render_template, request
import plotly.graph_objects as go
from randomwalk import RandomWalk


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    graph = None
    size=2 
    
    if request.method == "POST":
        data = 5000
        size = int(request.form.get("size"))

        rw = RandomWalk(data)
        rw.fill_walk()

        fig = go.Figure(data=go.Scatter(
            x = rw.x_values,
            y = rw.y_values,
            mode='markers',
            marker=dict(
                size=size,
                color = rw.x_values,
                colorscale='Blues',
                showscale=True
            )
        ))

        fig.update_layout(
            width=1000,
            height = 600, 
            showlegend = False,
            template="plotly_white",
                xaxis=dict(
                visible=False
            ),
            yaxis=dict(
                visible=False
            )
        )

        graph = fig.to_html(
            full_html=False,
            config={"responsive": True}

        )
        
    return render_template("index.html", graph=graph, size = size)

if __name__ == "__main__":
    app.run(debug=True)