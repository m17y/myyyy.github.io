---
layout: post
title: 配置sublime-python-全栈开发环境
tags: tools
description: sublime编辑器下python全栈开发环境配置
---

#配置sublime全栈开发环境（python）
 
###1 下载sublime [link](http://www.sublimetext.com)

##2 安装Package Control
    1.ctrl + ~ 快捷键，调出 console
    2.import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())

###3 ubuntu 下输入法问题：
     1. 下载我们需要的文件,打开终端 ,输入：
       git clone https://github.com/lyfeyaj/sublime-text-imfix.git
     2. 将下载的文件解压之后，移到当前目录（～目录下边），然后执行下边命令：
      cd ~/sublime-text-imfix （前提：解压后的sublime-text-imfix必须在~目录下）
       sudo cp ./lib/libsublime-imfix.so /opt/sublime_text/
       sudo cp ./src/subl /usr/bin/
     3. 最后把sublime都关掉，然后在终端输入subl，就可以在sublime使用中文了

###4 汉字时输入框不跟随光标:
 安装插件：IMESupport

###5 THEM:
 itg.flat

##常用插件

* 1.SideBarEnhancements插件
  SideBarEnhancements是一款很实用的右键菜单增强插件

* 2.Anaconda

  Anaconda 是一个终极 Python 插件。它为 ST3 增添了多项 IDE 类似的功能，例如：

  Autocompletion 自动完成，该选项默认开启，同时提供多种配置选项。
  Code linting 使用支持 pep8 标准的 PyLint 或者 PyFlakes。因为我个人使用的是另外的 linting 工具，所以我会在 Anaconda 的配置文件 Anaconda.sublime-settings 中将 linting 完全禁用。操作如下: Sublime > Preferences > Package Settings > Anaconda > Settings – User： p
  McCabe code complexity checker 让你可以在特定的文件中使用 McCabe complexity checker. 如果你对软件复杂度检查工具不太熟悉的话，请务必先浏览上边的链接。
  Goto Definitions 能够在你的整个工程中查找并且显示任意一个变量，函数，或者类的定义。
  Find Usage 能够快速的查找某个变量，函数或者类在某个特定文件中的什么地方被使用了。
  Show Documentation： 能够显示一个函数或者类的说明性字符串(当然，是在定义了字符串的情况下)

* 3.requirementstxt
  Requirementstxt 可以为你的 requirements.txt 文件提供自动补全，语法高亮以及版本管理功能

* 4.GitGutter
  GitGutter 让 ST3 能在左边栏的位置显示一个小图标，用以表示在最后一次提交以后，代码是否有追加，修改或者删除。

* 5.Javascript-API-Completions:
  支持Javascript、JQuery、Twitter Bootstrap框架、HTML5标签属性提示的插件

* 6.WakaTime -- 记录你的Code时间;
  WakaTime可以做到精确地统计到你花在某个项目上的时间

* 7.sublime-text-git: Git 版本控制

