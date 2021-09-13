import gradio

def hello(inp):
  return "Hello {}!".format(inp)

io = gradio.Interface(fn=hello, inputs='text', outputs='text', title='Hello World', 
    description='My first hosted interface!')  
io.launch()
