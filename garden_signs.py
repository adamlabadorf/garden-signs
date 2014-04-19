import csv
import sys

import textwrap

import matplotlib.font_manager as fm
import matplotlib.text as mt
from matplotlib.pyplot import *

import reportlab

import qrcode

fn = sys.argv[1]

f = csv.reader(open(fn),delimiter="\t")

title_size = 48.
desc_size = 18.

# annoyingly figure out the content width
figsize = (6,4)
fig = figure(figsize=figsize)
fig.savefig('tmp.png')

# I think matplotlib does 80 dpi by default
margin = 40

fig_bbox = fig.get_window_extent()
content_width, content_height = fig_bbox.size-2*margin
print content_width, content_height

figs = []
for r in f:
    print r

    # for title
    title_txt = mt.Text(0.5,0.75,r[0],
        horizontalalignment="center",
        verticalalignment="bottom",
        fontproperties=fm.FontProperties(fname="queblackssiextrabold.ttf",
                                         size=title_size),
        color="black"
    )

    desc_txt = mt.Text(0.5,0.5,textwrap.fill(r[1],40),
        horizontalalignment="center",
        verticalalignment="bottom",
        fontproperties=fm.FontProperties(fname="queblackssiextrabold.ttf",
                                         size=desc_size),
        color="#444444"
    )

    fig = figure(figsize=figsize)
    txt_ax = fig.add_axes([0,0,1,1])
    #subplots_adjust(left=0,right=1,top=1,bottom=0,hspace=0,wspace=0)
    txt_ax.add_artist(title_txt)
    txt_ax.add_artist(desc_txt)
    txt_ax.set_xticks([])
    txt_ax.set_yticks([])

    qr_ax = fig.add_axes((0.3,0.05,0.4,0.4))
    qr = qrcode.make(r[2])
    qr_ax.imshow(qr)
    qr_ax.set_xticks([])
    qr_ax.set_yticks([])

    fig.gca().axis("off")
    fig.savefig('%s.png'%r[0].lower().replace(" ","_"),dpi=300)
