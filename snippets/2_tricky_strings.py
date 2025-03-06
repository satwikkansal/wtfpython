# 1
assert id("some_string") == id("some" + "_" + "string")
assert id("some_string") == id("some_string")

# 2
a = "wtf"
b = "wtf"
assert a is b

a = "wtf!"
b = "wtf!"
assert a is b

# 3
a, b = "wtf!", "wtf!"
assert a is b

a = "wtf!"; b = "wtf!"
assert a is b
