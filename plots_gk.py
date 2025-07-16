# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:18:39 2023

@author: Gregor
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import scienceplots
import sys
# sys.path.append(r"C:\Users\Gregor\Documents\GitHub\matplotlib_templates")
plt.style.use(['science','vibrant'])
# plt.rcParams.update({"figure.dpi": 200})
# plt.style.use("default")

# import personal plotting lib
# sys.path.append(r"C:\Users\Gregor\Documents\GitHub\matplotlib_templates")
# import plots_gk as pgk

size = 12    # font size should be larger than 24, and I use 36 to control different sizes
params = {
    "legend.fontsize": size*0.9,
    "axes.labelsize": size,
    "axes.titlesize": size,
    "xtick.labelsize": size,
    "ytick.labelsize": size,
    "axes.titlepad": 20,
    "xtick.direction": "in",
    "font.size": size,
    "legend.handletextpad" : 0.8,
    "legend.borderpad" : 0.4,
    # markers
    # "lines.markersize" : 8,
    # "lines.markeredgecolor" : "k",
    # "lines.markeredgewidth" : 1,
    # "scatter.edgecolors" : "k",
    # xtick
    # "xtick.major.size": 6,
    # "xtick.major.width": 1.5,
    # "xtick.minor.size": 4,
    # "xtick.minor.width": 1,
    # ytick
    # "ytick.major.size": 6,
    # "ytick.major.width": 1.5,
    # "ytick.minor.size": 4,
    # "ytick.minor.width": 1,
    # linewidth
    # "axes.linewidth": 2,
    # "grid.linewidth": 1,
    # "lines.linewidth": 3,
    # "lines.markersize": 10,
    "axes.grid": False,   # delete this line before using grid style
    # font-family
    # Remove legend frame
    "legend.frameon": False,    # delete this line before use grid style
    # Always save as 'tight'
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.05
}
plt.rcParams.update(params)

# colors = ["red", "green", "blue", "magenta", "black", "orange", "cyan"]
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
# colors = ['#377eb8', '#ff7f00', '#4daf4a',
#           '#f781bf', '#a65628', '#984ea3',
#           '#999999', '#e41a1c', '#dede00']
colors2 = ["brown", "purple", "teal", "gray"]
markers = ["x","o", "v", "^","d","+", "."]
markers2 = ["1","2", "3"]
hatch1 = ["//", "\\", "x", "o", ".", "*", "///", "xx", "oo", ".."]
linestyles = ["-", "--", "-.", ":"]

def create_plot(figsize=(4.2,3.6), dpi=200, x_range=(0,1), y_range=(0,1), x_label="x", y_label="y", second_ax=False, y2_range=None, y2_label="y2", title=None, grid=False, grid_fine=False, pad=False):
    fig, ax = plt.subplots(1, 1, figsize=figsize, dpi=dpi)
    fig.tight_layout()
    if pad:
        x_pad = (x_range[1]-x_range[0])*0.05
        y_pad = (y_range[1]-y_range[0])*0.05
    else:
        x_pad=0
        y_pad=0
    xmin, xmax = x_range
    ymin, ymax = y_range
    ax.set_xlim(xmin-x_pad, xmax+x_pad)
    ax.set_ylim(ymin-y_pad, ymax+y_pad)
    # ax.tick_params(labelsize=13)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    if grid:
        ax.grid()
    if grid_fine:
        # ax.grid(which='minor', color='lightgray', linestyle=':', linewidth=0.5)
        ax.grid(which='minor', color='lightgray', linewidth=0.3, alpha=0.8)
        ax.minorticks_on()
    if title:
        ax.set_title(title)
    if second_ax:
        ax2 = ax.twinx()
        y2min, y2max = y2_range
        ax2.set_ylim(y2min, y2max)
        ax2.set_ylabel(y2_label)
        return fig, (ax, ax2)
    else:
        return fig, ax
    
def const_lines(ax, y, label, colors):
    for i in range(len(y)):
        ax.axhline(y[i], color = colors[i], linestyle = '--', label=label[i])
    
def scatter_plots(ax, x, y, label, markers, colors):
    for i in range(len(y)):
        ax.plot(x, y[i], markers[i], color=colors[i], label=label[i])
        
def line_plots(ax, x, y, label, style, colors):
    for i in range(len(y)):
        ax.plot(x, y[i], linestyle=style, color=colors[i], label=label[i])
        
