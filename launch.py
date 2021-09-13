import gradio

def hello(YOUR_NAME):
  return "Hello {}!".format(YOUR_NAME)

io = gradio.Interface(fn=hello, inputs='text', outputs='text', title='Hello World', 
    description='My first hosted interface!',share=True)  
io.launch()
