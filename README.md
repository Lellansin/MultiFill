MultiFill
====================

A sublime text plugin to multi-fill text.

With this plugin, you can press <code>[ctrl+m]</code> and <code>[ctrl+k]</code>, when you use the sublime choose multi-place, to select a text type to fill multi-place automatically.

Um, I think it will be very useful, while we write .html .sql and so on.


<h1>Using Screenshot</h1>

<h2>Ordered fill numbers</h2>

![image](https://github.com/Lellansin/MultiFill/raw/master/screenshots/multi_fill_num_1.jpg)
![image](https://github.com/Lellansin/MultiFill/raw/master/screenshots/multi_fill_num_2.jpg)
![image](https://github.com/Lellansin/MultiFill/raw/master/screenshots/multi_fill_num_3.jpg)

<h2>Auto fill names</h2>

![image](https://github.com/Lellansin/MultiFill/raw/master/screenshots/multi_fill_names_1.jpg)
![image](https://github.com/Lellansin/MultiFill/raw/master/screenshots/multi_fill_names_2.jpg)
![image](https://github.com/Lellansin/MultiFill/raw/master/screenshots/multi_fill_names_3.jpg)

<h2>Random fill</h2>

![image](https://github.com/Lellansin/MultiFill/raw/master/screenshots/multi_fill_sex_1.jpg)
![image](https://github.com/Lellansin/MultiFill/raw/master/screenshots/multi_fill_sex_2.jpg)
![image](https://github.com/Lellansin/MultiFill/raw/master/screenshots/multi_fill_sex_3.jpg)

<h1>Customize easily</h1>

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


<h1>Wait Help</h1>

Um, I must tell you a truth that today is the second day I use python (that's really an amazing language XD), and the code I wrote seems bad, so if is okay could you help to improve this plugin, thanks a lot XD