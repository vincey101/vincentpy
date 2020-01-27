def country(state, state2, state3="pelumi state"):
    print(state, state2, state3)


# country("lagos","abuja")
# country(state2="abuja", state="lagos", state3="kwara")

def country2(*args,**kwargs):
    print(args)
    print(kwargs)
# country2("lagos","abuja","kwara")
country2(state2="abuja",state="lagos",state3 ="kwara")
