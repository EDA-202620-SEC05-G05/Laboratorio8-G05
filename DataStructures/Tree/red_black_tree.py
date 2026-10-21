RED = 0
BLACK = 1
import rbt_node as rb


def rotate_left(h):
    x = h["right"]
    h["right"] = x["left"]
    x["left"] = h
    x["color"] = h["color"]
    h["color"] = RED
    return x


def rotate_right(h):
    x = h["left"]
    h["left"] = x["right"]
    x["right"] = h
    x["color"] = h["color"]
    h["color"] = RED
    return x

def flip_colors(h):
    h["color"] = RED
    h["left"]["color"] = BLACK
    h["right"]["color"] = BLACK


def put(my_rbt, key, value):
    my_rbt["root"] = insert_node(my_rbt["root"], key, value)
    my_rbt["root"]["color"] = BLACK
    return my_rbt


def insert_node(root, key, value):
    if root is None:
        return rb.new_nodenew_node(key, value)

    if key < root["key"]:
        root["left"] = insert_node(root["left"], key, value)
    elif key > root["key"]:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value

    if rb.is_red(root["right"]) and not rb.is_red(root["left"]):
        root = rotate_left(root)
    if rb.is_red(root["left"]) and rb.is_red(root["left"]["left"]):
        root = rotate_right(root)
    if rb.is_red(root["left"]) and rb.is_red(root["right"]):
        flip_colors(root)

    return root