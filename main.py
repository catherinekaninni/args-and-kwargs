def multiply_and_greet(*args,**kwargs):
    product =1
    for i in args:
        product*= i
    print(product)
    keys=kwargs.keys()
    if "country" in keys:
        print (f"hello {kwargs['name']} from {kwargs['country']}")
    elif"age" in keys:
        year=2022-kwargs["age"]
        print(f"hello {kwargs['name']}you were born in {year}") 
    elif "name" in keys:
        print(f"hello{kwargs['name']}")
    else:
        print(f"hello Alien")
