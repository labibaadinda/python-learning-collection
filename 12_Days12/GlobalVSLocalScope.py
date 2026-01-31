# the difference between global and local scope is where you define the paramter
# global function available in everywhere u can access in outside of function also inside a function
# while local function is only available inside of that function (function where that variable has defined)

def drink_portion():
    portion = 2
    print(f"this is lokal scope, portion = {portion}")

drink_portion()
portion = 5
print(f"this is global scope, portion = {portion}")
