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
    
    if request.method == "POST":
        data = 1000
        
        rw = RandomWalk(data)
        rw.fill_walk()

        fig = go.Figure(go.Scatter(x=rw.x_values, y=rw.y_values, mode="markers"))
        fig.update_layout(
            width=800,
            height=600
        )
        graph = fig.to_html(full_html=True)
        
    return render_template("index.html", graph=graph)

if __name__ == "__main__":
    app.run(debug=True)