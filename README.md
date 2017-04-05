# AutomaticReport
一段代码片段，用来每天自动使用微信向老板发日报，搬砖真苦！

# 依赖
1. wxpy
2. apscheduler

# 使用方法
- 使用scheduler.add_job中的hour 和 minute参数设置每天发送的日报时间，取值范围分别为[0,23],[0,59]
- 配置config_sample，并改名为config
- 创建report.txt并将要汇报内容写入。
- 跑它！