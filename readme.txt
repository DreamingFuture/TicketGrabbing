Redis命名规则:
    可用票以列表形式存储, 表名: G/V-time-tickets;
    用户抢票信息以哈希(Hash)存储, key: G/V-U-time-stu_id;

requirements:
    Django>=2.0;
    Xadmin==2.0.1;
    redis;
    mysqlclient;

部署事项:
    1.settings.py 里的debug需要改成false, 数据库配置改成服务器相应的, 收集静态文件时把static_root注释去掉;
    2.首页二维码: wide_screen.css 里36行和85行;
    3.票页面二维码: ticket_preach.html和ticket_visit.html里二维码图片链接地址里相应部分改成服务器地址或域名;
    4.时间段修改: views.py里两个时间字典, my_xadmin_view.py里有两处, query_ticket里js部分有;
    6.……
    nginx配置文件(Ubuntu下在/etc/nginx/nginx.conf):
        在events里把连接数改大 worker_connections 20480;
        在最上面那一块地方加上 worker_rlimit_nofile 65535;

V0.0
    完成了大体架构;
    ……;

V1.0
    把直接数据库存储改为Redis;

V1.5
    完成了admin对Redis里余票以及抢票信息的统一管理;
    修改了一些小细节;

V1.5.1
    精简了一些冗余代码;
    把页面逻辑与设计稿改为一致形式;
    增加了404和500页面的处理;

V1.5.2
    对接了前后端

V1.5.3
    在重置余票处不应该使用flushall;    √√√
    限定参与抢票的人群，只允许2019级新生参与;     √√√
    防爬虫，二重请求验证;     √√√
    修改允许了有些用户可能一天内抢两个时间段的票;    √√√
    一人多次抢票问题;   (只检测Redis,所以转存后还是可以抢的)√√√

V1.5.4
    过滤可能引起MySQL存储错误的特殊Unicode字符(顺便加上MySQL异常处理);     √√√
    修改了信息输入页面警告框样式

V1.5.5
    增加了票页面提醒,修改了首页

V1.5.6
    增加了查票系统,链接/ticket/query_ticket/

V1.5.7
    更改了后台管理页面
    查票下拉框字体改大
    加上了日期

V1.5.8
    宣讲人信息的增加;
    后台页面完成

V1.5.9
    检票页面完成;
    导出页面置灰;


利用js循环加密token来防爬虫
