from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts
from pyecharts import options as opts
from pyecharts.charts import AMap
from pyecharts.faker import Faker

# 高德地图
AMAP_KEY = '4d3199116b54b0306e9ba7fb1dff2a21'
c = (
    AMap(opts.InitOpts(width="1920px", height="1080px"))
    .add_schema(amap_ak = AMAP_KEY, center=[120.13066322374, 30.240018034923])
    .render("amap_base.html")
)

# 得到折线图对象
# line = Line()

# 添加x轴数据
# line.add_xaxis(['java','python','javascript'])

# 添加y轴数据
# line.add_yaxis('count',[10,20,30])

# 全局配置
# line.set_global_opts(
#     title_opts=TitleOpts(title="测试标题",pos_left="10%"),
#     legend_opts=LegendOpts(is_show=True),
# )

# 生成图表
# line.render()


