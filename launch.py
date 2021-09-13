import gradio

def hello(inp2):
  return "Hello {}!".format(inp2)

io = gradio.Interface(fn=hello, inputs='text', outputs='text', title='Hello World', 
    description='My first hosted interface!')  
io.launch()
