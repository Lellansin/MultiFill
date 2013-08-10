MultiFill
====================

A sublime text plugin to multi-fill text.

With this plugin, you can press <code>[ctrl+m]</code> and <code>[ctrl+k]</code>, when you use the sublime choose multi-place, to select a text type to fill multi-place automatically.

Um, I think it will be very useful, while we write .html .sql and so on.


Using Screenshot
====================

Ordered fill numbers
--------------------

you can choose to fill the multi-place with numbers increase.

![image](https://github.com/Lellansin/MultiFill/raw/master/screenshots/multi_fill_num.png)

Auto fill names
--------------------

you can fill the multi-place with ordered names (you can config the names manually, or set it random appear, see the bottom of the article for more detail..).

![image](https://github.com/Lellansin/MultiFill/raw/master/screenshots/multi_fill_names.png)

Random fill
--------------------

it can random insert the text as you can see:

![image](https://github.com/Lellansin/MultiFill/raw/master/screenshots/multi_fill_sex.png)

Customize easily
====================

you can easily customize the MultiFill's text type title and content as you wish.

the config file is <code>MultiFill.sublime-settings</code> it seems like:
<pre>
{
	"custom":
	[
		{
			"name"  : "Names (ordered)",
			"way"   : "ordered",
			"values": 
			[
				"Alan","Bob","Cici","David","Elisabeth","Franklin"
			]
		},
		{
			"name"  : "Gender (random)",
			"way"   : "random",
			"values": 
			[
				"male","female"
			]
		},
		{
			"name":"V Roman (ordered)",
			"way"   : "ordered",
			"values":
			[
				"I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"
			]
		}			
	]
}
</pre>


Wait Help
--------------------

Um, I must tell you a truth that today is the second day I use python (that's really an amazing language XD), and the code I wrote seems bad, so if is okay could you help to improve this plugin, thanks a lot XD



MultiFill
====================

MultiFill（多处填充）是一个 sublime text 的插件。主要作用就是在选中多出的时候能够自动填充设置好的文字和数字。

当你选中多处之后按下 <code>[ctrl+m]</code> 和 <code>[ctrl+k]</code>，就可以调出 MultiFill 的主界面，你可以通过这个界面选择要填充的类型


安装
--------------------

今天刚写出来，新鲜着，目前还未加入package control，只能手动安装：

* 下载当前包 [MultiFill-master.zip]: https://github.com/Lellansin/MultiFill/archive/master.zip
* 找到sublime上面的菜单->【Preferences】->【Browse Packages..】打开【插件目录】
* 将 【MultiFill-master.zip】 解压到【插件目录】 注意 .py 等文件要在 【Packages/MultiFill/】 目录下

放置好之后可以重启 sublime 或者不重启直接尝试使用 <code>[ctrl+m]</code> 和 <code>[ctrl+k]</code> 来呼叫 MultiFill 的界面，示例参照上面的图片。

配置文件就是刚刚那个【Packages/MultiFill/】目录下的 <code>MultiFill.sublime-settings</code> 输出的文字还有是否随机插入都是可以配置的。

<pre>
{
	"custom":
	[
		{
			"name"  : "Names (ordered)", // 插入项名称(MultiFill界面显示)
			"way"   : "ordered",		 // 顺序插入
			"values": 	// 插入内容
			[
				"Alan","Bob","Cici","David","Elisabeth","Franklin"
			]
		},
		{
			"name"  : "Gender (random)",
			"way"   : "random",
			"values": 
			[
				"male","female"
			]
		},
		{
			"name":"V Roman (ordered)",
			"way"   : "ordered",
			"values":
			[
				"I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"
			]
		},
		// 新添加一个试试
		{
			"name":"Names chinese (中文名称)",
			"way"   : "ordered",	// 顺序插入
			"values":
			[
				"张三", "李四", "唐儒马"
			]
		}
	]
}
</pre>

配置之后，有图有真相：

![image](https://github.com/Lellansin/MultiFill/raw/master/screenshots/add_chinese.png)
