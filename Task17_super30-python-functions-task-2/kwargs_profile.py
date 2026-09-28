def create_profile(**kwargs):
    # **kwargs collects key-value pairs into a dictionary
    for key, value in kwargs.items():
        print(key, ":", value)

create_profile(name="Rahul", age=22, course="Python", city="Delhi")
