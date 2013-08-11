thub的多人协作
================

1. github上你可以用别人的现成的代码
直接 git clone 即可了

2. 然后你也想改代码或者贡献代码咋办？

#### Fork

从别人的项目中fork一个到你自己的仓库
这个时候这个仓库就是你的了，要删除这个仓库到设置-admin
那里，像你删除你自己创建的repo一样删除，（因为这个库就是你的了，你现在可以任意修改这个库，除非你pull
request被接受否则你 不会对原作者的库产生任何影响）

比如osteach账号下有个osteach.github.com的库
这个项目的地址是https://github.com/TiffanyZhou/Mailer

这时候我（suziewong）想贡献代码了。fork之
fork之后，你的个人仓库就多了这个库
git@github.com:YOURNAME/Mailer.git

#### 开发并且提交代码

**clone**

首先要从github上下载代码到本地，你需要执行如下命令：

    git clone git@github.com:TiffanyZhou/Mailer.git
    cd Mailer

然后代码到本地里了，你就可以各种修改  add commit 了

**commit**

当你修改代码之后，需要commit到本地仓库，执行的命令如下：

    git add xx
    git commit  -m '修改原因，相关说明信息'



**push**

执行git
commit之后，只是提交到了本机的仓库，而不是github上你账号的仓库。你需要执行push命令，把commit提交到服务器。

    这里你可以直接git push 木有问题直接到远程默认仓库，当然remote add
也木有问题，因为和操纵自己的库没有任何区别
    git push
    这里的git push  指的是push 到YOURNAME/Mailer
的默认仓库（master）

这里有**重点**

    这里你如果 remote add YOURNAME YOURNAME/Mailer.git
    好吧，你 
    git push osteach master 之类的都是没用的
    因为你没有权限！没有权限修改别人(tiffanyzhou)的库!
    
    
    
    
#### 上游仓库
**更新远程代码：**
1. 更新自己的仓库
    git pull 

2.你正在开发，主作者【项目负责人】tiffanyzhou也在开发，你当时fork的代码已经不是tiffanyzhou的最新的代码了。
 这时候的你对你的代码肯定没问题，但是pull request
就有可以会出错，因为你fork的repo和现在的tiffanyzhou的repo已经不一样了。
 这时候理论上tiffanyzhou会close你的request，让你先pull tiffanyzhou的最新代码。
 于是乎
    git remote add tiffanyzhou tiffanyzhou/Mailer.git
    git fetch tiffanyzhou master:develop
    
自己merge代码 不和谐的地方，这里肯定不能git pull,会提示conflict
即代码是需要自己merge的
    
    你修改代码后
    
    git add 
    git commit
然后测试一下是不是已经拉取完成最新的了。

    git pull tiffanyzhou master 

你就会发现原先的出错不见了，变成了**everything update   **
    
你就可以提交到自己的远程版本库了。
    git push origin master
    
之后你再pull request，osteach那边就木有出现 不能 auto
merge的情况了，然后osteach看你的代码给不给力，
给力就merge你的代码到他的主分支去了。
功德圆满 ：）



#### pull request

登陆github，在你自己的账号中的仓库中点击pull request，就会要求你输入pull
request的原因和详细信息，你确认之后。tiffanyzhou的owner就会收到并且审查，审查通过就会合并到主干上。
