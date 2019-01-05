# 创建第一个django程序
- 命令行启动

        djiango-admin startproject 项目名称
        cd 项目名称
        python manage.py runserver
        
- pycharm启动
    - 需要配置
    
# 路由系统-urls
- 创建app
    - app：负责一个具体业务或者一类具体业务的模块
    - python manage.py startspp app名称
- 路由
    - 按照具体的请求url，导入到相应的业务处理模块的一个功能模块。
    - django的信息控制中枢
    - 本质上是接收的url和相应的处理模块的一个映射
    - 在接收url请求的匹配上使用了re
    - url的具体格式urls.py中所示
- 需要关注的俩点
    - 1.接收的url是什么，即如何使用RE对传入url进行匹配
    - 2.已知url匹配到哪个处理模块
    
- url匹配规则
    - 从上往下一个一个比对
    - url格式是分级格式，则按照级别一级一级往下比对，主要对应url包含子url的情况
    - 子url一旦被调用，则不会返回到主url
        - '/one/two/three/'
    - 正则以r开头，表示不需要转义，注意箭号(^ 从前面开始查找)和美元符号($ 检查最后是否配对)
        - '/one/two/three/'        配对 r'^one/'
        - '/oo/one/two/three/'     不配对 r'^one/'
        - '/one/two/three/'        配对 r'three/$'
        - '/oo/one/two/three/oo/'  不配对 r'three/$'
        - 开头不需要有反斜杠
    - 如果从上向下都没有找到合适的匹配内容，则报错


# 2.正常映射
- 把某一个符合RE的url映射到事物处理函数中去
    - 举例如下
        
        from showeast import views as sv
        
        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^normalmap', sv.normalmap),
        ]    
# 3.url中带参数映射
- 在事件处理代码中需要由url传入参数，形如/myurl/param中的param
- 参数都是字符串形式，如果需要整数等形式需要自行转换
- 通常形式如下：
    - /search/page/432  中的432需要经常性变换

# 4.url在app中处理
    - 
        
    
    
    
    
    
    
    
    
    
    
    
    