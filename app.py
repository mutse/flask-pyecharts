#!/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask
from jinja2 import Markup


from pyecharts import options as opts
from pyecharts.charts import WordCloud, Line, Tab, Timeline, Pie, Tree, Bar
from pyecharts.components import Table

import random

app = Flask(__name__, static_folder="templates")


def word_cloud():
    words = [
        ("Sam S Club", 10000),
        ("Macys", 6181),
        ("Amy Schumer", 4386),
        ("Jurassic World", 4055),
        ("Charter Communications", 2467),
        ("Chick Fil A", 2244),
        ("Planet Fitness", 1868),
        ("Pitch Perfect", 1484),
    ]

    return WordCloud().add("", words, word_size_range=[20, 100], shape='diamond').set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-示例", subtitle="我是副标题"))

def _create_line():
    return Line().add_xaxis(['Sunday', 'Saturday', 'Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']).add_yaxis("商家A", [7, 6, 5, 4, 3, 2, 1])

def _create_table():
    table = Table()
    headers = ["City name", "Area", "Population", "Annual Rainfall"]
    rows = [
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Adelaide", 1295, 1158259, 600.5],
        ["Darwin", 112, 120900, 1714.7],
    ]
    table.add(headers, rows)
    return table


def _get_random_value():
    return [random.randint(100, 1000) for _ in range(6)]

def _create_timeline():
    name = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
    
    quarter_one = Pie().add("", [list(v) for v in zip(name, _get_random_value())]).set_global_opts(title_opts=opts.TitleOpts(title="第一季度销售图"))
 
    quarter_two = Pie().add("", [list(v) for v in zip(name, _get_random_value())]).set_global_opts(title_opts=opts.TitleOpts(title="第二季度销售图"))
 
    quarter_three = Pie().add("", [list(v) for v in zip(name, _get_random_value())]).set_global_opts(title_opts=opts.TitleOpts(title="第三季度销售图"))
 
    quarter_four = Pie().add("", [list(v) for v in zip(name, _get_random_value())]).set_global_opts(title_opts=opts.TitleOpts(title="第四季度销售图"))
 
    timeline = Timeline()
 
    timeline.add(quarter_one, '第一季度')
    timeline.add(quarter_two, '第二季度')
    timeline.add(quarter_three, '第三季度')
    timeline.add(quarter_four, '第四季度')

    return timeline

def _create_tree():
    TEST_DATA = [
        {
            "children": [
                {"name": "B"},
                {
                    "children": [{"children": [{"name": "I"}], "name": "E"}, {"name": "F"}],
                    "name": "C",
                },
                {
                    "children": [
                        {"children": [{"name": "J"}, {"name": "K"}], "name": "G"},
                        {"name": "H"},
                    ],
                    "name": "D",
                },
            ],
            "name": "A",
        }
    ]

    return Tree().add(
        series_name="tree",
        data=TEST_DATA,
        orient="LR",
        initial_tree_depth=3,
        label_opts=opts.LabelOpts(),
        leaves_label_opts=opts.LabelOpts(),
    )


def _create_bar():
    bar = Bar().add_xaxis(["A", "B", "C"]).add_yaxis("series0", [1, 2, 4])
    bar.set_colors(["#AABBCC", "#BBCCDD", "#CCDDEE"] + bar.colors)
    return bar


def create_tab():
    c = (
        Tab()
            .add(_create_line(), 'Line')
            .add(_create_table(), 'Table')
            .add(word_cloud(), 'WorldCloud')
            .add(_create_timeline(), 'Timeline')
            .add(_create_tree(), 'Tree')
            .add(_create_bar(), 'Bar')
    )
    return c

@app.route("/")
def index():
    c = create_tab()
    return Markup(c.render_embed())


if __name__ == "__main__":
    app.run()