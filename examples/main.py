import justpy as jp

@jp.SetRoute('/home')
def home():
    wp = jp.WebPage()
    div = jp.Div(a=wp, classes="bg-gray-200 h-screen")

    div1 = jp.Div(a=div, classes="grid grid-cols-3 gap-4 p-3")
    jp.Input(a=div1, placeholder="Enter first value",
             classes="form-input")
    jp.Input(a=div1, placeholder="Enter second value",
             classes="form-imput")
    jp.Div(a=div, text="Results goes here...", classes="text-gray-600")
    jp.Div(a=div1, text="Just another div...", classes="text-gray-600")
    jp.Div(a=div1, text="Yet another div", classes="text-gray-600")

    div2= jp.Div(a=div, classes="grid grid-cols-2 gap-4")
    jp.Button(a=div, text="Calculate",
              classes="border border-blue-600 m-2 py-1 px-4 rounded "
              "text-blue-600 hover:bg-red-500 hover:text-white")
    jp.Div(a=div2, text="I am a cool interactive div!")
    return wp

jp.justpy()