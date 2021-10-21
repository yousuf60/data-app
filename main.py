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
	MDBoxLayout:
		orientation:"vertical"		
		MDLabel:
			id:lbl
			text:""
			pos_hint:{"top":1}
		MDLabel:
			id:number
			text:"number"
	MDIconButton:
		icon:"plus"
		on_press:root.plus()
		pos_hint:{'center_y':.5}
	MDIconButton:
		icon:"minus"
		on_press:root.minus()
		pos_hint:{'center_y':.5}

	MDFloatLayout:	
		MDFlatButton:
			text:"delete"
			on_release:
				app.delete(root)
				root.delete()
			pos_hint:{"right":1,'center_y':.5}

MDBoxLayout:
	canvas:
		Color
			rgba:0,0,.8,1
		Rectangle:
			size:self.size
			pos:self.pos
	MDBoxLayout:
		orientation:"vertical"
		ScrollView:
			
			MDList:	
				spacing:dp(20)
				id:list
		MDCard:
			size_hint:1,.23
			md_bg_color:1, 180/255, 70/255, 1
			radius:[0,0,0,0]
			MDBoxLayout:
				orientation:"horizontal"
				MDBoxLayout:
					orientation:"vertical"
					MDTextField:
						hint_text:"name"
						line_color_focus:0,0,0,1
						id:new
					MDTextField:
						hint_text:"num"
						line_color_focus:0,0,0,1
						id:new_num

				MDIconButton:
					icon:"plus"
					pos_hint:{"top":.7}
					on_press:app.add_new()

				
				



"""
class ma_card(MDCard):
	md_bg_color=(.5,.5,.5,1)

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

	def delete(self,x):
		self.root.ids.list.remove_widget(x)
		print(x)



app=main()
app.run()

