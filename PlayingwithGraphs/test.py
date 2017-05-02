import pandas
from bokeh.plotting import figure, output_file, show

# pandas
df = pandas.read_csv('data2.csv')
# read in name, x , y
# print df.x, df,y

# bokeh
plot =  figure()
plot.scatter(x=df.x, y=df.y,z=df.z)

output_file('test.html')
show(plot)
