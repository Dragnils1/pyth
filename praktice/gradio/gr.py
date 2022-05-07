import gradio as gr
import matplotlib.pyplot as plt
import numpy as np


def plot(v, a):
    g = 9.81
    theta = a/180*3.14
    tmax = ((2 * v) * np.sin(theta)) / g
    timemat = tmax*np.linspace(0, 1, 40)[:, None]

    x = ((v * timemat) * np.cos(theta))
    y = ((v * timemat) * np.sin(theta)) - ((0.5 * g) * (timemat ** 2))

    fig = plt.figure()
    plt.scatter(x=x, y=y, marker='.')
    plt.xlim(0, 100)
    plt.ylim(0, 60)
    return fig


block = gr.Blocks()

with block:
    gr.Markdown(
        "Let's do some kinematics! Choose the speed and angle to see the trajectory.")

    with gr.Row():
        speed = gr.inputs.Slider(1, 30, default=25, label="Speed")
        angle = gr.inputs.Slider(0, 90, default=45, label="Angle")
    output = gr.outputs.Image(type="plot")
    btn = gr.Button("Run")
    btn.click(plot, [speed, angle], output)

block.launch()
