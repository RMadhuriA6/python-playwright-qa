def outer():
    x = 5

    def inner():
        print("inner: " + str(x))

    inner()
    print ('outer')

outer()