##快捷命令
* 快捷键

  1.跳转到任意内容 (“cmd+p”) 用来快速查找和打开文件。你仅仅只需要工程中文件的一部分路径或者文件名你就可以很容易的打开这个文件。这在一个大型的 Django 工程中显得非常方便。
  2.跳转到指定行 (“ctrl+g”) 让你在当前文件中跳转到指定行数。
  3.跳转到标志 (“cmd+r”) 可以列出当前文件中所有的函数或者类，让你更方便查找。你可以通过输入关键字来查找你所需要的函数或者类。
  4.跳转到行首 (cmd+left-arrow-key) 与 跳转到行尾 (cmd+right-arrow-key)
  5.删除当前行(ctrl+shift+k)
  6.多重编辑 是我迄今为止最喜欢的快捷键
   1.选定一个单词，点击 **“cmd+d”** 来选择同样的单词，再次点击 **“cmd+d”** 继续选择下一个单词…
   2.或者 **“cmd+单击”** 来指定多个你想要同时修改的地方。
  7.块编辑 (option+left-mouse-click) 用于选择一整块的内容。通常在整理 CSV 文件的时候用于删除空白内容。






	Sublime Text 3 快捷键精华版

	Ctrl+Shift+P：打开命令面板

	Ctrl+P：搜索项目中的文件

	Ctrl+G：跳转到第几行

	Ctrl+W：关闭当前打开文件

	Ctrl+Shift+W：关闭所有打开文件

	Ctrl+Shift+V：粘贴并格式化

	Ctrl+D：选择单词，重复可增加选择下一个相同的单词

	Ctrl+L：选择行，重复可依次增加选择下一行

	Ctrl+Shift+L：选择多行

	Ctrl+Shift+Enter：在当前行前插入新行

	Ctrl+X：删除当前行

	Ctrl+M：跳转到对应括号

	Ctrl+U：软撤销，撤销光标位置

	Ctrl+J：选择标签内容

	Ctrl+F：查找内容

	Ctrl+Shift+F：查找并替换

	Ctrl+H：替换

	Ctrl+R：前往 method

	Ctrl+N：新建窗口

	Ctrl+K+B：开关侧栏

	Ctrl+Shift+M：选中当前括号内容，重复可选着括号本身

	Ctrl+F2：设置/删除标记

	Ctrl+/：注释当前行

	Ctrl+Shift+/：当前位置插入注释

	Ctrl+Alt+/：块注释，并Focus到首行，写注释说明用的

	Ctrl+Shift+A：选择当前标签前后，修改标签用的

	F11：全屏

	Shift+F11：全屏免打扰模式，只编辑当前文件

	Alt+F3：选择所有相同的词

	Alt+.：闭合标签

	Alt+Shift+数字：分屏显示

	Alt+数字：切换打开第N个文件

	Shift+右键拖动：光标多不，用来更改或插入列内容

	鼠标的前进后退键可切换Tab文件

	按Ctrl，依次点击或选取，可需要编辑的多个位置

	按Ctrl+Shift+上下键，可替换行
	选择类

	Ctrl+D 选中光标所占的文本，继续操作则会选中下一个相同的文本。

	  Alt+F3 选中文本按下快捷键，即可一次性选择全部的相同文本进行同时编辑。举个栗子：快速选中并更改所有相同的变量名、函数名等。
	  
	  Ctrl+L 选中整行，继续操作则继续选择下一行，效果和 Shift+↓ 效果一样。
	  
	  Ctrl+Shift+L 先选中多行，再按下快捷键，会在每行行尾插入光标，即可同时编辑这些行。
	  
	  Ctrl+Shift+M 选择括号内的内容（继续选择父括号）。举个栗子：快速选中删除函数中的代码，重写函数体代码或重写括号内里的内容。
	  
	  Ctrl+M 光标移动至括号内结束或开始的位置。
	  
	  Ctrl+Enter 在下一行插入新行。举个栗子：即使光标不在行尾，也能快速向下插入一行。
	  
	  Ctrl+Shift+Enter 在上一行插入新行。举个栗子：即使光标不在行首，也能快速向上插入一行。
	  
	  Ctrl+Shift+[ 选中代码，按下快捷键，折叠代码。
	  
	  Ctrl+Shift+] 选中代码，按下快捷键，展开代码。
	  
	  Ctrl+K+0 展开所有折叠代码。
	  
	  Ctrl+← 向左单位性地移动光标，快速移动光标。
	  
	  Ctrl+→ 向右单位性地移动光标，快速移动光标。
	  
	  shift+↑ 向上选中多行。
	  
	  shift+↓ 向下选中多行。
	  
	  Shift+← 向左选中文本。
	  
	  Shift+→ 向右选中文本。
	  
	  Ctrl+Shift+← 向左单位性地选中文本。
	  
	  Ctrl+Shift+→ 向右单位性地选中文本。
	  
	  Ctrl+Shift+↑ 将光标所在行和上一行代码互换（将光标所在行插入到上一行之前）。
	  
	  Ctrl+Shift+↓ 将光标所在行和下一行代码互换（将光标所在行插入到下一行之后）。
	  
	  Ctrl+Alt+↑ 向上添加多行光标，可同时编辑多行。
	  
	  Ctrl+Alt+↓ 向下添加多行光标，可同时编辑多行。
	  
	编辑类
	  Ctrl+J 合并选中的多行代码为一行。举个栗子：将多行格式的CSS属性合并为一行。
	  
	  Ctrl+Shift+D 复制光标所在整行，插入到下一行。
	  
	  Tab 向右缩进。
	  
	  Shift+Tab 向左缩进。
	  
	  Ctrl+K+K 从光标处开始删除代码至行尾。
	  
	  Ctrl+Shift+K 删除整行。
	  
	  Ctrl+/ 注释单行。
	  
	  Ctrl+Shift+/ 注释多行。
	  
	  Ctrl+K+U 转换大写。
	  
	  Ctrl+K+L 转换小写。
	  
	  Ctrl+Z 撤销。
	  
	  Ctrl+Y 恢复撤销。
	  
	  Ctrl+U 软撤销，感觉和 Gtrl+Z 一样。
	  
	  Ctrl+F2 设置书签
	  
	  Ctrl+T 左右字母互换。
	  
	  F6 单词检测拼写

