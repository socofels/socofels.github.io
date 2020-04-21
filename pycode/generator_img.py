from matplotlib import pyplot as plt
from matplotlib.image import imread,imsave
import seaborn as sns
import numpy as np
#用于显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）

save_img_path = "assets/images/generate_img/"

y = [393,6271,20463,32282,30915,26323]
x = ["3/12","3/21","3/30","4/8","4/17","4/19"]
def scatter(x,y,title,label_x,label_y):
  fig,ax=plt.subplots()
  plt.title(title)
  plt.scatter(x,y)
  plt.xlabel(label_x)
  plt.ylabel(label_y)
  plt.show()
  fig.savefig(save_img_path+f"{title}.jpg",dpi=600,format='jpg')

def scatter_and_line(x,y,title,label_x,label_y,point1,point2):
  fig,ax=plt.subplots()
  plt.title(title)
  plt.scatter(x,y)
  plt.xlabel(label_x)
  plt.ylabel(label_y)
  plt.show()
  fig.savefig(save_img_path+f"{title}.jpg",dpi=600,format='jpg')
if __name__ == "__main__":
  scatter(x,y,"covid-19","date","USA_infections")
