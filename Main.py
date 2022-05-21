def multiply_and_greet(*number,**student):
    num=1
    for f in number:
        num*=f
        print(num)
    print(f"Hello{student}")