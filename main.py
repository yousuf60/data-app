from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
import json

database_path="database.js"
try: open(database_path,'r')
except:open(database_path,'w').write("""{"informations": {}}""")
database=json.loads(open(database_path).read())
print(database)
KV="""
<ma_card>:
	size_hint:1,None
	height:dp(100)
	MDCard:
		size_hint:None,1
		width:dp(10)
		md_bg_color:213/255, 184/255, 1, 1#1, 180/255, 70/255, 1
		radius:[0,0,0,0]
	MDBoxLayout:
		orientation:"vertical"		
		MDLabel:
			id:lbl
			text:""
			pos_hint:{"top":1}
		MDLabel:
			id:number
			text:"number"
	MDBoxLayout:
		orientation:"vertical"
		MDIconButton:
			icon:"plus"
			on_press:root.plus()
			pos_hint:{'center_y':.5}
		MDIconButton:
			icon:"minus"
			on_press:root.minus()
			pos_hint:{'center_y':.5}

	MDFloatLayout:	
		MDIconButton:
			icon:"delete"
		
			on_release:
				app.delete(root)
				root.delete()
			pos_hint:{"right":1,"center_y":.23}

MDBoxLayout:
	canvas:
		Color
			rgba:1,1,1,1#57/255, 46/255, 133/255,1#140/255, 20/255, 252/255, 1#0,0,1,.8
		Rectangle:
			size:self.size
			pos:self.pos
	MDBoxLayout:
		orientation:"vertical"
		md_bg_color:1,1,1,1

		MDCard:
			size_hint:1,.23
			md_bg_color:42/255, 23/255, 177/255,1#1, 180/255, 70/255, 1
			radius:[0,0,0,0]
			MDBoxLayout:
				orientation:"horizontal"
				MDBoxLayout:
					orientation:"vertical"
					MDTextField:
						hint_text:"name"
						line_color_focus:1,1,1,1
						text_color:1,1,1,1
						id:new
					MDTextField:
						hint_text:"num"
						line_color_focus:1,1,1,1
						text_color:1,1,1,1
						id:new_num

				MDIconButton:
					icon:"plus"
					pos_hint:{"top":.7}
					on_press:app.add_new()

		MDFloatLayout:
			md_bg_color:57/255, 46/255, 133/255,1	
			size_hint:1,1
			ScrollView:
				size_hint:.9,1

				MDList:

					spacing:dp(10)
					id:list
					



"""
class ma_card(MDCard):
	md_bg_color=(93/255, 75/255, 216/255,1)#(154/255, 18/255, 179/255, 1)#(1,3/255,158/255,1)#(.5,.5,.5,1)

	def __init__(self,x,y,**kwargs):
		super().__init__()
		self.z=x
		self.c=y
		self.ids.lbl.text=x
		if y.isnumeric():
			self.ids.number.text=y
			self.c=int(y)

		else:
			self.ids.number.text="1"
			self.c=1

	def plus(self):
		self.c+=1
		self.ids.number.text=str(self.c)
		database["informations"][self.z]=str(self.c)
		json.dump(database,open(database_path,'w'))
	def minus(self):
		self.c-=1
		self.ids.number.text=str(self.c)
		database["informations"][self.z]=str(self.c)
		json.dump(database,open(database_path,'w'))
	def delete(self):
		del database["informations"][self.z]
		json.dump(database,open(database_path,'w'))

class main(MDApp):
	def build(self):
		return Builder.load_string(KV)
	def on_start(self):
		for x,y in database["informations"].items():
			self.root.ids.list.add_widget(ma_card(str(x),str(y)))
		print(self.root.ids.list.children)
	def add_new(self):
		if self.root.ids.new.text and self.root.ids.new_num.text:
			x=self.root.ids.new.text
			y=self.root.ids.new_num.text

			self.root.ids.list.add_widget(ma_card(x,y))
			self.root.ids.new.text,self.root.ids.new_num.text="",""
			database["informations"][x]=y
			json.dump(database,open(database_path,'w'))
		elif  self.root.ids.new.text:
			x=self.root.ids.new.text
			y="1"

			self.root.ids.list.add_widget(ma_card(x,y))
			self.root.ids.new.text,self.root.ids.new_num.text="",""
			database["informations"][x]=y
			json.dump(database,open(database_path,'w'))
	def delete(self,x):
		self.root.ids.list.remove_widget(x)
		print(x)



app=main()
app.run()

