# closure
# - using closure, inner function can be called outside the outer function
# - function returning a reference of a inner function
# - the inner function can access the all the members of outer function
#   even if the outer function has already lost its scope
#   since the inner function remembers all the members of outer function

# closure
def outer_function(param):
    print("inside outer_function")
    print(f"param = {param}")

    # scope: local
    num = 200

    # scope: local
    def inner_function():
        print(f"inside inner_function")
        print(f"param = {param}")
        print(f"num   = {num}")

    # inner_function()

    # return the reference of inner_function
    return inner_function

# return_value = outer_function(10)
# print(f"return_value = {return_value}, type = {type(return_value)}")

# thi will call the inner_function
# return_value()

# since inner_function is a local function of outer_function
# it can be called only within the outer_function
# inner_function()

# <h1>header 1</h1>
# <p>para 1</p>
# <p>para 2</p>
# <p>para 3</p>

def write_html_tag(tag: str, content: str):
    print(f"<{tag}>{content}</{tag}>")

# write_html_tag('h1', 'header1')
# write_html_tag('p', 'para 1')
# write_html_tag('p', 'para 2')
# write_html_tag('p', 'para 3')
# write_html_tag('p', 'para 4')
# write_html_tag('p', 'para 5')


# closure
def create_tag(tag: str):

    # write the tag and its content
    def write_output(content: str):
        print(f"<{tag}>{content}</{tag}>")

    return write_output
    

# create h1 tag
h1 = create_tag('h1')
h1('header 1')

# create a p tag
p = create_tag('p')
p('para 1')
p('para 2')
p('para 3')
p('para 4')

# create a span tag
span = create_tag('span')
span('span 1')
span('span 2')
span('span 3')