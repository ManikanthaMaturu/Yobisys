# Q. No.  1. Write a generator function to flatten a deeply nested list so that it yields each element.


def flatten_nested(nested_list):

    for i in nested_list:
        if isinstance(i, list):
            yield from flatten_nested(i) 
        else:
            yield i

nested_list = [2, [5, [12, 4], 98], [26, [37, [48, 91]]]]
flattened = flatten_nested(nested_list)
print("First Question =",list(flattened))

# -----------------------------------------------------------------------------

# Q. No. 2. Create a function that parses a string mathematical expression (like "3 + 2 * (8 / 4)" ) and evaluates it.


def evaluate_exp(exp):

    try:
        result = eval(exp)
        return result
    except Exception as e:
        return f"Error: {e}"

exp = "3 + 2 * (8 / 4)"
print("Second Question =",evaluate_exp(exp))


# ----------------------------------------------------------------------------------------