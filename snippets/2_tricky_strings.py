# 1
assert id("some_string") == id("some" + "_" + "string")
assert id("some_string") == id("some_string")

# 2
a = "wtf"
b = "wtf"
assert a is b

a = "wtf!"
b = "wtf!"
# True because it is invoked in script. Might be False in python shell or ipython
assert a is b

# 3
a, b = "wtf!", "wtf!"
assert a is b

a = "wtf!"; b = "wtf!"  # noqa: E702 - multiline statement
# True because it is invoked in script. Might be False in python shell or ipython
assert a is b

# 4 - not relevant for modern (>3.8) Python version, should be moved to `legacy` section
# a = 'a' * 20
# b = 'aaaaaaaaaaaaaaaaaaaa'
# assert a is b
#
# a = 'a' * 21
# b = 'aaaaaaaaaaaaaaaaaaaa'
# # Fails
# assert a is b
