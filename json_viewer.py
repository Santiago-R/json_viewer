import json, sys
import plotly.express as px

def show_file(file):
    with open(file) as f:
        data = json.load(f)
    fig = px.scatter(x=data["x"], y=data["y"], title="Hello, world!").show()

if __name__ == "__main__":
    assert len(sys.argv) == 2
    show_file(sys.argv[1])