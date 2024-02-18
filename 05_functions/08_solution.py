# Function with **kwargs

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
print_kwargs(name = "Swayam", power = "Honest")
print_kwargs(name = "Swayam")
print_kwargs(name = "Swayam", power = "Honest", enemy = "Fear")
