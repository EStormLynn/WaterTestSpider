# WaterTestSpider 
地表水水质监控系统爬虫

![](http://oo8jzybo8.bkt.clouddn.com/%E5%9B%BD%E5%AE%B6%E5%9C%B0%E8%A1%A8%E6%B0%B4%E6%B0%B4%E8%B4%A8%E7%9B%91%E6%8E%A7%E7%B3%BB%E7%BB%9F.png)

## 实现功能
* 爬取全国地表水水质数据 [地址](http://online.watertest.com.cn/)
* 创建地址Dict，记录观测值地理位置
* 设计WaterTest类，记录水质测量信息(包括:时间、ph值、溶解氧、氨氮、高锰酸盐指数等)
* 写入csv文件，统计数据总量
* 隔时段定时爬取水质数据

## 记录数据
![](http://oo8jzybo8.bkt.clouddn.com/%E6%B0%B4%E8%B4%A8%E6%95%B0%E6%8D%AEcsv.png)

## 数据内容
![](http://oo8jzybo8.bkt.clouddn.com/%E6%95%B0%E6%8D%AE%E5%86%85%E5%AE%B9.png)