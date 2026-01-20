import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from flask import Flask, render_template, request, jsonify
import plotly.graph_objects as go
from randomwalk import RandomWalk


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["GET", "POST"])
def generate():
    graph = None
    size=2 
    dataP = 5000
    if request.method == "POST":
        data = request.get_json()

        dataP = int(data["points"])
        size = int(data["size"])
        print(dataP)

        rw = RandomWalk(dataP)
        rw.fill_walk()

        fig = go.Figure(data=go.Scatter(
            x = rw.x_values,
            y = rw.y_values,
            mode='markers',
            marker=dict(
                size=size,
                color = rw.x_values,
                colorscale='ice',
                showscale = False
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

        graph = fig.to_json()
        
        return jsonify({
            "graph": graph
        }) 

if __name__ == "__main__":
    app.run(debug=True)