def plot_fct(x, fct, xlabel="x", ylabel="y", x_range=None, y_range=None, title=None):
    y = fct(x)
    if not x_range:
        x_range=(min(x),max(x))
    if not y_range:
        y_range=(min(y),max(y))
    fig, ax = create_plot(dpi=200, x_range=x_range, y_range=y_range, x_label=xlabel, y_label=ylabel, title=title)
    ax.plot(x, y, linestyle="-", color="black", lw=1.2)


def barchart_sens_analysis(x_labels, bar_values, bar_labels, x_ax_label="$y$", y_ax_label="$\Delta y/y \,\cdot\, (\Delta x/x)^{-1}$", title=None, figsize=(4.8, 4), spacing=1, width=0.2, legend_loc=(1,1.02),legend_col=1):
    x = np.arange(len(x_labels))*spacing  # the label locations
    multiplier = 0
    
    fig, ax = plt.subplots(dpi=300, figsize=figsize)
    # ax.tick_params(labelsize=10)
    ax.set_xlabel(x_ax_label)
    ax.set_ylabel(y_ax_label)
    ax.set_axisbelow(True)
    ax.grid(axis="y", linestyle="-")
    # ax.grid(which='minor', color='silver', linestyle=':', linewidth=0.1, alpha=0.8, axis="y")
    # ax.minorticks_on()
    ax.xaxis.set_tick_params(which='minor', bottom=False)
    ax.xaxis.set_tick_params(which='minor', top=False)
    for ind, (bar_label, bar_value) in enumerate(zip(bar_labels, bar_values)):
        offset = width * multiplier
        rects = ax.bar(x + offset, bar_value, width, label=bar_label, edgecolor='black', hatch=hatch1[ind])
        # ax.bar_label(rects, padding=3)
        multiplier += 1

    if title:
        ax.set_title(title)
    ax.set_xticks(x + width/2*(len(bar_labels)-1), x_labels)
    y_max = max(abs(bar_values.flatten()))
    ax.set_ylim(-y_max*1.15, y_max*1.15)
    ax.legend(ncol=legend_col, fontsize=9)
    return fig, ax








if __name__ == "__main__":
    # fig, ax = create_plot(figsize=(6, 5), dpi=200, x_range=(min(var), max(var)), y_range=(0.2,1.2), x_label=f'${lab}$', y_label='$\eta,\,X \;/\;\mathrm{-}$', second_ax=False, y2_range=None, y2_label="y2")
    # ys = [float(SER["eta_cg"]), float(SER["eta_E"]), float(SER["C_conv_pg"]), float(SER["C_conv_glob"])]
    # labels = ["$\eta_{CG,SER}$", "$\eta_{EX,SER}$", "$X_{C,SER}$", "$X_{C,tot,SER}$"]
    # const_lines(ax, ys, labels, colors)
    # x = var
    # ys = [data["eta_cg"], data["eta_E"], data["C_conv_pg"], data["C_conv_glob"]]
    # labels = ["$\eta_{CG}$", "$\eta_{EX}$", "$X_{C}$", "$X_{C,tot}$"]
    # scatter_plots(ax, x, ys, labels, markers, colors)
    # fig.legend(bbox_to_anchor=(1, 1), loc="upper left")
    x=np.linspace(0, 100, 101)
    def f(x):
        y = ((1/(1-0.15)+0.47*x)**(-1)+0.15)
        return y
    plot_fct(x, f,xlabel="cycle number / -", ylabel="sorption capacity / mol/mol", y_range=(0,1))
    
    
    
    x_labels = ("x1", "x2", "x3", "x4")
    y_labels = ["y1", "y2", "y3", "y4", "y5"]
    y_values = np.array([[18.35, 18.43, 14.98, 12, 10], [38.79, 48.83, 47.50, 12, 10], [-190, 195.82, 217.19, 12, 10], [189.95, 195.82, 217.19, 15, 10]])
    data_sets = {
                "y1": np.array([18.35, 18.43, 14.98]),
                "y2": np.array([38.79, 48.83, 47.50]),
                "y3": np.array([189.95, 195.82, 217.19])
                }

    _ = barchart_sens_analysis(y_labels, y_values, x_labels, y_ax_label="test", title=None)
    